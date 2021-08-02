def binary_sum(num_one, num_two):
    output = int(num_one, base=2) + int(num_two, base=2)
    print(str(format(output, 'b')))



binary_sum('1000', '10')
binary_sum('1010', '101')
binary_sum('1', '1')
binary_sum('1111', '1111')