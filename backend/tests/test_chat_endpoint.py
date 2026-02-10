"""Tests for the chat HTTP endpoint."""
from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    # Patch dependencies before importing app
    with patch("app.dependencies.startup") as mock_startup:
        from app.main import app

        return TestClient(app)


@pytest.fixture
def mock_pipeline():
    pipeline = MagicMock()
    pipeline.query.return_value = "Test response from pipeline"
    return pipeline


def test_chat_endpoint(client, mock_pipeline):
    with patch("app.routers.chat.get_pipeline", return_value=mock_pipeline):
        response = client.post("/api/chat", json={"message": "Hvordan logger jeg inn?"})

    assert response.status_code == 200
    data = response.json()
    assert "response" in data
    assert data["response"] == "Test response from pipeline"


def test_chat_endpoint_empty_message(client, mock_pipeline):
    with patch("app.routers.chat.get_pipeline", return_value=mock_pipeline):
        response = client.post("/api/chat", json={"message": ""})

    # FastAPI will still accept it — pipeline handles empty messages
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_missing_field(client):
    response = client.post("/api/chat", json={})
    assert response.status_code == 422  # Validation error
