import csv
import os
from cricket_stats.models import Player

def run():
    # Dynamically construct the path to the CSV file
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    csv_file_path = os.path.join(base_dir, 'data', 'raw_data', 'players_data.csv')
    print(f"Looking for CSV file at: {csv_file_path}")
    print(os.path.exists(csv_file_path))

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Player.objects.create(
                name=row['Player'],
                matches=int(row['Matches']),
                innings=int(row['Innings']),
                runs=int(row['Runs']),
                batting_avg=float(row['Average']),
                strike_rate=float(row['Strike Rate']),
                hundreds=int(row['100s']),
                fifties=int(row['50s']),
                best_score=row['Best Score']
            )