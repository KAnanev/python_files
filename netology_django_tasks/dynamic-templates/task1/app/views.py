from django.shortcuts import render

from app.settings import FILE_INFLATION_CSV

import csv




def inflation_view(request):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    with open(FILE_INFLATION_CSV, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        read_inflation = [
            '-' if i is None else i for i in reader
        ]

    context = {
        'table_header': read_inflation[0],
        'table_rows': read_inflation[1:]
    }

    return render(request, template_name,
                  context)
