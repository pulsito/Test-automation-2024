import requests
import allure

@allure.title("Test API/SINGLE USER")
@allure.description("Тестування GET-запиту на інформацію про користувача")
def test_get_single_user():
    with allure.step("Отримання URL-адреси та надсилання GET-запиту"):
        url = "https://reqres.in/api/users/2"
        response = requests.get(url)
    with allure.step("Перевірка JSON-відповіді та заголовків"):
        print(response.json())
        print(response.headers['Content-Type'])
    with allure.step("Перевірка статус-коду"):
        assert response.status_code == 200
    with allure.step("Перевірка формату відповіді"):
        assert response.headers['Content-Type'] == "application/json; charset=utf-8"
    with allure.step("Перевірка даних користувача"):
        data = response.json()['data']
        assert 'id' in data
        assert 'first_name' in data
        assert 'last_name' in data

@allure.title("Test API/CREATE")
@allure.description("Тестування POST-запиту для створення нового користувача")
def test_create():
    with allure.step("Надсилання POST-запиту для створення нового користувача"):
        url = "https://reqres.in/api/users"
        data = {"username": "Valentin", "job": "boss"}
        response = requests.post(url, data)
    with allure.step("Перевірка статус-коду та формату відповіді"):
        assert response.status_code == 201
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    with allure.step("Перевірка даних нового користувача"):
        response = response.json()
        assert response['username'] == data['username']
        assert response['job'] == data['job']

@allure.title("Test API/UPDATE")
@allure.description("Тестування PATCH-запиту для оновлення інформації про користувача")
def test_update():
    with allure.step("Надсилання PATCH-запиту для оновлення інформації про користувача"):
        url = "https://reqres.in/api/users/3"
        data = {"username": "Petro", "job": "waiter"}
        response = requests.patch(url, data)
    with allure.step("Перевірка статус-коду та формату відповіді"):
        assert response.status_code == 200
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    with allure.step("Перевірка оновлених даних користувача"):
        response = response.json()
        assert response['username'] == data['username']
        assert response['job'] == data['job']

@allure.title("Test API/UPDATE")
@allure.description("Тестування DELETE-запиту для видалення користувача")
def test_delete():
    with allure.step("Надсилання DELETE-запиту для видалення користувача"):
        url = "https://reqres.in/api/users/3"
        response = requests.delete(url)
    with allure.step("Перевірка статус-коду"):
        assert response.status_code == 204