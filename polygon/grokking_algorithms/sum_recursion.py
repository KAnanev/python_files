def func_sum(lst):
    """Рекурсивно сумма всех элементов"""
    if not lst:
        return 0
    return lst[0] + func_sum(lst[1:])


list_num = [1, 2, 10, 4, 5, 6]
# print(func_sum(list_num))


def count(lst):
    """Рекурсивно длина списка"""
    if not lst:
        return 0
    return 1 + count(lst[1:])

# print(count(list_num))


def func_max(lst):
    """Рекурсивно наибольшее число"""
    if len(lst) == 2:
        return lst[0] if lst[0] > lst[1] else lst[1]
    sub_max = func_max(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max


print(func_max(list_num))
