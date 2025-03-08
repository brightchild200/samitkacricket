import pandas as pd

def extract_data_from_csv(file_path):
    """
    Extracts player data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing player data.

    Returns:
        DataFrame: A pandas DataFrame containing the extracted player data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error extracting data from {file_path}: {e}")
        return None

def extract_data_from_api(api_url):
    """
    Extracts player data from a given API.

    Args:
        api_url (str): The URL of the API to extract data from.

    Returns:
        dict: A dictionary containing the extracted player data.
    """
    import requests

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error extracting data from API {api_url}: {e}")
        return None

# Example usage
if __name__ == "__main__":
    csv_data = extract_data_from_csv('data/raw_data/players_data.csv')
    print(csv_data)

    api_data = extract_data_from_api('https://api.example.com/cricket-players')
    print(api_data)