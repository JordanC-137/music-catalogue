from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField(max_length=200)

class Album(models.Model):
    title = models.TextField(max_length=200)
    artist = models.ForeignKey(Artist)
