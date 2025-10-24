import sys
from pathlib import Path
import requests
import local_settings
import settings
from gtfs import GTFS

try:
    gtfs = GTFS(
        live_url = settings.GTFS_LIVE_URL,
        api_key = local_settings.API_KEY,
        redis_url = None, # Not using Redis
        rebuild_cache = False,
        filter_stops = None, # Load all stops
        profile_memory = False
    )
    print("GTFS initialized successfully!")
except Exception as e:
    print(f"Error: {e}")

####################################################################
# Fetch live data from the API manually without using the GTFS class
####################################################################

api_key = local_settings.API_KEY
header = {
    "X-API-Key": api_key,
    "Accept": "application/json"
}

end_point = settings.GTFS_LIVE_URL

try:
    response = requests.get(end_point, headers=header)
    if response.status_code == 200:
        print(f"Successfully fetched data from {end_point}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"Response text: {response.text}")
    else:
        print(f"Failed to fetch data from {end_point}")
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
except Exception as e:
    print(f"Error: {e}")