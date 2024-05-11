from django.db import models

class HashKey (models.Model):
    ids = models.PositiveIntegerField()
    hash = models.CharField(max_length=100000000000000000000000)

# Create your models here.
