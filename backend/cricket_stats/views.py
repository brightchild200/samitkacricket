from django.shortcuts import render
from django.http import JsonResponse
from .models import Player, Match

# Fetch Player Stats from Database
def get_player_stats(request):
    player_name = request.GET.get('name', None)
    if player_name:
        try:
            player = Player.objects.get(name__iexact=player_name)
            data = {
                "name": player.name,
                "batting": {
                    "runs": player.runs,
                    "avg": player.batting_avg,
                    "fifties": player.fifties,
                },
                "bowling": {
                    "wickets": player.wickets,
                    "avg": player.bowling_avg,
                    "economy": player.economy,
                }
            }
            return JsonResponse(data)
        except Player.DoesNotExist:
            return JsonResponse({"error": "Player not found"}, status=404)
    return JsonResponse({"error": "No player name provided"}, status=400)

# Fetch Match Stats from Database
def get_match_stats(request):
    player_name = request.GET.get('name', None)
    if player_name:
        matches = Match.objects.filter(player__name__iexact=player_name)
        if matches.exists():
            data = [
                {
                    "date": match.date,
                    "opponent": match.opponent,
                    "runs_scored": match.runs_scored,
                    "wickets_taken": match.wickets_taken,
                }
                for match in matches
            ]
            return JsonResponse({"matches": data})
        return JsonResponse({"error": "No matches found for this player"}, status=404)
    return JsonResponse({"error": "No player name provided"}, status=400)

# Homepage View
def home(request):
    return render(request, 'index.html')

# Player Stats Page
def players(request):
    return render(request, 'players.html')

# Cricket World Cup 2023 Page
def cwc2023(request):
    return render(request, 'cwc2023.html')

# Champions Trophy 2025 Page
def ct2025(request):
    return render(request, 'ct2025.html')

def cwc2023(request):
    query = request.GET.get('name', None)  # Get the player name from the query string
    player = None
    if query:
        try:
            player = Player.objects.get(name__iexact=query)  # Case-insensitive match
        except Player.DoesNotExist:
            player = None
    return render(request, 'cwc2023.html', {'player': player})

def ct2025(request):
    query = request.GET.get('name', None)  # Get the player name from the query string
    player = None
    if query:
        try:
            player = Player.objects.get(name__iexact=query)  # Case-insensitive match
        except Player.DoesNotExist:
            player = None
    return render(request, 'ct2025.html', {'player': player})
