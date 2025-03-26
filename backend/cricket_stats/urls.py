from django.contrib import admin
from django.urls import path, include
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', views.players, name='players'),  # Route for displaying player statistics
    path('', views.home, name='home'),  # Route for homepage
    path('cwc2023/', views.cwc2023, name='cwc2023'),
    path('ct2025/', views.ct2025, name='ct2025'),
    path('get_player_stats/', views.get_player_stats, name='get_player_stats'),
    path('get_match_stats/', views.get_match_stats, name='get_match_stats'),
   
]
#  path('predicted/', views.predicted, name='preidicted'),