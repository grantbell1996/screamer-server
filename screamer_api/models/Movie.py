
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    
    movie_id = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    director = models.ForeignKey("Director", related_name="directed_by", on_delete=models.CASCADE, null=True)
    release_date = models.DateField(null=True)
    run_time = models.IntegerField(null=True)
    filming_location = models.CharField(max_length=50)
    synopsis =models.CharField(max_length=300, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trailer = models.CharField(max_length=300, null=True)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE, null=True)
    poster = models.CharField(max_length=500, null=True)
    actor = models.ManyToManyField("Actor", through="MovieActor", null=True)