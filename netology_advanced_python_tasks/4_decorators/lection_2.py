import requests
import json
import time


def args_to_string(*args, **kwargs):

    return f'{json.dumps(args)}_{json.dumps(kwargs)}'


def parametrizesed(ttl):
    def cache_decor(old_function):
        cache = dict()

        def new_function(*args, **kwargs):
            start = time.time()
            stringed_args = args_to_string(*args, **kwargs)
            try:
                result = cache[stringed_args]['result']
                current_time = time.time()
                print('cache live', current_time - cache[stringed_args]['time'])
                if current_time - cache[stringed_args]['time'] > ttl:
                    del cache[stringed_args]
            except KeyError:
                result = old_function(*args, **kwargs)
                cache[stringed_args] = {
                    'result': result,
                    'time': time.time()
                }

            print(time.time() - start)
            return result
        return new_function
    return cache_decor

@parametrizesed(3)
def get_habr(uri='/'):
    result = requests.get(f'http://habr.com{uri}')
    return result.text

get_habr()