
from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    body = models.CharField(max_length=250)
    rating = models.IntegerField()
