from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    car = ('brand', 'model', )
    list_display = car + ('review_count', )
    list_filter = search_fields = car
    ordering = ('pk', )


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'title', )
    list_filter = search_fields = ('car', )
    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
