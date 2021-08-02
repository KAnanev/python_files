from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    articles = models.ManyToManyField('Scope', through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    topic = models.CharField(max_length=128, verbose_name='Наименование тега')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тег'

    def __str__(self):
        return self.topic


class ArticleScope(models.Model):
    topic = models.ForeignKey(Scope, on_delete=models.CASCADE, verbose_name='Категория', related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.article}_{self.topic}'
