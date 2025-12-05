import os
import sys

# фикс для импорта app.py при запуске pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from app import app

def test_items_get():
    client = app.test_client()
    response = client.get('/items')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, World!"


def test_api_get():
    client = app.test_client()
    response = client.get('/api')

    assert response.status_code == 200
    assert response.get_json() == {'status': 'test'}


def test_api_post():
    client = app.test_client()
    payload = {"name": "Dima"}

    response = client.post('/api', json=payload)

    assert response.status_code == 200
    assert response.get_json() == {'status': 'OK!'}
