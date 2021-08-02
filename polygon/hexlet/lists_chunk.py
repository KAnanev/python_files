# def chunked(num, data):
#     return [data[i:i + num] for i in range(0, len(data), num)]

def chunked(num, data):
    list_data = []
    for i in range(0, len(data), num):
        list_data.append(data[i:i + num])
    return list_data


print(chunked(2, ('A', 'B', 'C', 'D')))


