# from django.shortcuts import render

# # Hardcoded player data
# PLAYERS_DATA = {
#     "Rohit Sharma": {
#         "role": "Batsman",
#         "runs": 9207,
#         "batting_avg": 48.96,
#         "fifties": 43,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0
#     },
#     "Virat Kohli": {
#         "role": "Batsman",
#         "runs": 12311,
#         "batting_avg": 59.07,
#         "fifties": 62,
#         "wickets": 4,
#         "bowling_avg": 166.0,
#         "economy": 5.0,
#     },
#     "MS Dhoni": {
#         "role": "Batsman",
#         "runs": 10773,
#         "batting_avg": 50.57,
#         "fifties": 73,
#         "wickets": 1,
#         "bowling_avg": 36.0,
#         "economy": 4.0,
#     },
#     "Ravindra Jadeja": {
#         "role": "Allrounder",
#         "runs": 2447,
#         "batting_avg": 32.58,
#         "fifties": 13,
#         "wickets": 210,
#         "bowling_avg": 35.3,
#         "economy": 4.8,
#     },  
#     "Jasprit Bumrah": {
#         "role": "Bowler",
#         "runs": 800,
#         "batting_avg": 20.0,
#         "fifties": 0,
#         "wickets": 250,
#         "bowling_avg": 20.0,
#         "economy": 4.5,
#     },
#     "R Ashwin": {
#         "role": "Bowler",
#         "runs": 707,
#         "batting_avg": 16.79,
#         "fifties": 0,
#         "wickets": 251,
#         "bowling_avg": 32.3,
#         "economy": 4.7,
#     },
#     "Mohammed Shami": {
#         "role": "Bowler",
#         "runs": 500,
#         "batting_avg": 20.0,
#         "fifties": 0,
#         "wickets": 200,
#         "bowling_avg": 24.0,
#         "economy": 5.0,
#     },
#     "Shreyas Iyer": {
#         "role": "Batsman",
#         "runs": 2000,
#         "batting_avg": 42.0,
#         "fifties": 10,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },
#     "KL Rahul": {
#         "role": "Batsman",
#         "runs": 5000,
#         "batting_avg": 45.0,
#         "fifties": 25,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },
#     "Hardik Pandya": {
#         "role": "Allrounder",
#         "runs": 1000,
#         "batting_avg": 29.0,
#         "fifties": 2,
#         "wickets": 50,
#         "bowling_avg": 31.0,
#         "economy": 4.0,
#     },
#     "Bhuvneshwar Kumar": {
#         "role": "Bowler",
#         "runs": 200,
#         "batting_avg": 20.0,
#         "fifties": 0,
#         "wickets": 150,
#         "bowling_avg": 25.0,
#         "economy": 4.5,
#     },
#     "Shikhar Dhawan": {
#         "role": "Batsman",
#         "runs": 6793,
#         "batting_avg": 49.14,
#         "fifties": 39,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },
#     "Yuzvendra Chahal": {
#         "role": "Bowler",
#         "runs": 100,
#         "batting_avg": 20.0,
#         "fifties": 0,
#         "wickets": 150,
#         "bowling_avg": 25.0,
#         "economy": 4.5,
#     },
#     "Shubman Gill": {
#         "role": "Batsman",
#         "runs": 1500,
#         "batting_avg": 40.0,
#         "fifties": 5,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },
#     "Prithvi Shaw": {
#         "role": "Batsman",
#         "runs": 1000,
#         "batting_avg": 35.0,
#         "fifties": 3,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },
#     "Yashasvi Jaiswal": {
#         "role": "Batsman",
#         "runs": 500,
#         "batting_avg": 30.0,
#         "fifties": 2,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },
#     "Mohammed Siraj": {
#         "role": "Bowler",
#         "runs": 100,
#         "batting_avg": 20.0,
#         "fifties": 0,
#         "wickets": 100,
#         "bowling_avg": 24.0,
#         "economy": 4.5,
#     },
#     "Suryakumar Yadav": {
#         "role": "Batsman",
#         "runs": 1500,
#         "batting_avg": 40.0,
#         "fifties": 5,
#         "wickets": 0,
#         "bowling_avg": 0.0,
#         "economy": 0.0,
#     },

#     # Add more players as needed
# }

# def cwc2023(request):
#     query = request.GET.get('name', None)  # Get the player name from the query string
#     player = None
#     if query:
#         player = PLAYERS_DATA.get(query)  # Fetch player data from the hardcoded dictionary
#     return render(request, 'cwc2023.html', {'player': player})

# def ct2025(request):
#     query = request.GET.get('name', None)  # Get the player name from the query string
#     player = None
#     if query:
#         player = PLAYERS_DATA.get(query)  # Fetch player data from the hardcoded dictionary
#     return render(request, 'ct2025.html', {'player': player})





# databse

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

def cwc2027(request):
    return render(request, 'cwc2027.html')

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
