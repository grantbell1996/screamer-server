from django.db import models

class ProductionCompany(models.Model):

    name = models.CharField(max_length=100)
    year_founded = models.DateField()
    location = models.CharField(max_length=50)

