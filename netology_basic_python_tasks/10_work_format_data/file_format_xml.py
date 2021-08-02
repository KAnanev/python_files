import xml.etree.ElementTree as ET

list_words = []
dict_words = {}
description = ''
tree = ET.parse('newsafr.xml')

root = tree.getroot()

description = root.findall('channel/item')

for i in description:
    list_words.append(i.find('description').text.lower())

description = ' '.join(list_words)
description_list = description.split(' ')

for item in description_list:
    if len(item) > 6:
        dict_words[item] = description_list.count(item)

list_words = sorted(dict_words.items(), key=lambda item: (-item[1], item[0]))

for i in range(10):
    print(f'{i + 1}. Слово {list_words[i][0]} используется в тексте {list_words[i][1]} раза')
