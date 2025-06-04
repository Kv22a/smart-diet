import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_recommend_endpoint():
    resp = client.post("/recommend", json={
        "age": 25,
        "bmi": 22.0,
        "conditions": []
    })
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
    assert len(resp.json()) == 5
