from django.db import models
from datetime import *

# Create your models here.
# Работа с Базами Данных

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории') # строка
    alias = models.SlugField(verbose_name='Псевдоним категории')

    class Meta: # описание в админке
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return 'Категория %s' % self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара') # строка
    price = models.IntegerField(default=0, verbose_name='Цена товара') # integer
    image = models.CharField(max_length=255, verbose_name='Путь к изображению') # integer
    alias = models.SlugField(verbose_name='Псевдоним товара')
    description = models.CharField(max_length=255, verbose_name='Описание товара')

    category = models.ForeignKey(Category) # ссылаемся на категорию

    class Meta:  # описание в админке
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return 'Товар %s' % self.name