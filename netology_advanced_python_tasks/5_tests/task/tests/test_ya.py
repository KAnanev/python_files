import unittest
import requests
import api


def translation_ya(ru_text):
    API_KEY = api.api
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': API_KEY,
        'text': ru_text,
        'lang': 'ru'
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return json_


class TestTranslYa(unittest.TestCase):
    def test_200_translation_ya(self):
        res_ya = translation_ya('Hi')
        self.assertEqual(res_ya['code'], 200)

    def test_401_translation_ya(self):
        res_ya = translation_ya('Hi')
        self.assertNotEqual(res_ya['code'], 401)

    def test_402_translation_ya(self):
        res_ya = translation_ya('Hi')
        self.assertNotEqual(res_ya['code'], 402)
