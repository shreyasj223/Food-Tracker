import os
import json
import uuid
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs.json")

def load_db():
    if not os.path.exists(DB_FILE):
        return {"meals": []}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {"meals": []}

def save_db(data):
    try:
        with open(DB_FILE, "w") as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving database: {e}")
        return False

def get_today_meals():
    db = load_db()
    today_str = datetime.now().strftime("%Y-%m-%d")
    today_meals = []
    
    for meal in db.get("meals", []):
        # We store timestamp as ISO string, so we extract YYYY-MM-DD
        if meal.get("timestamp", "").startswith(today_str):
            today_meals.append(meal)
            
    return today_meals

def log_meal(name, portion_g, calories, protein, carbs, fat, source="manual"):
    db = load_db()
    
    meal = {
        "id": str(uuid.uuid4()),
        "name": name,
        "portion_g": float(portion_g),
        "calories": float(calories),
        "protein": float(protein),
        "carbs": float(carbs),
        "fat": float(fat),
        "source": source, # e.g., 'vit-food101', 'yolo-coco', 'manual'
        "timestamp": datetime.now().isoformat()
    }
    
    if "meals" not in db:
        db["meals"] = []
        
    db["meals"].append(meal)
    save_db(db)
    return meal

def delete_meal(meal_id):
    db = load_db()
    meals = db.get("meals", [])
    
    initial_len = len(meals)
    db["meals"] = [m for m in meals if m.get("id") != meal_id]
    
    if len(db["meals"]) < initial_len:
        save_db(db)
        return True
    return False

def get_daily_summary():
    meals = get_today_meals()
    summary = {
        "calories": 0.0,
        "protein": 0.0,
        "carbs": 0.0,
        "fat": 0.0,
        "count": len(meals)
    }
    
    for m in meals:
        summary["calories"] += m.get("calories", 0.0)
        summary["protein"] += m.get("protein", 0.0)
        summary["carbs"] += m.get("carbs", 0.0)
        summary["fat"] += m.get("fat", 0.0)
        
    # Round to 1 decimal place
    summary["calories"] = round(summary["calories"], 1)
    summary["protein"] = round(summary["protein"], 1)
    summary["carbs"] = round(summary["carbs"], 1)
    summary["fat"] = round(summary["fat"], 1)
    
    return summary
