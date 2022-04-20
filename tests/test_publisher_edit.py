import allure
import json
from datetime import datetime

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


@allure.epic('Edition cases')
class TestPublisherEdit(BaseCase):
    def setup(self):
        self.headers = {'token': 'chooQu3Yech4phoo1eip', 'accept': 'application/json'}

    @allure.title('AP-10. Изменение паблишера')
    @allure.testcase('https://app.qase.io/case/AP-10', 'Изменение паблишера')
    @allure.description('Тест на изменение только что созданного паблишера')
    def test_edit_just_created_publisher(self):
        # CREATE PUBLISHER
        create_data = self.prepare_data_for_publisher()

        response1 = MyRequests.post('/publishers', data=create_data, headers=self.headers)

        Assertions.assert_code_status(response1, 201)

        # EDIT PUBLISHER
        publisher_id = self.get_json_value(response1, 'id')
        new_name = 'Changed Name'
        random_part = datetime.now().strftime('%m%d%Y%H%M%S')
        new_email = f'{random_part}@gmail.com'
        new_password = 'changedPassword'
        changed_data = json.dumps({'email': new_email, 'name': new_name, 'password': new_password})

        response2 = MyRequests.put(f'/publishers/{publisher_id}', data=changed_data, headers=self.headers)

        Assertions.assert_code_status(response2, 200)

        # GET EDITED PUBLISHER
        response3 = MyRequests.get(f'/publishers/{publisher_id}', headers=self.headers)

        Assertions.assert_json_value_by_name(
            response3,
            'name',
            new_name,
            'Wrong name of the user after edit'
        )
        Assertions.assert_json_value_by_name(
            response3,
            'email',
            new_email,
            'Wrong email of the user after edit'
        )
