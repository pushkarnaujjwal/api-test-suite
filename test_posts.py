import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts_status_code():
    """API should return 200 OK"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

def test_get_all_posts_returns_list():
    """Response should be a list of 100 posts"""
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100

def test_get_single_post_status_code():
    """Fetching a valid post should return 200"""
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200

def test_get_single_post_has_required_fields():
    """Post object should contain id, title, body, userId"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

def test_get_single_post_correct_id():
    """Returned post id should match requested id"""
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["id"] == 1

def test_get_invalid_post_returns_404():
    """Requesting a non-existent post should return 404"""
    response = requests.get(f"{BASE_URL}/posts/9999")
    assert response.status_code == 404