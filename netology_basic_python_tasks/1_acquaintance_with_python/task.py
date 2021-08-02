"""
Финансовое планирование.

Приложение получает данные о заработной плате и тратах,
выводит в консоль затраты и накопления.
"""

salary = int(input('Введите заработанную плату в месяц: '))
percent_mortgage = int(input('Введите сколько процентов уходит на ипотеку: '))
percent_residence = int(input('Введите сколько процентов уходит на жизнь: '))
quantity_prize = int(input('Введите количество премий за год: '))

month_residence = salary * percent_residence / 100
month_mortgage = salary * percent_mortgage / 100
rest_money = salary - month_residence - month_mortgage

total_mortgage = 12 * month_mortgage

saving = 12 * rest_money + quantity_prize * (salary / 2)

print(
    f'Вывод:\n'
    f'На ипотеку было потрачено: {int(total_mortgage)} рублей\n'
    f'Было накоплено: {int(saving)} рублей')
