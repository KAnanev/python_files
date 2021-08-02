from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50, verbose_name='Брэнд', )
    model = models.CharField(max_length=50, verbose_name='Модель', )

    def __str__(self):
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    review_count.short_description = 'Количество отзывов'


class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль', )
    title = models.CharField(max_length=100, verbose_name='Название', )
    text = models.TextField(verbose_name='Описание', )

    def __str__(self):
        return str(self.car) + ' ' + self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

