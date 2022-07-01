from django.db import models
from django.contrib.auth.models import User

class List(models.Model):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.ForeignKey("Movie", on_delete=models.CASCADE)