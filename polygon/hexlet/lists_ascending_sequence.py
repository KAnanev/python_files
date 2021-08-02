def is_continuous_sequence(lst):
    if len(lst) <= 1:
        return False
    numb = lst[0]
    count = lst[0]
    for i in range(len(lst)-1):
        count += 1
        numb += count
    return numb == sum(lst)

# def is_continuous_sequence(source):
#     if len(source) < 2:
#         return False
#     for x, y in zip(source, source[1:]):
#         if (y - x) != 1:
#             return False
#     return True


is_continuous_sequence([5, 6, 6, 8, 7])

