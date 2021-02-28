from django.db import models
import datetime

counter = 1
class Artist(models.Model):
  name = models.CharField(max_length=30)
  date_joined = models.DateField(blank=False, null=True)
  
  def __str__(self):
    return self.name 