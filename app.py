import os
import uvicorn
import gradio as gr
from backend.main import app

# Create a simple Gradio blocks page to satisfy Hugging Face's space status check
with gr.Blocks(title="NutriLens AI System Status") as demo:
    gr.Markdown("# 🥗 NutriLens AI - Smart Food Tracker Backend")
    gr.Markdown("The backend server is running successfully!")
    gr.Markdown("API status: **Active**")
    gr.Markdown(f"Serving frontend index dashboard at: [https://{os.environ.get('SPACE_SUBDOMAIN', 'localhost')}.hf.space](https://{os.environ.get('SPACE_SUBDOMAIN', 'localhost')}.hf.space)")

# Mount the Gradio interface onto our FastAPI app under root '/'
# This lets Hugging Face's SDK embedding discover the Gradio configuration at root routes (e.g. /config)
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    # Hugging Face Spaces automatically configure the PORT env var, defaulting to 7860
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
