import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests



@allure.epic('Creation cases')
class TestPublisherCreate(BaseCase):
    def setup(self):
        self.headers = {'token': 'chooQu3Yech4phoo1eip', 'accept': 'application/json'}

    @allure.title('AP-1. Создание паблишера')
    @allure.testcase('https://app.qase.io/case/AP-1', 'Создание паблишера')
    @allure.description('Тест на успешное создание паблишера')
    def test_create_publisher_successfully(self):
        data = self.prepare_data_for_publisher()

        response = MyRequests.post('/publishers', data=data, headers=self.headers)

        expected_fields = ['id', 'uid', 'name', 'email']
        Assertions.assert_code_status(response, 201)
        Assertions.assert_json_has_keys(response, expected_fields)

    @allure.description('Тест на неудачное создание паблишера с уже используемым email')
    def test_create_publisher_with_existing_email(self):
        email = 'testemail@mail.net'
        data = self.prepare_data_for_publisher(email=email)

        response = MyRequests.post('/publishers', data=data, headers=self.headers)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode(
            'utf-8') == '{"error":"email should be unique"}', f'Unexpected response content {response.content}'
