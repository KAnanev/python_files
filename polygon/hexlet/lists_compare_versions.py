def compare_version(version_1, version_2):
    lst_version_1 = [int(i) for i in version_1.split('.')]
    lst_version_2 = [int(i) for i in version_2.split('.')]
    if lst_version_1 > lst_version_2:
        return 1
    elif lst_version_1 < lst_version_2:
        return -1
    else:
        return 0


assert compare_version('0.1', '0.2') == -1
assert compare_version('0.2', '0.1') == 1
assert compare_version('4.2', '4.2') == 0
assert compare_version('0.2', '0.12') == -1
assert compare_version('3.2', '4.12') == -1
assert compare_version('3.2', '2.12') == 1

