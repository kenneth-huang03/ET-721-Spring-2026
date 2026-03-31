"""
Kenneth Huang
March 31st, 2026
Rest API Unit Testing
"""

import pytest

from app import FApp, items

@pytest.fixture
def client():
    FApp.config["TESTING"] = True

    with FApp.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_Create_item(client):
    response = client.post("/items", json={"name": "Book", "price": 10})
    
    assert response.status_code == 201

    data = response.get_json()

    assert "id" in data
    assert data["item"]["name"] == "Book"
    assert data["item"]["price"] == 10


def test_get_single_item(client):
    client.post("/items", json={"name": "Laptop", "price": 980})

    response = client.get("/items/2")

    assert response.status_code == 200

    data = response.get_json()
    
    assert data["name"] == "Laptop"
    assert data["price"] == 980


def test_get_all_items(client):
    client.post("/items", json={"name": "Bookbag", "price": 130})

    response = client.get("/items")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 3


def test_update_item(client):
    put_response = client.put("/items/3", json={"name": "Phone"})

    assert put_response.status_code == 200
    
    get_response = client.get("/items")
    get_response_data = get_response.get_json()

    assert get_response.status_code == 200

    assert get_response_data["3"]["name"] == "Phone"
    assert get_response_data["3"]["price"] == 130


def test_delete_item(client):
    delete_response = client.delete("/items/1")

    assert delete_response.status_code == 200
    
    get_response = client.get("/items")
    get_response_data = get_response.get_json()

    assert get_response.status_code == 200

    assert not "1" in get_response_data
