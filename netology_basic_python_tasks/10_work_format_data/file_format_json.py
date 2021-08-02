import json

with open('newsafr.json', encoding='utf-8') as file:
    json_data = json.load(file)


list_words = []
dict_words = {}
description = ''
for i in json_data['rss']['channel']['items']:
    list_words.append(i['description'].lower())

description = ' '.join(list_words)
description_list = description.split(' ')

for item in description_list:
    if len(item) > 6:
        dict_words[item] = description_list.count(item)

list_words = sorted(dict_words.items(), key=lambda item: (-item[1], item[0]))

for i in range(10):
    print(f'{i + 1}. Слово {list_words[i][0]} используется в тексте {list_words[i][1]} раза')

