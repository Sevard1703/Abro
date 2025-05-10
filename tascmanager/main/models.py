from django.db import models
import os

# Create your models here.

class Task (models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title