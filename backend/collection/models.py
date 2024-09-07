from django.db import models
from django.db.models import Q
from django.conf import settings

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

class Rating(models.Model):
    stars = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user_id = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(stars__gte=0) & Q(stars__lte=5),
                name = "valid_range_of_stars_constraint"
            )
        ]