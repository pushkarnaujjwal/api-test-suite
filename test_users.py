import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_users_status_code():
    """API should return 200 OK"""
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200

def test_get_all_users_returns_list():
    """Response should be a list of 10 users"""
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10

def test_get_single_user_status_code():
    """Fetching a valid user should return 200"""
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_get_single_user_has_required_fields():
    """User object should contain id, name, username, email"""
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "username" in data
    assert "email" in data

def test_get_single_user_email_format():
    """User email should contain @ symbol"""
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "@" in data["email"]

def test_get_invalid_user_returns_404():
    """Requesting a non-existent user should return 404"""
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404