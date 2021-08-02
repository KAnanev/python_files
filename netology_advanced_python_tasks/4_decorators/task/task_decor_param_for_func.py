import os


def path_log(path):
    def log_func(old_func):
        def new_func(*args, **kwargs):
            from datetime import datetime
            call_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            result = old_func(*args, **kwargs)
            if result is None:
                result = 'Функция ничего не возвращает'
            with open(f'{path}/file.log', 'a', encoding='utf-8') as file:
                try:
                    file.write(f'Время вызова функции: {call_time}\n'
                               f'Имя функции: {old_func.__name__}\n'
                               f'Аргументы функции: {args}_{kwargs}\n'
                               f'Возвращаемое значение: {result}\n'
                               f'\n')
                except Exception as er:
                    file.write(f'Время вызова функции: {call_time}\n'
                               f'Имя функции: {old_func.__name__}\n'
                               f'Аргументы функции: {args}_{kwargs}\n'
                               f'Возвращаемая ошибка: {er}\n'
                               f'\n')
            return result

        return new_func

    return log_func

class Contact:
    def __init__(self, name, surname, number_phone, *args, favorite_contact=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number_phone = number_phone
        self.favorite_contact = favorite_contact

        if not self.favorite_contact:
            self.favorite_contact = 'нет'
        else:
            self.favorite_contact = 'да'

        self.info = ''
        for item in args:
            self.info += f'{"":5}{item}\n'
        for key, value in kwargs.items():
            self.info = self.info + f'{"":5}{key} : {value}\n'

    def __str__(self):
        str_print = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Телефон: {self.number_phone}\n' \
                    f'В избранных: {self.favorite_contact}\n' \
                    f'Дополнительная информация:\n' \
                    f'{self.info}'
        return str_print


class PhoneBook:

    def __init__(self, name):
        self.name = name
        self.data = []

    def add_contact(self, contact):
        self.data.append(contact)

    def get_contact(self):
        for item in self.data:
            print(item)

    def del_contact(self, number_phone):
        for item in self.data:
            if number_phone == item.number_phone:
                self.data.remove(item)

    def get_favorite_contact(self):
        for item in self.data:
            if item.favorite_contact == 'да':
                print(item.number_phone)

    @path_log(os.getcwd())
    def get_search_contact(self, name, surname):
        for item in self.data:
            if name == item.name and surname == item.surname:
                print(item)


if __name__ == '__main__':
    john = Contact('John', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    peter = Contact('Peter', 'Wills', '+71676767809', favorite_contact=True, telegram='@peter', email='peter@wills.com')
    mary = Contact('Mary', 'Dick', '+79844489944', favorite_contact=True, telegram='@mary', email='mary@dick.com')

    book = PhoneBook('My book')
    book.add_contact(john)
    book.add_contact(peter)
    book.add_contact(mary)
    # book.get_contact()
    # book.del_contact('+71676767809')
    # book.get_contact()
    # book.get_favorite_contact()
    book.get_search_contact('Peter', 'Wills')
