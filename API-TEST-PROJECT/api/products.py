import requests

def test_create_product():
    url = 'https://api.example.com/products'
    data = {'name': 'iPhone 14', 'price': 1200}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json()['name'] == 'iPhone 14'

# ... (다른 상품 관련 테스트)