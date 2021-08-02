from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    context = {
        'object_list': Student.objects.order_by(
            ordering
        ).prefetch_related('teacher')
    }

    return render(request, template, context)
