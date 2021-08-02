from decorators.decor import function_decorator


@function_decorator
def function_hello(txt):
    print(txt)
    return 1, 2


def main():
    function_hello('Hell')


if __name__ == '__main__':
    main()
