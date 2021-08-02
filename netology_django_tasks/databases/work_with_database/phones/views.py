from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    query_set = Phone.objects.all()
    sort = request.GET.get('sort', None)

    if sort == 'name':
        query_set = query_set.order_by('name')
    if sort == 'min_price':
        query_set = query_set.order_by('price')
    if sort == 'max_price':
        query_set = query_set.order_by('-price')

    template = 'catalog.html'

    context = {
        'values': query_set
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    content = Phone.objects.get(slug=slug)
    context = {
        'value': content
    }
    return render(request, template, context)
