from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Categories'

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=150)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title