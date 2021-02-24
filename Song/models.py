from django.db import models
from django.db.models.deletion import CASCADE
from Artist.models import Artist

class Song(models.Model):
  title = models.CharField(max_length=50)
  duration = models.IntegerField()
  spotify_published = models.BooleanField(default=False)
  youtube_published = models.BooleanField(default=False)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
