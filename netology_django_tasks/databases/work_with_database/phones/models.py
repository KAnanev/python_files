from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.CharField(max_length=100)
