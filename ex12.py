import requests


def test_check_header_value():
    response = requests.get('https://playground.learnqa.ru/api/homework_header')
    assert response.headers['x-secret-homework-header'] == 'Some secret value', 'headers value wrong'


test_check_header_value()
