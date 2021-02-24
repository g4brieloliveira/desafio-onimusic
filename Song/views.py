from django.shortcuts import redirect, render, redirect
from django.contrib import messages
from .forms import SongForm
from .models import Song

def song_init(request):
  context = {'song_init': Song.objects.all()}
  return render(request, 'Song/principal.html', context)

def song_list(request):
  context = {'song_list': Song.objects.all()}
  return render(request, 'Song/song_list.html', context)

def song_form(request, id = 0):
  if request.method == 'GET':
    if id == 0:
      form = SongForm()
    else:
      song = Song.objects.get(pk = id)
      form = SongForm(instance = song)
    return render(request, 'Song/song_form.html', {'form': form })
  else:
    if id == 0: 
      form = SongForm(request.POST)
    else:
      song = Song.objects.get(pk = id)
      form = SongForm(request.POST,instance = song)
    if form.is_valid():
      form.save()
      messages.info(request, 'Música enviada com sucesso!')
      
    return redirect('/song')

def song_delete(request, id):
  song = Song.objects.get(pk = id)
  song.delete()
  
  return redirect('/song/list')
