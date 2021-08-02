def function_decorator(func):
    def wrapper(txt):
        count = 0
        while count < 3:
            result = func(txt)
            count += 1
        print(result[0])
    return wrapper
