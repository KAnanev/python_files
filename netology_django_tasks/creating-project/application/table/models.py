from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=50)
    width = models.IntegerField()
    number = models.IntegerField()

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '{number} - {name} - {width}'.format(number=self.number, name=self.name, width=self.width)


class Path(models.Model):
    path = models.CharField(max_length=50)

    def __str__(self):
        return self.path

    @staticmethod
    def get_path():
        path = Path.objects.first()
        if path:
            return path
        return None

    @staticmethod
    def set_path(value):
        path = Path.objects.first()
        if not path:
            path = Path()
            path.path = value
            path.save()
        return path
