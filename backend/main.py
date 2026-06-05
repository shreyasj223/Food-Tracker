import os
import shutil
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.nutrition_db import get_nutrition_data
from backend.cv_engine import analyze_image, load_models
from backend.database import get_today_meals, log_meal, delete_meal, get_daily_summary

# Setup folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(FRONTEND_DIR, exist_ok=True)

app = FastAPI(title="Smart Food Photo Calorie & Macro Tracker API")

# Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Preload models in background on startup
@app.on_event("startup")
def startup_event():
    # We can trigger lazy loading or load immediately
    # Loading immediately means the first upload request is fast, 
    # but the server startup log will show when it's ready.
    try:
        load_models()
    except Exception as e:
        print(f"Startup warning: could not load ML models: {e}")

class MealLogRequest(BaseModel):
    name: str
    portion_g: float
    calories: float
    protein: float
    carbs: float
    fat: float
    source: str = "manual"

@app.get("/api/meals")
def get_meals():
    try:
        return get_today_meals()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/summary")
def get_summary():
    try:
        return get_daily_summary()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/log")
def log_new_meal(req: MealLogRequest):
    try:
        meal = log_meal(
            name=req.name,
            portion_g=req.portion_g,
            calories=req.calories,
            protein=req.protein,
            carbs=req.carbs,
            fat=req.fat,
            source=req.source
        )
        return {"status": "success", "meal": meal, "summary": get_daily_summary()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/meals/{meal_id}")
def delete_logged_meal(meal_id: str):
    try:
        success = delete_meal(meal_id)
        if not success:
            raise HTTPException(status_code=404, detail="Meal not found")
        return {"status": "success", "summary": get_daily_summary()}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/analyze")
async def analyze_food_image(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image.")
        
    # Save the file temporarily
    file_ext = os.path.splitext(file.filename)[1]
    temp_file_name = f"upload_{os.urandom(8).hex()}{file_ext}"
    temp_file_path = os.path.join(UPLOAD_DIR, temp_file_name)
    
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save temporary image: {e}")
        
    # Run the CV engine
    try:
        raw_results = analyze_image(temp_file_path)
    except Exception as e:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=f"Inference failure: {e}")
        
    # Map predictions to nutritional details
    enhanced_dishes = []
    for dish in raw_results["dish_predictions"]:
        nutri_info = get_nutrition_data(dish["class_name"])
        enhanced_dishes.append({
            "class_name": dish["class_name"],
            "confidence": dish["confidence"],
            "display_name": nutri_info["name"],
            "calories_per_100g": nutri_info["calories"],
            "protein_per_100g": nutri_info["protein"],
            "carbs_per_100g": nutri_info["carbs"],
            "fat_per_100g": nutri_info["fat"],
            "default_serving_g": nutri_info["serving_size"]
        })
        
    enhanced_ingredients = []
    for ing in raw_results["ingredients"]:
        nutri_info = get_nutrition_data(ing["class_name"])
        enhanced_ingredients.append({
            "class_name": ing["class_name"],
            "confidence": ing["confidence"],
            "box": ing["box"],
            "visual_size_score": ing["visual_size_score"],
            "display_name": nutri_info["name"],
            "calories_per_100g": nutri_info["calories"],
            "protein_per_100g": nutri_info["protein"],
            "carbs_per_100g": nutri_info["carbs"],
            "fat_per_100g": nutri_info["fat"],
            "default_serving_g": nutri_info["serving_size"]
        })
        
    # Build complete analysis report
    report = {
        "dishes": enhanced_dishes,
        "ingredients": enhanced_ingredients,
        "image_url": f"/uploads/{temp_file_name}", # Serve the uploaded image back
        "execution_time_sec": raw_results["execution_time_sec"]
    }
    
    return report

# Serve uploads folder for visual feedback
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Serve frontend at root
if os.path.exists(FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
else:
    print(f"Warning: Frontend directory '{FRONTEND_DIR}' does not exist yet. Static files will not be served.")


if __name__ == "__main__":
    import uvicorn
    # Set host and port
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
