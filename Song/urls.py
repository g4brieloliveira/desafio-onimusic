from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.song_init, name='song_init'),
    path('register/', views.song_form, name='song_insert'),
    path('list/', views.song_list, name='song_list'),
    path('<int:id>/', views.song_form, name='song_update'),
    path('delete/<int:id>/', views.song_delete, name='song_delete'),
    
]
