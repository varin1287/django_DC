from django.db import models


class Category(models.Model):
    """Модель категории"""
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField('url', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Tag(models.Model):
    """Модель тегов"""
    name = models.CharField('Имя', max_length=100)
    slug = models.SlugField(max_length=100, verbose_name='url')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'теги'


class Post(models.Model):
    """Модель постов"""
    title = models.CharField(max_length=100, verbose_name='Название поста')
    mini_text = models.TextField(max_length=200, verbose_name='Краткое описание')
    text = models.TextField()
    created_date_and_nbsp = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, verbose_name='url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'посты'


class Comment(models.Model):
    """Модель Коментариев"""
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField()

    class Meta:
        verbose_name = 'Коментарии'
