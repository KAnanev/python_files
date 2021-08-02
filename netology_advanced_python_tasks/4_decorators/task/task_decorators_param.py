import os


def path_log(path):
    def log_func(old_func):
        def new_func(*args, **kwargs):
            from datetime import datetime
            call_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            result = old_func(*args, **kwargs)
            with open(f'{path}/file.log', 'a', encoding='utf-8') as file:
                file.write(f'Время вызова функции: {call_time}\n'
                           f'Имя функции: {old_func.__name__}\n'
                           f'Аргументы функции: {args}_{kwargs}\n'
                           f'Возвращаемое значение: {result}\n'
                           f'\n')
            return result

        return new_func

    return log_func


@path_log(os.getcwd())
def func(*args, **kwargs):
    return args, kwargs


func(3, 4)
