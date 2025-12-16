# tests/test_smoke.py
import requests

def test_root_404():
    r = requests.get("http://localhost:8080/")
    assert r.status_code in (200, 404)  # expect 404 or 200 depending on app
