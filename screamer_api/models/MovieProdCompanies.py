from django.db import models

class MovieProdCompany(models.Model):

    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    production_company = models.ForeignKey("ProductionCompany", on_delete=models.CASCADE)