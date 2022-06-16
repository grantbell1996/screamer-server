
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    
    name = models.CharField(max_length=100)
    director = models.ForeignKey("Director", related_name="directed_by", on_delete=models.CASCADE)
    release_date = models.DateField()
    run_time = models.IntegerField()
    filming_location = models.CharField(max_length=50)
    synopsis =models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trailer = models.CharField(max_length=300)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    poster = models.CharField(max_length=500, null=True)