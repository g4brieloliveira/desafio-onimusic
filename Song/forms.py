from django import forms
from django.forms import fields
from .models import Song

class SongForm(forms.ModelForm):
  class Meta:
    model = Song
    fields = ( 'artist', 'title', 'duration', 'spotify_published', 'youtube_published')
    labels = {
      'title': 'Música',
      'duration': 'Duração da música',
      'spotify_published': 'Spotify',
      'youtube_published': 'YouTube',
      'artist': 'Artista',
    }
  
  def __init__(self, *args, **kwargs):
    super(SongForm, self).__init__(*args, **kwargs)
    self.fields['artist'].empty_label = "Selecione um artista"