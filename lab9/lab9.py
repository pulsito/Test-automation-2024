import requests


def test_get_single_user():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    print(response.json())
    print(response.headers['Content-Type'])
    # Перевірка статусу коду
    assert response.status_code == 200
    # Перевірка формату відповіді
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    data = response.json()['data']
    assert 'id' in data
    assert 'first_name' in data
    assert 'last_name' in data


def test_create():
    url = "https://reqres.in/api/users"
    data = {"username": "Valentin", "job": "boss"}
    response = requests.post(url, data)
    # Перевірка статусу коду
    assert response.status_code == 201
    # Перевірка формату відповіді
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    response = response.json()
    # Перевірка коректного вмісту даних
    assert response['username'] == data['username']
    assert response['job'] == data['job']


def test_update():
    url = "https://reqres.in/api/users/3"
    data = {"username": "Petro", "job": "waiter"}
    response = requests.patch(url, data)
    # Перевірка статусу коду
    assert response.status_code == 200
    # Перевірка формату відповіді
    assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    response = response.json()
    # Перевірка коректного вмісту даних
    assert response['username'] == data['username']
    assert response['job'] == data['job']


def test_delete():
    url = "https://reqres.in/api/users/3"
    response = requests.delete(url)
    # Перевірка статусу коду
    assert response.status_code == 204
