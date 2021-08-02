def is_power_of_three(number):
    counter = 1
    while counter < number:
        counter *= 3
    return counter == number

print(is_power_of_three(18))