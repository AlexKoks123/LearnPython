import requests

METHODS = ['GET', 'POST', 'PUT', 'DELETE']


def request_with_base_methods(method=None, url='https://playground.learnqa.ru/ajax/api/compare_query_type',
                              params=None, data=None):
    if method is not None:
        if method.upper() == 'GET':
            response = requests.get(url, params=params)
            print(response.text)
        elif method.upper() == 'POST':
            response = requests.post(url, data=data)
            print(response.text)
        elif method.upper() == 'PUT':
            response = requests.put(url, data=data)
            print(response.text)
        elif method.upper() == 'DELETE':
            response = requests.delete(url, data=data)
            print(response.text)
        elif method not in METHODS:
            print('Please, use one of this methods: ' + str(METHODS))
    else:
        print('You must use the method in this function')


for item in METHODS:
    request_with_base_methods(item)

