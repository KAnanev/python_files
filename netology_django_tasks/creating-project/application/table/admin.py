from django.contrib import admin
from table.models import Path, Table


@admin.register(Path, Table)
class TableAdmin(admin.ModelAdmin):
    pass

