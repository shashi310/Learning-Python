# test_app.py

import json
import pytest
from app import app

# Create a testing client
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

# Define a helper function to send JSON requests
def send_json_request(client, method, url, data):
    return client.open(
        url,
        method=method,
        data=json.dumps(data),
        content_type='application/json'
    )

# Example test using the client
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
