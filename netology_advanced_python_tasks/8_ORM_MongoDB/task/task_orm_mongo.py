import csv
import re
from datetime import datetime

from pymongo import MongoClient

connection = MongoClient()
db = connection.task_database
collection = db.task_collection


def read_data(csv_file, db):
    """
    Загрузить данные в бд из CSV-файла
    """
    with open(csv_file, encoding='utf8') as csvfile:
        # прочитать файл с данными и записать в коллекцию
        reader = csv.DictReader(csvfile)
        for item in reader:
            item['Цена'] = int(item['Цена'])
            item['Дата'] = datetime(2020, int(item['Дата'].split('.')[1]), int(item['Дата'].split('.')[0]))
            db.insert_one(item)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастанию цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    return db.find().sort("Цена", 1)


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке,
    например "Seconds to"),
    и вернуть их по возрастанию цены
    """

    regex = re.compile(name, re.I)
    return db.find({'Исполнитель': regex}).sort("Цена", 1)



if __name__ == '__main__':
    # read_data('artists.csv', collection)
    # print(list(find_cheapest(collection)))
    print(list(find_by_name('fest', collection)))
