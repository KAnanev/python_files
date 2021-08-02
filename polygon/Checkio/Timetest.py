import timeit

code_to_test = """
from collections import defaultdict


def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result


d = collect_indexes("hello")

d['h']
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)
