import requests

def test_create_user():
    url = 'https://reqres.in/api/users'
    data = {'name': 'yunjinyoung', 'email': 'acejinyoung@gmail.com'}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    assert response.json()['id'] is not None
    print("\n")
    print(response.json())

def test_get_user():
    url = 'https://reqres.in/api/users/2'
    data = {}
    response = requests.get(url, json=data)
    assert response.status_code == 200
    response.json()["data"]["id"] is not None
    print("\n")
    print(response.json())