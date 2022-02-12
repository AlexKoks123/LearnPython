import requests


def test_check_cookie_value():
    response = requests.get('https://playground.learnqa.ru/api/homework_cookie')
    assert response.cookies['HomeWork'] == 'hw_value', 'cookies wrong'


test_check_cookie_value()
