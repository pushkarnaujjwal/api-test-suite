# api-test-suite
# API Test Suite – JSONPlaceholder

Automated API test suite built with Python and Pytest, validating REST API endpoints for posts and users.

## What It Tests

**Posts API (`/posts`)**
- Returns HTTP 200 status code
- Returns a list of 100 posts
- Single post contains required fields (id, title, body, userId)
- Returned post ID matches requested ID
- Invalid post ID returns 404

**Users API (`/users`)**
- Returns HTTP 200 status code
- Returns a list of 10 users
- Single user contains required fields (id, name, username, email)
- User email contains valid format with @ symbol
- Invalid user ID returns 404

## Tech Stack
- Python 3.14
- Pytest
- Requests

## How to Run

Install dependencies:
pip install pytest requests

Run all tests:
pytest -v
