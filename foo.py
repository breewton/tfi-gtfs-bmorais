import requests
import pandas as pd

BASE = "http://localhost:7341"

# 1) Discover recent stop_ids
r = requests.get(f"{BASE}/api/v1/recent-stops", headers={"Accept": "application/json"})
r.raise_for_status()
stops = r.json().get("stops", [])
stops_df = pd.DataFrame(stops)
print(stops_df.head())

# Pick the most recently seen stop_id with data
stops_df["last_seen"] = pd.to_datetime(stops_df["last_seen"], errors="coerce")
candidate = stops_df.sort_values("last_seen", ascending=False).query("count > 0").head(1)
if candidate.empty:
    raise RuntimeError("No recent stops yet. Wait a minute for the live feed to populate.")
stop_id = candidate.iloc[0]["stop_id"]

# 2) Fetch arrivals for that stop_id (realtime-only works with raw stop_id or stop number)
arr = requests.get(
    f"{BASE}/api/v1/arrivals",
    params={"stop": stop_id},
    headers={"Accept": "application/json"},
)
arr.raise_for_status()
data = arr.json()

# 3) Flatten arrivals to a DataFrame
items = data.get(str(stop_id), data.get(stop_id, {})).get("arrivals", [])
arrivals_df = pd.DataFrame(items)
if not arrivals_df.empty:
    arrivals_df["scheduled_arrival"] = pd.to_datetime(arrivals_df["scheduled_arrival"], errors="coerce")
    arrivals_df["real_time_arrival"] = pd.to_datetime(arrivals_df["real_time_arrival"], errors="coerce")

print(arrivals_df.head())