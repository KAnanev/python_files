from basic_python import data


class Secretary:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def num_doc_people(self, number):
        name = False
        for item in data.documents:
            if item["number"] == number:
                name = item["name"]
        if name:
            print(name)
        else:
            print("Документ не найден")

    def list_documents(self):
        for item in data.documents:
            print(f'{item["type"]} \"{item["number"]}\" \"{item["name"]}\"')

    def list_names(self):
        for item in data.documents:
            print(f'{item["name"]}')

    def number_shelf_doc(self, number):
        number_shelf = False
        for key, value in data.directories.items():
            if value.count(number):
                number_shelf = key
        if number_shelf:
            print(f"Документ под номером {number} находится на полке {number_shelf}")
        else:
            print("Документ не найден")

    def add_num_doc(self, number, num_type, name_doc, num_shelf):
        data.documents.append({"type": num_type, "number": number, "name": name_doc})
        if num_shelf in data.directories:
            data.directories[num_shelf].append(number)
        else:
            data.directories.setdefault(num_shelf, [])
            data.directories[num_shelf].append(number)

    def del_doc(self, number):
        for item in data.documents:
            if item["number"] == number:
                data.documents.remove(item)
        for key, values in data.directories.items():
            if values.count(number):
                values.remove(number)


def main():
    secretary = Secretary('Ivan', '1234')
    print(f'Доброе утро, {secretary.name}')
    while True:
        user_input = input("Введите команду: ")
        if user_input == 'p':
            num_doc = input("Введите номер документа для поиска владельца: ")
            secretary.num_doc_people(num_doc)
        elif user_input == 'l':
            print("Список всех документов:")
            secretary.list_documents()
        elif user_input == 's':
            num_doc = input("Введите номер документа для поиска по полкам: ")
            secretary.number_shelf_doc(num_doc)
        elif user_input == 'a':
            num_doc = input("Введите номер добавляемого документа: ")
            num_type = input("Введите тип документа: ")
            name_doc = input("Введите имя владельца: ")
            num_shelf = input("Введите номер полки: ")
            secretary.add_num_doc(num_doc, num_type, name_doc, num_shelf)
        elif user_input == 'd':
            num_doc = input("Введите номер удаляемого документа: ")
            secretary.del_doc(num_doc)
        elif user_input == 'n':
            try:
                (secretary.list_names())
            except KeyError:
                print('В документе отсутствует имя')
        elif user_input == 'q':
            break


main()
