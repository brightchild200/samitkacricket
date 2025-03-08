from django.contrib import admin
from django.urls import path, include
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/', views.players, name='players'),  # Route for displaying player statistics
    path('', views.home, name='home'),  # Route for homepage
]