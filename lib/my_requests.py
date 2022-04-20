import requests
import allure
from lib.logger import Logger


class MyRequests():
    @staticmethod
    def post(url: str, data: dict = None, headers: dict = None):
        with allure.step(f'POST request to URL "{url}"'):
            return MyRequests._send(url, data, headers, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None):
        with allure.step(f'GET request to URL "{url}"'):
            return MyRequests._send(url, data, headers, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None):
        with allure.step(f'PUT request to URL "{url}"'):
            return MyRequests._send(url, data, headers, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None):
        with allure.step(f'DELETE request to URL "{url}"'):
            return MyRequests._send(url, data, headers, 'DELETE')


    @staticmethod
    def _send(url: str, data: dict, headers: dict, method: str):

        url = f'https://api-adserver.k-stage.sbmt.io/v1{url}'

        if headers is None:
            headers = {}

        Logger.add_request(url, data, headers, method)

        if method == 'GET':
            response = requests.get(url, params=data, headers=headers)
        elif method == 'POST':
            response = requests.post(url, data=data, headers=headers)
        elif method == 'PUT':
            response = requests.put(url, data=data, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, data=data, headers=headers)
        else:
            raise Exception(f'Bad HTTP method received')

        Logger.add_response(response)

        return response
