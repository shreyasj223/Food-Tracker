// Configuration Targets
const TARGETS = {
    calories: 2000,
    protein: 130,
    carbs: 250,
    fats: 70
};

const CIRCUMFERENCE = 2 * Math.PI * 84; // Radius of SVG circle is 84

// Resolve the backend endpoint dynamically for local/remote hosting
function getApiUrl(path) {
    const isLocal = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
    let base = '';
    if (!isLocal) {
        base = localStorage.getItem('backend_url') || '';
        if (base && !base.endsWith('/')) {
            base += '/';
        }
    }
    // Remove leading slash if any
    const cleanPath = path.startsWith('/') ? path.substring(1) : path;
    return base + cleanPath;
}

// State variables
let activeTab = 'upload';
let stream = null;
let currentPredictions = null;
let selectedPredictionIndex = 0; // index in current list

// DOM Elements
const tabUpload = document.getElementById('tab-upload');
const tabCamera = document.getElementById('tab-camera');
const uploadPlaceholder = document.getElementById('upload-placeholder');
const fileInput = document.getElementById('file-input');
const webcamFeed = document.getElementById('webcam-feed');
const previewImg = document.getElementById('preview-img');
const bboxOverlay = document.getElementById('bbox-overlay');
const btnReset = document.getElementById('btn-reset');
const btnSnap = document.getElementById('btn-snap');
const loader = document.getElementById('loader');
const loaderMsg = document.getElementById('loader-msg');
const scanner = document.getElementById('scanner');
const resultsCard = document.getElementById('results-card');
const resultsMeta = document.getElementById('results-meta');
const predictionsList = document.getElementById('predictions-list');
const btnLogMeal = document.getElementById('btn-log-meal');
const viewport = document.getElementById('viewport');

// Settings Elements
const btnSettings = document.getElementById('btn-settings');
const settingsPanel = document.getElementById('settings-panel');
const backendUrlInput = document.getElementById('backend-url-input');
const btnSaveSettings = document.getElementById('btn-save-settings');

// Progress Indicator Elements
const calorieCircle = document.getElementById('calorie-progress-circle');
const loggedCalories = document.getElementById('logged-calories');
const loggedProtein = document.getElementById('logged-protein');
const loggedCarbs = document.getElementById('logged-carbs');
const loggedFats = document.getElementById('logged-fats');
const barProtein = document.getElementById('bar-protein');
const barCarbs = document.getElementById('bar-carbs');
const barFats = document.getElementById('bar-fats');
const foodLogList = document.getElementById('food-log-list');
const emptyLogPlaceholder = document.getElementById('empty-log-placeholder');

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    initTabs();
    initUpload();
    initCameraControls();
    initSettings();
    initDate();
    refreshData();
});

// Setup current date readable string
function initDate() {
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    document.getElementById('current-date').innerHTML = `
        <i class="fa-regular fa-calendar-days" style="margin-right: 0.5rem;"></i>
        ${new Date().toLocaleDateString('en-US', options)}
    `;
}

// Tab Switching logic
function initTabs() {
    tabUpload.addEventListener('click', () => {
        if (activeTab === 'upload') return;
        activeTab = 'upload';
        tabUpload.classList.add('active');
        tabCamera.classList.remove('active');
        stopCamera();
        resetUI();
    });

    tabCamera.addEventListener('click', () => {
        if (activeTab === 'camera') return;
        activeTab = 'camera';
        tabCamera.classList.add('active');
        tabUpload.classList.remove('active');
        resetUI();
        startCamera();
    });
}

// Camera control handlers
async function startCamera() {
    uploadPlaceholder.style.display = 'none';
    previewImg.style.display = 'none';
    webcamFeed.style.display = 'block';
    btnSnap.style.display = 'flex';
    viewport.classList.add('active-stream');
    
    try {
        stream = await navigator.mediaDevices.getUserMedia({
            video: { facingMode: 'environment', width: 800, height: 600 },
            audio: false
        });
        webcamFeed.srcObject = stream;
    } catch (err) {
        console.error("Camera access failed:", err);
        alert("Could not access camera. Please check permissions or switch to File Upload mode.");
        tabUpload.click();
    }
}

function stopCamera() {
    if (stream) {
        stream.getTracks().forEach(track => track.stop());
        stream = null;
    }
    webcamFeed.srcObject = null;
    webcamFeed.style.display = 'none';
    btnSnap.style.display = 'none';
    viewport.classList.remove('active-stream');
}

function initCameraControls() {
    btnSnap.addEventListener('click', () => {
        if (!stream) return;
        
        // Render webcam video frame to static canvas to export image blob
        const tempCanvas = document.createElement('canvas');
        tempCanvas.width = webcamFeed.videoWidth || 640;
        tempCanvas.height = webcamFeed.videoHeight || 480;
        
        const ctx = tempCanvas.getContext('2d');
        // Mirror back the capture
        ctx.translate(tempCanvas.width, 0);
        ctx.scale(-1, 1);
        ctx.drawImage(webcamFeed, 0, 0, tempCanvas.width, tempCanvas.height);
        
        tempCanvas.toBlob(blob => {
            const capturedFile = new File([blob], "capture.jpg", { type: "image/jpeg" });
            
            // Render captured frame on static preview image element
            const dataUrl = tempCanvas.toDataURL('image/jpeg');
            previewImg.src = dataUrl;
            previewImg.style.display = 'block';
            webcamFeed.style.display = 'none';
            btnSnap.style.display = 'none';
            stopCamera();
            
            uploadAndAnalyze(capturedFile);
        }, 'image/jpeg');
    });
}

// Drag, Drop, and File Input actions
function initUpload() {
    uploadPlaceholder.addEventListener('click', () => fileInput.click());
    
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleUploadedFile(e.target.files[0]);
        }
    });

    uploadPlaceholder.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadPlaceholder.style.background = 'rgba(255, 255, 255, 0.05)';
    });

    uploadPlaceholder.addEventListener('dragleave', () => {
        uploadPlaceholder.style.background = 'transparent';
    });

    uploadPlaceholder.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadPlaceholder.style.background = 'transparent';
        if (e.dataTransfer.files.length > 0) {
            handleUploadedFile(e.dataTransfer.files[0]);
        }
    });
    
    btnReset.addEventListener('click', () => {
        resetUI();
        if (activeTab === 'camera') {
            startCamera();
        }
    });
}

function handleUploadedFile(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImg.src = e.target.result;
        previewImg.style.display = 'block';
        uploadPlaceholder.style.display = 'none';
        uploadAndAnalyze(file);
    };
    reader.readAsDataURL(file);
}

// API interaction: Analysis upload
async function uploadAndAnalyze(file) {
    const formData = new FormData();
    formData.append('file', file);
    
    showLoader("Analyzing dish and ingredients...");
    resetOverlays();
    
    try {
        const res = await fetch(getApiUrl('/api/analyze'), {
            method: 'POST',
            body: formData
        });
        
        if (!res.ok) throw new Error("Server analysis failed");
        
        const data = await res.json();
        renderAnalysisResults(data);
    } catch (err) {
        console.error("Analysis failed:", err);
        alert("Meal analysis failed. Please verify the backend server is running.");
        resetUI();
    } finally {
        hideLoader();
    }
}

// Visual indicator toggles
function showLoader(msg) {
    loaderMsg.textContent = msg;
    loader.style.display = 'flex';
    scanner.style.display = 'block';
}

function hideLoader() {
    loader.style.display = 'none';
    scanner.style.display = 'none';
}

function resetUI() {
    resetOverlays();
    previewImg.style.display = 'none';
    previewImg.src = '';
    uploadPlaceholder.style.display = 'flex';
    resultsCard.style.display = 'none';
    btnReset.style.display = 'none';
    fileInput.value = '';
    currentPredictions = null;
}

function resetOverlays() {
    bboxOverlay.innerHTML = '';
}

// Render predictions with reactive sliders
function renderAnalysisResults(data) {
    currentPredictions = [];
    selectedPredictionIndex = 0;
    
    // Combine full plate dish predictions (from ViT) and ingredients (from YOLO)
    // We filter predictions so that we have clean unique entries
    const items = [];
    
    // Dishes (ViT model output)
    data.dishes.forEach(dish => {
        items.push({
            type: 'dish',
            label: dish.class_name,
            name: dish.display_name,
            confidence: dish.confidence,
            calories: dish.calories_per_100g,
            protein: dish.protein_per_100g,
            carbs: dish.carbs_per_100g,
            fat: dish.fat_per_100g,
            weight: dish.default_serving_g,
            box: null
        });
    });
    
    // Ingredients (YOLO model output)
    data.ingredients.forEach(ing => {
        items.push({
            type: 'ingredient',
            label: ing.class_name,
            name: ing.display_name,
            confidence: ing.confidence,
            calories: ing.calories_per_100g,
            protein: ing.protein_per_100g,
            carbs: ing.carbs_per_100g,
            fat: ing.fat_per_100g,
            weight: ing.default_serving_g,
            box: ing.box
        });
    });
    
    currentPredictions = items;
    resultsMeta.textContent = `Analyzed in ${data.execution_time_sec} seconds. Select a prediction to edit portion size:`;
    
    // Set preview image back to show the relative paths from the backend (so it serves uploaded images correctly)
    if (data.image_url) {
        previewImg.src = getApiUrl(data.image_url);
    }
    
    renderPredictionList();
    renderBoundingBoxes();
    
    resultsCard.style.display = 'block';
    btnReset.style.display = 'flex';
}

function renderPredictionList() {
    predictionsList.innerHTML = '';
    
    if (currentPredictions.length === 0) {
        predictionsList.innerHTML = `<p style="text-align: center; color: var(--text-muted);">No food detected. Try uploading a clearer picture.</p>`;
        return;
    }
    
    currentPredictions.forEach((pred, index) => {
        const item = document.createElement('div');
        item.className = `prediction-item ${index === selectedPredictionIndex ? 'selected' : ''}`;
        item.addEventListener('click', () => selectPrediction(index));
        
        // Calculate initial macros
        const portionFactor = pred.weight / 100;
        const curCal = Math.round(pred.calories * portionFactor);
        const curProt = Math.round(pred.protein * portionFactor * 10) / 10;
        const curCarb = Math.round(pred.carbs * portionFactor * 10) / 10;
        const curFat = Math.round(pred.fat * portionFactor * 10) / 10;
        
        item.innerHTML = `
            <div class="pred-header">
                <div class="pred-name-badge">
                    <div class="radio-circle"></div>
                    <span class="pred-title">${pred.name}</span>
                    <span style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase;">(${pred.type})</span>
                </div>
                <span class="pred-confidence">${Math.round(pred.confidence * 100)}% Match</span>
            </div>
            
            ${index === selectedPredictionIndex ? `
                <div class="portion-slider-group" onclick="event.stopPropagation();">
                    <div class="slider-labels">
                        <span>Portion Weight:</span>
                        <strong style="color: var(--color-accent);"><span id="slider-weight-lbl-${index}">${pred.weight}</span>g</strong>
                    </div>
                    <input type="range" class="weight-slider" id="slider-weight-${index}" min="10" max="800" step="5" value="${pred.weight}">
                </div>
            ` : ''}
            
            <div class="calculated-macros-grid">
                <div class="macro-box">
                    <span class="macro-box-val cal" id="cal-lbl-${index}">${curCal}</span>
                    <span class="macro-box-lbl">kcal</span>
                </div>
                <div class="macro-box">
                    <span class="macro-box-val prot" id="prot-lbl-${index}">${curProt}g</span>
                    <span class="macro-box-lbl">prot</span>
                </div>
                <div class="macro-box">
                    <span class="macro-box-val carb" id="carb-lbl-${index}">${curCarb}g</span>
                    <span class="macro-box-lbl">carbs</span>
                </div>
                <div class="macro-box">
                    <span class="macro-box-val fat" id="fat-lbl-${index}">${curFat}g</span>
                    <span class="macro-box-lbl">fats</span>
                </div>
            </div>
        `;
        
        predictionsList.appendChild(item);
        
        // Bind slider event
        if (index === selectedPredictionIndex) {
            const slider = item.querySelector(`#slider-weight-${index}`);
            if (slider) {
                slider.addEventListener('input', (e) => {
                    const weightVal = parseInt(e.target.value);
                    pred.weight = weightVal;
                    
                    // Update UI text labels
                    document.getElementById(`slider-weight-lbl-${index}`).textContent = weightVal;
                    
                    const newFactor = weightVal / 100;
                    document.getElementById(`cal-lbl-${index}`).textContent = Math.round(pred.calories * newFactor);
                    document.getElementById(`prot-lbl-${index}`).textContent = (Math.round(pred.protein * newFactor * 10) / 10) + 'g';
                    document.getElementById(`carb-lbl-${index}`).textContent = (Math.round(pred.carbs * newFactor * 10) / 10) + 'g';
                    document.getElementById(`fat-lbl-${index}`).textContent = (Math.round(pred.fat * newFactor * 10) / 10) + 'g';
                });
            }
        }
    });
}

function selectPrediction(index) {
    if (selectedPredictionIndex === index) return;
    selectedPredictionIndex = index;
    renderPredictionList();
    renderBoundingBoxes();
}

// Bounding boxes drawn on viewport overlay
function renderBoundingBoxes() {
    bboxOverlay.innerHTML = '';
    
    currentPredictions.forEach((pred, index) => {
        if (!pred.box) return; // Only ingredients have boxes
        
        const boxDiv = document.createElement('div');
        boxDiv.className = 'bbox-rect';
        
        // Apply relative box coordinates
        boxDiv.style.left = `${pred.box.x}%`;
        boxDiv.style.top = `${pred.box.y}%`;
        boxDiv.style.width = `${pred.box.w}%`;
        boxDiv.style.height = `${pred.box.h}%`;
        
        // Highlight active selection
        if (index === selectedPredictionIndex) {
            boxDiv.style.borderColor = 'var(--color-cal)';
            boxDiv.style.boxShadow = '0 0 16px var(--color-cal)';
            boxDiv.style.zIndex = '20';
        } else {
            boxDiv.style.borderColor = 'var(--color-accent)';
            boxDiv.style.boxShadow = '0 0 8px var(--border-glow)';
            boxDiv.style.zIndex = '12';
        }
        
        // Add label text
        const labelSpan = document.createElement('span');
        labelSpan.className = 'bbox-label';
        labelSpan.textContent = pred.name;
        if (index === selectedPredictionIndex) {
            labelSpan.style.background = 'var(--color-cal)';
        }
        boxDiv.appendChild(labelSpan);
        
        // Clicking box selects corresponding list item
        boxDiv.addEventListener('click', (e) => {
            e.stopPropagation();
            selectPrediction(index);
        });
        
        bboxOverlay.appendChild(boxDiv);
    });
}

// Add prediction details to logged history database
btnLogMeal.addEventListener('click', async () => {
    if (!currentPredictions || currentPredictions.length === 0) return;
    
    const pred = currentPredictions[selectedPredictionIndex];
    const factor = pred.weight / 100;
    
    const logPayload = {
        name: pred.name,
        portion_g: pred.weight,
        calories: Math.round(pred.calories * factor),
        protein: Math.round(pred.protein * factor * 10) / 10,
        carbs: Math.round(pred.carbs * factor * 10) / 10,
        fat: Math.round(pred.fat * factor * 10) / 10,
        source: pred.type
    };
    
    showLoader("Logging meal to dashboard...");
    
    try {
        const res = await fetch(getApiUrl('/api/log'), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(logPayload)
        });
        
        if (!res.ok) throw new Error("Failed to log meal");
        
        // Refresh values and close results panel
        resetUI();
        await refreshData();
        
    } catch (err) {
        console.error("Logging failed:", err);
        alert("Failed to log meal. Please check server connection.");
    } finally {
        hideLoader();
    }
});

// Fetch current totals and lists to rebuild page metrics
async function refreshData() {
    try {
        const [summaryRes, mealsRes] = await Promise.all([
            fetch(getApiUrl('/api/summary')),
            fetch(getApiUrl('/api/meals'))
        ]);
        
        if (!summaryRes.ok || !mealsRes.ok) throw new Error("Failed to sync dashboard metrics");
        
        const summary = await summaryRes.json();
        const meals = await mealsRes.json();
        
        updateMetricsDisplay(summary);
        updateMealsTimeline(meals);
    } catch (err) {
        console.error("Sync data error:", err);
    }
}

// Update Calories Ring and Macro Horizontal Bars
function updateMetricsDisplay(summary) {
    // 1. Calorie values
    const calVal = Math.round(summary.calories);
    loggedCalories.textContent = calVal;
    
    // 2. Animate SVG circle
    const calPct = Math.min((calVal / TARGETS.calories) * 100, 100);
    const offset = CIRCUMFERENCE - (calPct / 100) * CIRCUMFERENCE;
    calorieCircle.style.strokeDashoffset = offset;
    
    // Set circle color to coral if exceeded target limit
    if (calVal > TARGETS.calories) {
        calorieCircle.style.stroke = 'var(--color-prot)';
    } else {
        calorieCircle.style.stroke = 'var(--color-cal)';
    }
    
    // 3. Macros values and bars
    loggedProtein.textContent = Math.round(summary.protein);
    const protPct = Math.min((summary.protein / TARGETS.protein) * 100, 100);
    barProtein.style.width = `${protPct}%`;
    
    loggedCarbs.textContent = Math.round(summary.carbs);
    const carbPct = Math.min((summary.carbs / TARGETS.carbs) * 100, 100);
    barCarbs.style.width = `${carbPct}%`;
    
    loggedFats.textContent = Math.round(summary.fat);
    const fatPct = Math.min((summary.fat / TARGETS.fats) * 100, 100);
    barFats.style.width = `${fatPct}%`;
}

// Update scroll list of today's eaten items
function updateMealsTimeline(meals) {
    foodLogList.innerHTML = '';
    
    if (meals.length === 0) {
        foodLogList.appendChild(emptyLogPlaceholder);
        return;
    }
    
    meals.slice().reverse().forEach(meal => {
        const item = document.createElement('div');
        item.className = 'timeline-item';
        
        // Extract hour:minute AM/PM from ISO timestamp
        let timeStr = '';
        if (meal.timestamp) {
            try {
                const date = new Date(meal.timestamp);
                timeStr = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            } catch (e) {
                timeStr = 'Now';
            }
        }
        
        item.innerHTML = `
            <div class="timeline-info">
                <span class="timeline-name">${meal.name}</span>
                <span class="timeline-meta">${meal.portion_g}g • Logged at ${timeStr} via ${meal.source}</span>
                <div class="timeline-macros">
                    <span><strong>${Math.round(meal.calories)}</strong> kcal</span>
                    <span>P: <strong>${Math.round(meal.protein)}</strong>g</span>
                    <span>C: <strong>${Math.round(meal.carbs)}</strong>g</span>
                    <span>F: <strong>${Math.round(meal.fat)}</strong>g</span>
                </div>
            </div>
            <button class="delete-btn" title="Delete meal entry" onclick="deleteMealEntry('${meal.id}')">
                <i class="fa-regular fa-trash-can"></i>
            </button>
        `;
        
        foodLogList.appendChild(item);
    });
}

// Trigger meal deletion
async function deleteMealEntry(id) {
    if (!confirm("Are you sure you want to delete this log entry?")) return;
    
    try {
        const res = await fetch(getApiUrl(`/api/meals/${id}`), {
            method: 'DELETE'
        });
        
        if (!res.ok) throw new Error("Delete request failed");
        
        await refreshData();
    } catch (err) {
        console.error("Delete failed:", err);
        alert("Failed to delete log entry.");
    }
}
window.deleteMealEntry = deleteMealEntry; // expose to window for HTML click handlers

// Initialize connection settings actions
function initSettings() {
    // Load stored backend URL
    const storedUrl = localStorage.getItem('backend_url') || '';
    backendUrlInput.value = storedUrl;

    // Toggle settings visibility
    btnSettings.addEventListener('click', () => {
        const isHidden = settingsPanel.style.display === 'none';
        settingsPanel.style.display = isHidden ? 'block' : 'none';
    });

    // Save settings action
    btnSaveSettings.addEventListener('click', () => {
        let urlVal = backendUrlInput.value.trim();
        
        if (urlVal) {
            // Automatically clean protocol or formatting if needed
            if (!urlVal.startsWith('http://') && !urlVal.startsWith('https://')) {
                urlVal = 'https://' + urlVal;
            }
        }
        
        localStorage.setItem('backend_url', urlVal);
        backendUrlInput.value = urlVal;
        settingsPanel.style.display = 'none';
        
        // Flash save visual feedback
        alert("Backend URL saved successfully! Syncing dashboard data...");
        refreshData();
    });
}
