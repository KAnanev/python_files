import datetime


class DateTime:

    def __init__(self, path):
        self.enter_time = datetime.datetime.now()
        print(f'Начало скрипта: {self.enter_time}')
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        time_end = datetime.datetime.now()
        print(f'Конец скрипта: {time_end}')
        print(f'Время выполнение скрипта: {time_end - self.enter_time}')
        self.file.close()

    def write_fib(self, message):
        self.file.write(f' {message}\n')


if __name__ == '__main__':
    with DateTime('testfile') as file:
        def fibonacci(n):
            if n in (1, 2):
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)
        file.write_fib(fibonacci(10))
