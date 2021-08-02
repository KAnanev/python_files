import csv
from pprint import pprint


with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as File:
    reader = csv.DictReader(File)
    list_station = [[i['Name'], i['Street'], i['District']] for i in reader]

print(list_station[-1])
