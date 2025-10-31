import os
import pandas as pd
import requests

def get_files_from_path(directory: str, extension: str = '.txt') -> list:
    '''
    Returns a list of all files in a directory with a given extension.
    '''
    filenames = []
    for entry in os.listdir(directory):
        full_path = os.path.join(directory, entry)
        _, _extension = os.path.splitext(full_path)
        if os.path.isfile(full_path) and _extension == extension:
            filenames.append(full_path)
    return filenames

def generate_df_from_txt(filename: str):
    '''
    Reads a txt file and [always] returns a pandas DataFrame even if the file is empty.
    If the file is empty, the DataFrame will have 0 rows.
    '''
    try:
        df = pd.read_csv(filename)
        return df
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return pd.DataFrame()

def get_access_token(refresh_token: str) -> str | None:
    '''
    Makes a POST request to the Mobility Database API to get an access token.
    '''
    headers = {'Content-Type': 'application/json'}
    data = {'refresh_token': refresh_token}

    try:
        r = requests.post(
            url = "https://api.mobilitydatabase.org/v1/tokens",
            headers = headers,
            json = data
        )

        r.raise_for_status()
        if r.status_code == 200:
            token_response = r.json()
            return token_response.get('access_token')
        else:
            print(f"Error getting access token: {r.status_code}")
            return None

    except Exception as e:
        print(f"Error getting access token: {e}")
        return None
