import requests

response = requests.get('https://playground.learnqa.ru/api/long_redirect')
print('Кол-во редиректов: ' + str(len(response.history)))
print('Конечный url: ' + response.url)