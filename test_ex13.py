import json

import requests
import pytest

params = [
    ({
         "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"},
     {"platform": "Mobile", "browser": "No", "device": "Android"}),
    ({
         "User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"},
     {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}),
    ({"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"},
     {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}),
    ({
         "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'},
     {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}),
    ({
         "User-Agent": 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'},
     {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'})
]

list_with_wrong_user_agent = []


@pytest.mark.parametrize('user_agent, expected_text', params)
def test_check_user_agent(user_agent, expected_text):
    response = requests.get('https://playground.learnqa.ru/ajax/api/user_agent_check', headers=user_agent)
    response_obj = json.loads(response.text)

    for key in expected_text:
        try:
            assert expected_text[key] in response_obj[
                key], f'Expected value for key: ***{key}*** must be ***{expected_text[key]}***, but we have ***{response_obj[key]}***'
        except AssertionError:
            list_with_wrong_user_agent.append(
                response.text + " MUST BE " + expected_text[key] + " BUT WE HAVE " + response_obj[key])
    print(list_with_wrong_user_agent)

    #  Список User-agent с неправильными параметрами = [
    #  '{"user_agent":"Mozilla\\/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit\\/605.1.15 (KHTML, like Gecko) CriOS\\/91.0.4472.77 Mobile\\/15E148 Safari\\/604.1","platform":"Mobile","browser":"No","device":"iOS"}
    #  MUST BE Chrome BUT WE HAVE No',
    #
    #  '{"user_agent":"Mozilla\\/5.0 (compatible; Googlebot\\/2.1; +http:\\/\\/www.google.com\\/bot.html)","platform":"Unknown","browser":"Unknown","device":"Unknown"}
    #  MUST BE Googlebot BUT WE HAVE Unknown',
    #
    #  '{"user_agent":"Mozilla\\/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit\\/605.1.15 (KHTML, like Gecko) Version\\/13.0.3 Mobile\\/15E148 Safari\\/604.1","platform":"Mobile","browser":"No","device":"Unknown"}
    #  MUST BE iPhone BUT WE HAVE Unknown'
    #  ]
