import hashlib


def md_hash(path):
    with open(path, 'r', encoding='utf-8') as file:
        for str_file in file.readlines():
            h = hashlib.md5(str_file.encode())
            p = h.hexdigest()
            yield p


if __name__ == '__main__':
    for i in md_hash('lermontov.txt'):
        print(i)

