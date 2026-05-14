# Cloud Health API (Docker)

A tiny **FastAPI** service packaged for **Docker** and **Docker Compose**, with **liveness-style** `/health`, **readiness** `/ready`, and interactive **OpenAPI** docs at `/docs`.

## Quick start

```bash
docker compose up --build
```

Then open:

- http://localhost:8080/docs — Swagger UI  
- http://localhost:8080/health — `{"status":"ok"}`  
- http://localhost:8080/ready — `{"ready":true}`  

## Run without Compose

```bash
docker build -t cloud-health-api .
docker run --rm -p 8080:8000 cloud-health-api
```

## Local dev (no Docker)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## License

MIT
