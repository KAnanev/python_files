# Вариант 1


# def foo():
#     return 42
#
#
# def decor_function(old_function):
#     def new_function():
#         result = old_function()
#         result = {'status': 'succes', 'result': result}
#         return result
#     return new_function()
#
#
# foo = decor_function(foo)

# Вариант 2


# def decor_function(old_function):
#     def new_function():
#         result = old_function()
#         result = {'status': 'succes', 'result': result}
#         return result
#     return new_function()
#
#
# @decor_function
# def foo():
#     return 42
import requests
from pprint import pprint



def stability(old_function):
    def new_function(*args, **kwargs):
        try:
            description = old_function(*args, **kwargs)
            status = 'success'
        except Exception as er:
            status = 'error'
            description = er
        result = {'status': status,
                  'description': description,
                  'action': old_function.__name__}
        return result
    return new_function()


@stability
def get_habr(uri='/'):
    result = requests.post(f'http://habr.com{uri}')
    return result.text
pprint(get_habr)


# class Person:
#     poppulation = {}
#
#     def __int__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def say_hi():
#         print('Hi')
#
#     @classmethod
#     def was_borned(cls, name):
#         new_person = cls(name, 0)
#         cls.poppulation[name] = new_person
#         return cls(name, 0)
#
#
# misha = Person('Misha', 4)
#
# misha.say_hi()
