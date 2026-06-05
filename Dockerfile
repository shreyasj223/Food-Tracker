FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    HF_HUB_DISABLE_SYMLINKS_WARNING=1

WORKDIR /app

# Install system dependencies (OpenCV requires libGL and libglib)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast package installation
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install dependencies directly into the system environment (since we are inside Docker)
RUN uv pip install --system --no-cache fastapi uvicorn python-multipart ultralytics transformers torch torchvision pillow numpy

# Copy project files
COPY . .


# Expose port (Render overrides this with $PORT env var)
EXPOSE 8000

# Start FastAPI server, binding to 0.0.0.0 and respecting Render's $PORT env var
CMD uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}
