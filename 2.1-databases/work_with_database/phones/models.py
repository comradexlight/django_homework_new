from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели')
    image = models.CharField(max_length=250, verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='Наличие lte')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='url')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
