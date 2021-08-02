from icecream import ic

frame = ['A', ]

frame2 = ['']

frame3 = [' *', '# ', ]

# def enlarge(lst):
#     list_ret = []
#     for i in lst:
#         list_ret.append(''.join(i) * 2)
#     print(list_ret)


list_lst = [frame, frame2, frame3]

for item in list_lst:
    lst = []
    for i in item:
        row = [''.join(j) * 2 for j in i]
        lst.append(''.join(row))
        lst.append(''.join(row))
    print(lst)

# print(pow_string(string_))


# print(enlarge(frame2))

# print(enlarge(frame2))
