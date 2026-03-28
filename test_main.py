from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_sheep():
    response = client.get("/sheep/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "Female"
    }

def test_update_sheep():
    sheep_data = {
        "id": 2,
        "name": "Bella",
        "breed": "Suffolk",
        "sex": "Female"
    }

    response = client.post("/sheep/", json=sheep_data)
    assert response.status_code == 201

    updated_data = {
        "id": 2,
        "name": "Bella Updated",
        "breed": "Suffolk",
        "sex": "Female"
    }

    response = client.put("/sheep/2", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Bella Updated"
    