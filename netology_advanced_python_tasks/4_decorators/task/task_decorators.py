def decor_func(old_func):
    def new_func(*args, **kwargs):
        import json
        from datetime import datetime
        call_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        result = old_func(*args, **kwargs)
        with open('file.log', 'a', encoding='utf-8') as file:
            file.write(f'Время вызова функции: {call_time}\n'
                       f'Имя функции: {old_func.__name__}\n'
                       f'Аргументы функции: {json.dumps(args)}_{json.dumps(kwargs)}\n'
                       f'Возвращаемое значение: {result}\n'
                       f'\n')
        return result
    return new_func


@decor_func
def func(*args, **kwargs):
    return args, kwargs


func(3, 4)






