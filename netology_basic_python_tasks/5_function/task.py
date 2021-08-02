# Я работаю секретарем и мне постоянно приходят различные документы. Я должен быть очень внимателен чтобы не потерять
# ни один документ. Каталог документов хранится в следующем виде:
#
#       documents = [
#         {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
#         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
#         {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
#       ]
# Перечень полок, на которых находятся документы хранится в следующем виде:
#
#       directories = {
#         '1': ['2207 876234', '11-2', '5455 028765'],
#         '2': ['10006', '5400 028765', '5455 002299'],
#         '3': []
#       }
# Задача №1
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
#
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит; l– list –
# команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"; s – shelf –
# команда, которая спросит номер документа и выведет номер полки, на которой он находится; a – add – команда,
# которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки,
# на котором он будет храниться. Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции
# должны иметь выразительное название, передающие её действие.

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def num_doc_people(num_doc):
    name = False
    for item in documents:
        if item["number"] == num_doc:
            name = item["name"]
    if name:
        print(name)
    else:
        print("Документ не найден")


def list_documents():
    for item in documents:
        print(f'{item["type"]} \"{item["number"]}\" \"{item["name"]}\"')


def number_shelf_doc(num_doc):
    number_shelf = False
    for key, value in directories.items():
        if value.count(num_doc):
            number_shelf = key
    if number_shelf:
        print(f"Документ под номером {num_doc} находится на полке {number_shelf}")
    else:
        print("Документ не найден")


def add_num_doc(num_doc, num_type, name_doc, num_shelf):
    documents.append({"type": num_type, "number": num_doc, "name": name_doc})
    if num_shelf in directories:
        directories[num_shelf].append(num_doc)
    else:
        directories.setdefault(num_shelf, [])
        directories[num_shelf].append(num_doc)


def del_doc(num_doc):
    for item in documents:
        if item["number"] == num_doc:
            documents.remove(item)
    for key, values in directories.items():
        if values.count(num_doc):
            values.remove(num_doc)


def main():
    while True:
        user_input = input("Введите команду: ")
        if user_input == 'p':
            num_doc = input("Введите номер документа для поиска владельца: ")
            num_doc_people(num_doc)
        elif user_input == 'l':
            print("Список всех документов:")
            list_documents()
        elif user_input == 's':
            num_doc = input("Введите номер документа для поиска по полкам: ")
            number_shelf_doc(num_doc)
        elif user_input == 'a':
            num_doc = input("Введите номер добавляемого документа: ")
            num_type = input("Введите тип документа: ")
            name_doc = input("Введите имя владельца: ")
            num_shelf = input("Введите номер полки: ")
            add_num_doc(num_doc, num_type, name_doc, num_shelf)
        elif user_input == 'd':
            num_doc = input("Введите номер удаляемого документа: ")
            del_doc(num_doc)
        elif user_input == 'q':
            break


main()

