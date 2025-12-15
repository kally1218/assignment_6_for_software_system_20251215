import requests

def test_create_todo():
    response = requests.post("http://localhost:5000/todos", json={"title": "task1"})
    assert response.status_code == 201

def test_get_todos():
    response = requests.get("http://localhost:5000/todos")
    assert isinstance(response.json(), list)
