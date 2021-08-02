import requests
import os

API_KEY = 'api'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

name_file = 'FR'
path_file = os.path.abspath(f'{name_file}.txt')
source_lang = name_file.lower()
target_lang = 'ru'
path_file_tr = f'{path_file[:-4]}-{target_lang}.txt'


def translate_it(file_in, file_out, lang_in, lang_out='ru'):
    with open(file_in) as file:
        text = file.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': f'{lang_in}-{lang_out}'
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(file_out, 'w') as file:
        file.write(''.join(json_['text']))
    return print('Перевод выполнен')


if __name__ == '__main__':
    translate_it(path_file, path_file_tr, source_lang, target_lang)
