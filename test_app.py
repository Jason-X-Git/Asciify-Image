from fastapi import status
import pytest
from main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


def test_status_request(client):
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_images(client):
    response = client.get("/images")
    assert response.status_code == 200


def test_get_image(client):
    response = client.get("/images/DO_NOT_EXIST")
    assert response.status_code == status.HTTP_404_NOT_FOUND
