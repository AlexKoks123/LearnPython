import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic('Get cases')
class TestPublisherGet(BaseCase):
    def setup(self):
        self.headers = {'token': 'chooQu3Yech4phoo1eip', 'accept': 'application/json'}

    @allure.testcase('https://app.qase.io/case/AP-8', 'Получение списка паблишеров')
    @allure.description('Тест на получение списка всех паблишеров')
    def test_get_publishers(self):
        response = MyRequests.get('/publishers', headers=self.headers)

        expected_fields = ['totalPages', 'totalCount', 'data']
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys(response, expected_fields)
