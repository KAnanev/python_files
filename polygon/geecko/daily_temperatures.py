# Имеется список дневных температур T. Для каждого дня во входных данных необходимо определить, сколько дней
# придется ждать более теплой температуры. Если в последующих днях нет более теплой температуры, количество дней
# будет равно 0.
#
# На входе:
#
# T - список дневных температур, значения температур от 30 до 100
# На выходе:  массив с количеством дней
#
# Пример:
#
#T = [73, 74, 75, 71, 69, 72, 76, 73]
# daysNumber( T ) --> [1, 1, 4, 2, 1, 1, 0, 0]
#
# Реализуйте функцию daily_temperatures
#
t = [73, 74, 75, 71, 69, 72, 76, 73]


def daily_temperatures(lst):
    list_count = []
    for start_index in range(len(lst)):
        count = 0
        for letter in range(start_index + 1, len(lst)):
            if lst[letter] > lst[start_index]:
                count += 1
                list_count.append(letter - start_index)
                break
        if count == 0:
            list_count.append(0)
    return list_count


def daily_temperatures_ver2(t):
    days = []
    for ind, temp in enumerate(t):
        temp_greater = [(i, val) for i, val in enumerate(t[ind+1:], ind+1) if val > temp]
        day = temp_greater[0][0]-ind if temp_greater else 0
        days.append(day)
    return days


print(daily_temperatures_ver2(t))


daily_temperatures(t)