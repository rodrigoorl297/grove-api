from fastapi.testclient import TestClient

from app.auth import create_token
from app.main import app

client = TestClient(app)


def auth_header() -> dict[str, str]:
    return {"Authorization": f"Bearer {create_token('test-user')}"}


def test_requires_auth_and_crud():
    denied = client.get("/api/v1/shipments")
    assert denied.status_code == 401

    created = client.post(
        "/api/v1/shipments",
        headers=auth_header(),
        json={
            "tracking_code": "ref-001",
            "origin": "alpha",
            "destination": "beta",
            "status": "created",
        },
    )
    assert created.status_code == 201
    item_id = created.json()["id"]

    listed = client.get("/api/v1/shipments", headers=auth_header())
    assert listed.status_code == 200
    assert any(row["id"] == item_id for row in listed.json())
