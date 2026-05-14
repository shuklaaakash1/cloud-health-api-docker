"""Minimal container-friendly API — health checks and service metadata."""

from fastapi import FastAPI

app = FastAPI(
    title="Cloud Health API",
    description="Small FastAPI service packaged with Docker for demos and portfolio.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "cloud-health-api",
        "docs": "/docs",
        "health": "/health",
        "readiness": "/ready",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    return {"ready": True}
