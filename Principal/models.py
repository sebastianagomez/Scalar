from django.db import models

# Create your models here.

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default='No Title', unique = True)
    rating = models.IntegerField()
    movieInfo = models.TextField(max_length=500, default="")
    director = models.CharField(max_length=20, default="")
    runTime = models.CharField(max_length=20, default="2h 30m")
    leadingActor = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.title