from collections import Counter

from django.shortcuts import render

from django.http import HttpResponseNotFound

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнуляться
counter_show = Counter()
counter_click = Counter()
reference_point = 1


def index(request):
    # Реализуйте логику подсчета количества переходов с лендинга по GET параметру from-landing

    link = request.GET.get('from-landing')
    counter_click.update({link: reference_point})
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    # return render(request, 'landing.html')

    link = request.GET.get('ab-test-arg')
    counter_show.update({link: reference_point})
    if link == 'original':
        return render(request, 'landing.html')
    elif link == 'test':
        return render(request, 'landing_alternate.html')
    else:
        return HttpResponseNotFound('<h1>Page not found</h1>')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:

    def show(value):
        result = counter_show[value]
        return 1 if result == 0 else result

    test_conversion = counter_click['test'] / show('test')
    original_conversion = counter_click['original'] / show('original')
    context = {
        'test_conversion': '{:.1f}'.format(test_conversion),
        'original_conversion': '{:.1f}'.format(original_conversion),
    }

    return render(request, 'stats.html', context=context)
