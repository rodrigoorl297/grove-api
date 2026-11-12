# Grove API

rastreio de envios, SLA e eventos de status em uma API unica.

Recorte de **logistica / tracking**: operacoes nao enxergam atrasos de entrega ate o cliente reclamar.

## Stack

FastAPI, SQLAlchemy 2, PyJWT, Pytest, Docker.

## Setup

Copy `.env.example` to `.env` and set a real `SECRET_KEY`. Do not commit `.env`.

```bash
python -m venv .venv
.venv/Scripts/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
pytest -q
```

Issue a local token after the app can import settings:

```bash
python -c "from app.auth import create_token; print(create_token('local'))"
```

## Docker

```bash
docker compose up --build
```
