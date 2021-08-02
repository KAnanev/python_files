import json


class FindWiki:
    def __init__(self, path_read, path_write):
        self.read_file = open(path_read, "r")
        self.write_file = open(path_write, 'w', encoding='utf-8')
        self.data = json.load(self.read_file)
        self.start = 0
        self.end = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        data_1 = self.data[self.start]
        self.start += 1
        country = data_1['translations']['rus']['common']
        self.write_file.write(f"{country} - https://ru.wikipedia.org/wiki/{'_'.join(country.split())}\n")


if __name__ == '__main__':
    for find_str in FindWiki('countries.json', 'countries_link.txt'):
        find_str
