from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

# Load player data from CSV
def load_player_data():
    data = pd.read_csv('data/raw_data/players_data.csv')
    return data

# View for displaying player statistics
def players(request):
    player_data = load_player_data()
    players_list = player_data.to_dict(orient='records')
    return render(request, 'index.html', {'players': players_list})

# View for the homepage
def home(request):
    return render(request, 'index.html')