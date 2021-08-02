import requests
chars = ['a', 'b', 'c']

for char in chars:
    print(char)

iter_chars = chars.__iter__() # for char in chars:
char = iter_chars.__next__()
print(char)

iter_chars = iter(chars) # for char in chars:
char = next(iter_chars)
print(char)
char = next(iter_chars)
print(char)
char = next(iter_chars)
print(char)
char = next(iter_chars)
print(char)

class Myrange:
    def __init__(self, start, end):
        self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start

for item in Myrange(1, 10):
    print(item)


class CheckSite:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, encoding='utf-8')
        self.session = requests.Session()

    def __iter__(self):
        return self

    def __next__(self):
        url = self.file.readline().strip()
        if not url:
            raise StopIteration
        response = self.session.get(f'https://{url}')
        status_code = response.status_code
        return {url: status_code}

def check_site(path):
    session = requests.Session()
    with open(path, encoding='utf8') as hosts_file:
        for url in hosts_file:
            url = url.strip()
            status = session.get(f'http://{url}').status_code
            yield {url: status}


if __name__ == '__main__':
    for url_status in check_site('sites.list'):
        print(url_status)


