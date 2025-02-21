import requests
import pytest

# Base URL for the API
url = "http://localhost:5000"

def test_get_todos():
    response = requests.get(url + "/todos")
    assert response.status_code == 200

# def test_create_todo():
#     response = requests.post(url + "/todos", json={"title": "first task"})
#     assert response.status_code == 201

# test connection
def test_connection():
    response = requests.get(url + "/")
    assert response.status_code == 200