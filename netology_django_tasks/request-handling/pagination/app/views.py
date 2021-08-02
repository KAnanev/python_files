from csv import DictReader

from urllib.parse import urlencode

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    next_page_url, prev_page_url = None, None

    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as File:
        reader = DictReader(File)
        data_bus_stations = [
            [i['Name'], i['Street'], i['District']] for i in reader
        ]

    paginator = Paginator(data_bus_stations, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    current_page = page_obj.number

    if page_obj.has_previous():
        prev_page_url = '?'.join(
            [
                reverse(bus_stations), urlencode(
                    {'page': page_obj.previous_page_number()}
                )
            ]
        )

    if page_obj.has_next():
        next_page_url = '?'.join(
            [
                reverse(bus_stations), urlencode(
                    {'page': page_obj.next_page_number()}
                )
            ]
        )

    return render(request, 'index.html', context={
        'bus_stations': [
            {
                'Name': page_obj[i][0],
                'Street': page_obj[i][1],
                'District': page_obj[i][2]
            } for i, j in enumerate(page_obj)
        ],
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
