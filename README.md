# NutriLens AI: Smart Food Photo Calorie & Macro Tracker

NutriLens AI is a fully local, interactive web application that estimates calories and macronutrients (proteins, carbs, fats) from photos of meals or live webcam feeds. It utilizes dual local computer vision models to perform dish classification and ingredient tracking entirely on your machine.

## 🚀 Features

- **Dual-Model ML Pipeline**:
  - **Full-Plate Classifier**: Vision Transformer (ViT) fine-tuned on the Food-101 dataset to identify mixed dishes (sushi, pizza, lasagna, etc.).
  - **Ingredient Detector**: YOLOv8 to locate and outline individual fruits, vegetables, and generic items (apple, orange, sandwich, broccoli, etc.) with bounding boxes.
- **Interactive Dashboard**:
  - Drag-and-drop file uploader and live webcam snap interface.
  - Interactive SVG bounding box overlays drawn dynamically over images.
  - Recalculates nutritional data in real-time as portion sizes (grams) are adjusted via sliders.
- **Progress Tracking & Analytics**:
  - Radial target gauge tracking consumed calories against daily limit (2000 kcal).
  - Horizontal progress indicators for macronutrient targets (Protein, Carbs, Fats).
  - Chronological timeline logging past meals locally.
- **100% Offline Capable**: All model inferences run fully locally on CPU. No API keys or external cloud subscriptions required.

---

## 🛠️ Architecture

```
d:\food-tracker/
├── backend/
│   ├── main.py            # FastAPI server, endpoints, and static files router
│   ├── cv_engine.py       # YOLOv8 and ViT model wrappers with lazy loading
│   ├── nutrition_db.py    # Reference database with macro metrics for 100+ foods
│   └── database.py        # Local JSON persistence system for logging meals
├── frontend/
│   ├── index.html         # Dashboard layout
│   ├── styles.css         # Glassmorphism dark-theme stylesheets
│   └── app.js             # Client webcam streams, annotation overlays, and macro math
├── run.bat                # Easy-launch launcher script for Windows
├── pyproject.toml         # UV dependency specification
└── .gitignore             # Git ignore targets (.venv, caches, logs, images)
```

---

## 🔧 Installation & Setup

This project uses **[uv](https://github.com/astral-sh/uv)**, an extremely fast Python package installer and resolver.

### 1. Prerequisites
Make sure `uv` is installed on your machine. If you don't have it, install it via:
* **Windows (PowerShell)**:
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

### 2. Run the Application
You can start the server instantly using the provided batch script:
- Double-click **`run.bat`** in the project directory.

Alternatively, open your terminal in the project directory and run:
```bash
uv run python -m backend.main
```

> **Note**: On the very first run, `uv` will download Python, build the virtual environment, install PyTorch, and download the pre-trained models (~350MB total). Subsequent startups are near-instantaneous.

### 3. Open the Dashboard
Open your browser and navigate to:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 🥗 Nutritional Database
Macronutrient and calorie estimations are loaded from a local database map per 100g. You can customize the reference serving weights or add custom foods directly in `backend/nutrition_db.py`.
