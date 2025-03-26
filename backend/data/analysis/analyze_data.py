from pandas import read_csv, DataFrame

def load_data(file_path):
    return read_csv(file_path)

def analyze_player_statistics(df):
    player_stats = {
        'total_players': df.shape[0],
        'average_runs': df['runs'].mean(),
        'average_wickets': df['wickets'].mean(),
        'top_scorer': df.loc[df['runs'].idxmax(), 'player_name'],
        'top_wicket_taker': df.loc[df['wickets'].idxmax(), 'player_name'],
    }
    return player_stats

def main():
    file_path = '../raw_data/players_data.csv'
    df = load_data(file_path)
    stats = analyze_player_statistics(df)
    
    for key, value in stats.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()