from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.TextField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.DateField(null=True, blank=True)
    period = models.ForeignKey("Period", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Period(models.Model):
    name = models.TextField(max_length = 200)
    description = models.TextField()
    color = models.TextField(max_length=6)

    def __str__(self):
        return self.name
