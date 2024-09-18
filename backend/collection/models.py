from django.db import models
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User

from openai import OpenAI

# Create your models here.
class Artist(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.TextField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    release_date = models.DateField(null=True, blank=True)
    period = models.ForeignKey("Period", null=True, blank=True, on_delete=models.SET_NULL)
    rym_rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Period(models.Model):
    name = models.TextField(max_length = 200)
    description = models.TextField()
    color = models.TextField(max_length=6)

    def __str__(self):
        return self.name
    
    def save(self, generate_description=False, *args, **kwargs):
        #If True, use ChatGPT to auto generate a brief summary of the musical period
        if generate_description and not self.description:
            request_content = f"""Tell me about the {self.name} period of music
                                and some key musicians in under 50 words"""
            
            client = OpenAI()
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages = [
                    {"role": "user", "content": request_content}
                ]
            )
            response = completion.choices[0].message.content
            self.description = response
        super().save(*args, **kwargs)

class Rating(models.Model):
    stars = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(stars__gte=0) & Q(stars__lte=5),
                name = "valid_range_of_stars_constraint"
            )
        ]