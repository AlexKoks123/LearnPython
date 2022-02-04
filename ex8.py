import requests
import time
import json


response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
response_obj = json.loads(response.text)
token = response_obj['token']
seconds = response_obj['seconds']


def ex8(token=None, seconds=None):
    # Первый запрос
    first_response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
    payload = {'token': None}
    # Парсинг данных для дальнейшего использования
    response_obj = json.loads(first_response.text)
    token = response_obj['token']
    seconds = response_obj['seconds']
    # Заполнение токена
    payload['token'] = token
    # Второй запрос
    second_response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
    second_response_obj = json.loads(second_response.text)
    status = second_response_obj['status']
    # Проверка статуса
    if status == 'Job is NOT ready':
        # Ожидание, повторный запрос и проверка статуса и запрос результата
        time.sleep(seconds)
        last_response = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params=payload)
        last_response_obj = json.loads(last_response.text)
        status = last_response_obj['status']
        if status == 'Job is ready':
            print(last_response_obj['result'])


ex8()