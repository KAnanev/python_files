# def multuply_fabric(param):
#
#     def multiply(x):
#         return param * x
#
#     return multiply
#
#
# foo = multuply_fabric(3)
# print(foo(2))

# def foo(*args,**kwargs):
#     print('args', args)
#     print('kwargs', kwargs)
#
# foo(1, 2, 3, v = 5, c = 7)
import random

import requests


# def make_requests(url, n, *args, **kwargs):
#     for _ in range(n):
#         try:
#             response = requests.get(url, n, *args, **kwargs)
#             print(response.text)
#         except Exception as er:
#             print(er)
#
# make_requests('http://yandex.ru', 10)


# def make_requests(x={}):
#     x[random.randrange(1, 100)] = 1
#     print(x)
#
# make_requests()
# make_requests()
# make_requests()
# make_requests()

# x_list = [(1, 'a'), (2, 'c'), (0, 'b')]
#
# x_map = list(map(lambda x: x[1], x_list))
#
# print(x_map)


# def multi_fabric(param):
#
#     return lambda x: x * param
#
# print((lambda x, y: x * y)(4, 2))

# session = requests.Session()
#
#
# def fabric(singletone):
#     singletone = singletone
#
#     def _get_singltone(*args, **kwargs):
#         nonlocal singletone
#         return singletone
#
#     return _get_singltone
#
#
# get_singletone = fabric(session)

def foo(a: int) -> str:
    return str




