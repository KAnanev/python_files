line1 = (0, 10), (100, 130)
line2 = (42, 1), (42, 2)
line3 = (100, 50), (200, 50)


def is_inclined(tpl):
    return tpl[0][0] != tpl[1][0] and tpl[0][1] != tpl[1][1]


def is_vertical(tpl):
    return tpl[0][0] == tpl[1][0] and tpl[0][1] != tpl[1][1]


def is_horizontal(tpl):
    return tpl[0][0] != tpl[1][0] and tpl[0][1] == tpl[1][1]


def is_degenerated(tpl):
    return tpl[0][0] == tpl[1][0] and tpl[0][1] == tpl[1][1]


print(is_inclined(line1))


print(is_vertical(line2))


print(is_horizontal(line3))
