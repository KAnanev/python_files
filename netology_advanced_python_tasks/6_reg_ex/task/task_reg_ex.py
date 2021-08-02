# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
pattern = re.compile(r'^(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])\s*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё])*\,*(\w+[А-яЁё]\w+[А-яЁё –]*\–*\s*)*\,*(\+*\d\s*\(*\d+\)*\-*\s*\d+\-*\d+\-*\d+\s*\(*\w*\.*\s*\d*\)*)*\,*(\w+\.*\w*\@\w+\.\w+)*')
pattern_tel = re.compile(r'\+*(\d)\s*\(*(\d\d\d)\)*\-*\s*(\d\d\d)\-*(\d\d)\-*(\d\d)\s*\(*(\w*\.*)\s*(\d*)\)*')

full_list_contacts = []
temp_list_contacts = []

for i in range(len(contacts_list)):
    if i == 0:
        temp_list_contacts.append(contacts_list[i])
        continue
    temp_string = ','.join(contacts_list[i])
    result = re.search(pattern, temp_string)
    temp_list_contacts.append(list(result.groups()))
    if temp_list_contacts[i][5] is None:
        continue
    else:
        temp_list_contacts[i][5] = pattern_tel.sub(r"+7(\2)\3-\4-\5 \6\7", temp_list_contacts[i][5])

for i in range(len(temp_list_contacts)):
    for j in range(len(temp_list_contacts)):
        if temp_list_contacts[i][0] == temp_list_contacts[j][0]:
            temp_list_contacts[i] = [x or y for x, y in zip(temp_list_contacts[i], temp_list_contacts[j])]
    if temp_list_contacts[i] not in full_list_contacts:
        full_list_contacts.append(temp_list_contacts[i])

print(full_list_contacts)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    data_writer = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    data_writer.writerows(full_list_contacts)
