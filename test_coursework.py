from requests.auth import HTTPBasicAuth 
import pytest
import requests

basic_auth = HTTPBasicAuth('1VQDHXQ8EF73QTHESPT7UHU9AJQPLXXL', '')

def test_get_check_search():
    response = requests.get("http://164.92.218.36:8080/search?controller=search&s=clothes", auth=basic_auth)
    print(response)
    assert response.text.find("clothes") >= 0

def test_get_check_currencies():
    response = requests.get("http://164.92.218.36:8080/api/currencies", auth=basic_auth)
    print(response)
    assert response.status_code == 200

def test_get_check_exit():
    response = requests.get("http://164.92.218.36:8080/?mylogout=", auth=basic_auth)
    print(response)
    assert response.status_code == 200

def test_get_request():
    resp = requests.get('http://164.92.218.36:8080/9-art', auth=basic_auth)
    assert resp.status_code == 200

def test_get_request_again():
    resp = requests.get('http://164.92.218.36:8080/6-accessories', auth=basic_auth)
    assert resp.status_code == 200

def test_get_request_contacts():
    resp = requests.get('http://164.92.218.36:8080/api/contacts', auth=basic_auth)
    assert resp.status_code == 200

def test_authorization():
    url = 'http://164.92.218.36:8080/login?back=my-account'
    data = {'username': 'Sara', 'password': 'Kapibara99'}
    response = requests.post(url, json=data)
    assert response.status_code == 200

def test_post_create_user():
    data = {
        'name': "John Doe",
        "email": "johndoe@example.com",
        "gender": "Male",
        "password": "1234567",
        "birthday": "2001 - 01 - 31"
    }
    response = requests.post("http://164.92.218.36:8080/login?create_account=1", data)
    assert response.status_code == 200

def test_post_check_auth():
    data = {'email': "user@gmail.com", 'password': "1234567","submitLogin": 1}
    response = requests.post("http://164.92.218.36:8080/login?back=my-account", data )
    print(response)
    assert response.status_code == 200

def test_post_check_communication_auth():
    data = {'from': "user@gmail.com", 'message': "help", 'fileUpload': "(binary)"}
    response = requests.post("http://164.92.218.36:8080/contact-us", data)
    print(response)
    assert response.status_code == 200

def test_post_check_failed_auth():
    data = {'email': "user@gmail.com", 'password': "123456","submitLogin": 1}
    response = requests.post("http://164.92.218.36:8080/login?back=my-account", data)
    print(response)
    assert response.text.find("Помилка авторизації") >= 0

def test_post_orders():
    url = "http://164.92.218.36:8080/api/orders"
    data = {
    'order_id': "WCQNUIQGV",
    'data': "2023-04-07",
    'sum': "14,28"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 401


def test_put_change_password():
    response = requests.put("http://164.92.218.36:8080/login?create_account=1", data ={
        'firstname': "user",
        'lastname': "name",
        "email": "user_name@gmail.com",
        "password": "1234567",
        "birthday": "2001 - 01 - 31"
    })
    print(response)
    assert response.status_code == 200

def test_put_invalid_birth():
    data = {
        'firstname': "user",
        'lastname': "name",
        'email': "user_name@gmail.com",
        'password': "1234567",
        'birthday': "0000-00-00"
    }
    response = requests.put("http://164.92.218.36:8080/login?create_account=1", data=data)
    print(response)
    assert response.text.find("Не вдалося оновити інформацію, будь ласка перевірте ваші дані.") != 200

def test_put_currencies():
    url = "http://164.92.218.36:8080/api/currencies"
    data = {
        'currency_id': "1",
        'currency_name': "yevro",
        "exchange_rate": "0.027072"
    }
    response = requests.put(url, data=data)
    if response.status_code == 200:
        print("Запит PUT успішно виконано.")
    else:
        print("Сталася помилка при виконанні запиту PUT.")

def test_delete_person():
        response = requests.delete("http://164.92.218.36:8080/login?create_account=1", data={
            'firstname': "user",
            'lastname': "name",
            "email": "user_name@gmail.com",
            "password": "1234567",
            "birthday": "2001 - 01 - 31"
        })
        if response.status_code == 204:
            print("Person Deleted")
        else:
            print(response.status_code)

def test_delete_orders():
    url = "http://164.92.218.36:8080/api/orders"
    response = requests.delete(url)
    if response.status_code == 401:
        print("Запит DELETE успішно виконано.")
    else:
        print("Сталася помилка при виконанні запиту DELETE.")
        print("Статус код:", response.status_code)
    if response.text:
        print("Текст відповіді:", response.text)

def test_delete_currencies():
    url = "http://164.92.218.36:8080/api/currencies"
    response = requests.delete(url)
    if response.status_code == 200:
        print("Запит DELETE успішно виконано.")
    else:
        print("Сталася помилка при виконанні запиту DELETE.")
        print("Статус код:", response.status_code)
    if response.text:
        print("Текст відповіді:", response.text)
