def hamming_weight(number):
    weight = 0
    digits = bin(number)[2:]

    for num in digits:
        weight += int(num)

    return weight


print(hamming_weight(34))
