from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)
    language = models.CharField(max_length=20)

