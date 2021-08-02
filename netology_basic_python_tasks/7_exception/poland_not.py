# Нужно реализовать Польскую нотацию для двух положительных чисел. Реализовать нужно будет следующие операции:
#
# Сложение
# Вычитание
# Умножение
# Деление
# Например, пользователь вводит: + 2 2 Ответ должен быть: 4

try:
    expression = input("Введите выражение в польской нотации: ")
    list_exp = list(expression.split())
    assert list_exp[0] in ['+', '-', '*', '/']

    num_one = int(list_exp[1])
    num_two = int(list_exp[2])
    dict_operator = {'+': num_one.__add__(num_two), '-': num_one.__sub__(num_two), '*': num_one.__mul__(num_two),
                     '/': num_one.__truediv__(num_two)}

    for key, value in dict_operator.items():
        if key == list_exp[0]:
            print(value)
except AssertionError:
    print('Неправильно введен арифмитический оператор!!!')
except ZeroDivisionError:
    print('Ошибка деления на ноль!!!')
except ValueError:
    print('Выражения должны содержать число!!!')
except IndexError:
    print('Аргументо выражения должно быть два!!!')

