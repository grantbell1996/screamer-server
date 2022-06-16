from operator import truediv
from django.db import models
from django.forms import CharField


class Director(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    death_date = models.DateField(null=True)
    bio = models.CharField(max_length=200)
    image = models.CharField(max_length=500, null=True)