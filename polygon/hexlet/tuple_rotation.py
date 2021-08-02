triple = ('A', 'B', 'C')


def rotate_left(tpl):
    """Add function"""
    tpl = list(tpl)
    tpl[0], tpl[1], tpl[2] = tpl[1], tpl[2], tpl[0]
    print(tuple(tpl))


def rotate_right(tpl):
    """Add function"""
    tpl = list(tpl)
    tpl[0], tpl[1], tpl[2] = tpl[2], tpl[0], tpl[1]
    print(tuple(tpl))


# def rotate_left(triple):
#     elem1, elem2, elem3 = triple
#     return (elem2, elem3, elem1)
#
#
# def rotate_right(triple):
#     elem1, elem2, elem3 = triple
#     return (elem3, elem1, elem2)


rotate_left(triple)
rotate_right(triple)
