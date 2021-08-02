# Цель данного упражнения — функция updated().
# Эта функция должна принимать словарь в качестве
# единственного позиционного аргумента (обязательного)
# и произвольное кол-во именованных аргументов.
# Возвращать же функция должна новую версию словаря,
# в котором ключи, соответствующие именованным аргументам,
# должны иметь сопутствующие значения (см.примеры).
#
# >>> d = {'a': 1, 'b': False}
# >>> updated(d, a=2, b=True, c=None)
# {'a': 2, 'b': True, 'c': None}
# >>> d
# {'a': 1, 'b': False}
# >>> updated(d) == d
# True
# >>> updated(d) is d
# False


def updated(*args, **kwargs):
    result = args[0].copy()
    result.update(kwargs)
    return result


def test_updated():
    old = {'a': 1, 'b': None, 2: 4}
    copy_of_old = old.copy()
    assert updated(old) is not old
    assert updated(old, a=2) == {'a': 2, 'b': None, 2: 4}
    assert old == copy_of_old, "Old dict should stay unchanged!"
    assert updated({}, foo='bar', bar=42) == {'foo': 'bar', 'bar': 42}


test_updated()
