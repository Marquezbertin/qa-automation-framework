import pytest
import requests

@pytest.mark.parametrize("endpoint, expected_status", [
    ("https://jsonplaceholder.typicode.com/posts/1", 200),
    ("https://jsonplaceholder.typicode.com/posts/9999", 404),
])
def test_api_multiple_endpoints(endpoint, expected_status):
    response = requests.get(endpoint)
    assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

def test_api_with_timeout():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
    assert response.status_code == 200, "Request timed out or failed"
