import re

from django.template import library

register = library.Library()


@register.filter
def grey_color(value):
    return 'grey'


@register.filter
def color_filter(value):
    regex = re.compile(r'^-?\d*\.{0,1}\d+$')
    if regex.match(value):
        value = float(value)
        if value < 0:
            return 'green'
        if 1 < value < 2:
            return '#FFCBDB'
        if 2 < value < 5:
            return '#FF007F'
        if value > 5:
            return '#92000a'

