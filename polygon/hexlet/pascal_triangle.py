def triangle(rows):
    row = [1]
    for i in range(rows):
        row = [sum(x) for x in zip([0]+row, row+[0])]
    return row


print(triangle(5))
