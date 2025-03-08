from pandas import read_csv, DataFrame

def clean_data(file_path):
    # Load the data
    data = read_csv(file_path)

    # Drop duplicates
    data = data.drop_duplicates()

    # Fill missing values
    data.fillna(method='ffill', inplace=True)

    # Convert data types if necessary
    data['Age'] = data['Age'].astype(int)
    data['Matches'] = data['Matches'].astype(int)
    data['Runs'] = data['Runs'].astype(int)

    # Remove any rows with invalid data
    data = data[data['Runs'] >= 0]

    return data

if __name__ == "__main__":
    cleaned_data = clean_data('../raw_data/players_data.csv')
    cleaned_data.to_csv('../raw_data/cleaned_players_data.csv', index=False)