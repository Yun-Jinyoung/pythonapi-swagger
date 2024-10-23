import pytest

@pytest.fixture
def base_url():
    return 'https://api.example.com'

@pytest.fixture
def headers():
    return {'Authorization': 'Bearer your_token'}