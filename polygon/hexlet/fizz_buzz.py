def fizz_buzz(num_begin, num_end):
    string_out = []
    for i in range(num_begin, num_end + 1):
        if i % 3 == 0 and i % 5 == 0:
            string_out.append('FizzBuzz')
        elif i % 3 == 0:
            string_out.append('Fizz')
        elif i % 5 == 0:
            string_out.append('Buzz')
        else:
            string_out.append(str(i))
    return ' '.join(string_out)


print(fizz_buzz(7, 7))
