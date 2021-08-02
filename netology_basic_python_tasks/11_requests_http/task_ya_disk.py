import os
import requests
from chardet import UniversalDetector

file_path = '/Users/ananevkonstantin/PycharmProjects/polygon/yandex'
file_name = 'DE-ru.txt'
full_file_path = '/Users/ananevkonstantin/PycharmProjects/polygon/yandex/DE-ru.txt'

GET_URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
TOKEN = ''
params = {'path': f'/{file_name}', 'overwrite': 'true'}
headers = {'Accept': 'application/json', 'Authorization': TOKEN}


def detect_encoding(file_path, file_name):
    """
    Определяем кодировку файла
    Нужно передать путь к файлу и указать название файла
    """
    detector = UniversalDetector()
    with open(os.path.join(file_path, file_name), 'rb') as file:
        for line in file.readlines():
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    return detector.result['encoding']


get_res = requests.get(GET_URL, headers=headers, params=params)
PUT_URL = get_res.json()['href']
files = {'file': open(full_file_path, 'r', encoding=detect_encoding(file_path, file_name))}
response = requests.put(PUT_URL, files=files)
print(response)
