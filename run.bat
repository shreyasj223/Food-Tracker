@echo off
title NutriLens AI - Smart Food Tracker
echo =======================================================
echo               NUTRIENS AI LAUNCHER
echo =======================================================
echo.
echo Starting FastAPI Backend Server via UV...
echo Note: If this is the first run, UV will download 
echo Python and install dependencies (including PyTorch).
echo It will also download YOLOv8 and ViT-Food101 models (~350MB).
echo This might take a few minutes depending on your internet.
echo.
echo Server will be available at: http://localhost:8000
echo =======================================================
echo.

uv run python -m backend.main

if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] Server failed to start.
    echo Please make sure 'uv' is installed and in your PATH.
    pause
)
