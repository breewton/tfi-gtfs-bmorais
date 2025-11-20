# Python Fundamentals - Practice Challenges

## Overview

This document contains basic Python challenges to assess your understanding of fundamental concepts used in this GTFS data processing project. These challenges are designed to help you practice the building blocks of data processing, API interaction, and file handling that form the foundation of working with transit data.

**What you'll learn:**
- Working with files and directories
- Processing CSV data with pandas
- Making HTTP API requests
- Handling errors gracefully
- Validating function inputs
- Manipulating dictionaries and DataFrames

---

## Tools and Libraries You'll Need

Before starting these challenges, make sure you have the following installed:

### Required Python Libraries

```bash
pip install -r requests.txt
```

**Library Breakdown:**
- **`pandas`** - For reading, manipulating, and analyzing tabular data (CSV files)
- **`requests`** - For making HTTP requests to APIs
- **`pathlib`** (built-in) - For working with file paths in a cross-platform way
- **`os`** (built-in) - For file system operations
- **`zipfile`** (built-in) - For working with ZIP archives
- **`io`** (built-in) - For working with byte streams

### Python Version
- Python 3.7 or higher recommended

### Development Environment
- Any text editor or IDE (VS Code, PyCharm, Jupyter Notebook, etc.)
- Terminal/Command Prompt for running scripts

### Optional but Helpful
- **Jupyter Notebook** - Great for testing code interactively
  ```bash
  pip install jupyter
  jupyter notebook
  ```

---

## General Hints and Tips

### Before You Start
1. **Create a workspace** - Make a new directory for your challenge solutions
2. **Test incrementally** - Don't write all the code at once; test each step
3. **Read error messages** - Python's error messages are very helpful and tell you exactly what went wrong
4. **Use print statements** - When debugging, print intermediate values to understand what's happening

### Common Pitfalls to Avoid
- **File paths:** Make sure your working directory is correct when referencing files like `data/stops.txt`
- **Column names:** Be careful with exact column names in pandas (they're case-sensitive!)
- **Empty DataFrames:** Always check if a DataFrame is empty before processing it
- **API rate limits:** Be mindful when making multiple API requests in loops

### Python Best Practices
```python
# DO: Use descriptive variable names
total_stops = len(df)

# DON'T: Use single letters (unless in loops)
t = len(df)

# DO: Check for None or empty values
if not data:
    raise ValueError("Data is required")

# DO: Use f-strings for readable string formatting (Python 3.6+)
print(f"Found {count} results")

# DON'T: Use old-style formatting
print("Found %d results" % count)
```

### Debugging Strategies
1. **Start simple:** Get the basic version working, then add complexity
2. **Check data types:** Use `type()` to verify what you're working with
3. **Inspect data structures:** 
   - For dictionaries: `print(data.keys())`
   - For DataFrames: `print(df.head())`, `print(df.columns)`
   - For lists: `print(len(my_list))`, `print(my_list[:5])`
4. **Use try/except during development:** Catch errors to see what's happening
   ```python
   try:
       # your code here
   except Exception as e:
       print(f"Error: {e}")
       print(f"Error type: {type(e)}")
   ```

### Useful Pandas Cheat Sheet
```python
# Reading data
df = pd.read_csv("file.csv")

# Inspecting data
df.head()              # First 5 rows
df.columns             # Column names
df.shape               # (rows, columns)
len(df)                # Number of rows
df.info()              # Column types and info

# Filtering
df[df['column'] == value]           # Filter by value
df[df['column'].isin([val1, val2])] # Filter by multiple values

# Selecting
df['column']           # Single column (Series)
df[['col1', 'col2']]   # Multiple columns (DataFrame)
```

### Useful Requests Cheat Sheet
```python
import requests

# Basic GET request
response = requests.get("https://api.example.com/data")

# With headers
headers = {"Authorization": "Bearer token123"}
response = requests.get(url, headers=headers)

# With query parameters
params = {"stop_id": "123", "limit": 10}
response = requests.get(url, params=params)

# Check response
response.status_code    # 200 = success
response.json()         # Parse JSON response
response.text           # Raw text response
response.raise_for_status()  # Raise error if status not 2xx
```

---

## Challenge Structure

Each challenge below follows this format:
- **Background:** How this relates to the real project
- **Task:** Step-by-step requirements
- **Hints:** Helpful nudges without spoiling the solution
- **Solution:** Click to reveal the complete answer

**Tip:** Try to solve each challenge without looking at the solution first! If you get stuck, review the hints above or check the Python documentation.

---

## Challenge 1: Working with Files and Paths

**Background:** Our project reads GTFS data from text files in the `data/` directory.

**Task:** Write a Python script that:
1. Lists all files in the `data/` directory
2. Prints only the filenames (not the full path)
3. Counts how many `.txt` files are in the directory

**Expected Output Example:**
```
agency.txt
routes.txt
stops.txt
...
Total .txt files: 10
```

<details>
<summary>Solution</summary>

```python
import os

data_dir = "data"
txt_count = 0

for filename in os.listdir(data_dir):
    print(filename)
    if filename.endswith('.txt'):
        txt_count += 1

print(f"\nTotal .txt files: {txt_count}")
```
</details>

---

## Challenge 2: Reading CSV Files with Pandas

**Background:** GTFS files are CSV-formatted text files. We use pandas to read them.

**Task:** Write a script that:
1. Reads the `data/stops.txt` file using pandas
2. Prints the number of rows in the DataFrame
3. Prints the column names
4. Displays the first 3 rows

**Hint:** Use `pd.read_csv()`, `len()`, `.columns`, and `.head()`

<details>
<summary>Solution</summary>

```python
import pandas as pd

df = pd.read_csv("data/stops.txt")

print(f"Number of rows: {len(df)}")
print(f"\nColumn names: {df.columns.tolist()}")
print(f"\nFirst 3 rows:")
print(df.head(3))
```
</details>

---

## Challenge 3: Working with Dictionaries

**Background:** API responses are typically returned as JSON, which Python converts to dictionaries.

**Task:** Given this sample API response:
```python
response = {
    "stop_8220DB000689": {
        "arrivals": [
            {"route": "46A", "headsign": "Phoenix Park", "scheduled_arrival": "14:30"},
            {"route": "145", "headsign": "Heuston Station", "scheduled_arrival": "14:35"}
        ]
    },
    "stop_8220DB000123": {
        "arrivals": [
            {"route": "25", "headsign": "City Centre", "scheduled_arrival": "14:40"}
        ]
    }
}
```

Write code that:
1. Prints all stop IDs (the keys)
2. Counts the total number of arrivals across all stops
3. Prints the route number and headsign of each arrival

<details>
<summary>Solution</summary>

```python
response = {
    "stop_8220DB000689": {
        "arrivals": [
            {"route": "46A", "headsign": "Phoenix Park", "scheduled_arrival": "14:30"},
            {"route": "145", "headsign": "Heuston Station", "scheduled_arrival": "14:35"}
        ]
    },
    "stop_8220DB000123": {
        "arrivals": [
            {"route": "25", "headsign": "City Centre", "scheduled_arrival": "14:40"}
        ]
    }
}

# 1. Print all stop IDs
print("Stop IDs:")
for stop_id in response.keys():
    print(f"  - {stop_id}")

# 2. Count total arrivals
total_arrivals = 0
for stop_data in response.values():
    total_arrivals += len(stop_data['arrivals'])
print(f"\nTotal arrivals: {total_arrivals}")

# 3. Print route and headsign
print("\nArrivals:")
for stop_id, stop_data in response.items():
    for arrival in stop_data['arrivals']:
        print(f"  Route {arrival['route']} to {arrival['headsign']}")
```
</details>

---

## Challenge 4: Making HTTP Requests

**Background:** We fetch GTFS data from APIs using the `requests` library.

**Task:** Write a script that:
1. Makes a GET request to `https://api.github.com/users/python` ## Generic API endpoint for testing
2. Checks if the request was successful (status code 200)
3. Parses the JSON response
4. Prints the user's name and number of public repositories

**Hint:** Use `requests.get()`, `.status_code`, and `.json()`

<details>
<summary>Solution</summary>

```python
import requests

url = "https://api.github.com/users/python"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Public repos: {data['public_repos']}")
else:
    print(f"Request failed with status code: {response.status_code}")
```
</details>

---


## Challenge 5: Function Input Validation

**Background:** Our functions validate inputs before processing them.

**Task:** Write a function `get_route_info(route_id, routes_data)` that:
1. Takes a `route_id` (string) and a `routes_data` (dictionary)
2. First checks if `route_id` is provided (not None or empty string), if not raise `ValueError("Route ID is required")`
3. Then checks if `route_id` exists in `routes_data`, if not raise `ValueError("Route ID not found")`
4. Returns the route data if validation passes

Test with:
```python
routes = {
    "46A": {"name": "Phoenix Park", "type": "bus"},
    "145": {"name": "Heuston Station", "type": "bus"}
}
```

<details>
<summary>Solution</summary>

```python
def get_route_info(route_id, routes_data):
    if not route_id:
        raise ValueError("Route ID is required")
    
    if route_id not in routes_data:
        raise ValueError("Route ID not found")
    
    return routes_data[route_id]

# Test
routes = {
    "46A": {"name": "Phoenix Park", "type": "bus"},
    "145": {"name": "Heuston Station", "type": "bus"}
}

print(get_route_info("46A", routes))  # Works
# print(get_route_info("", routes))   # Raises ValueError: Route ID is required
# print(get_route_info("999", routes)) # Raises ValueError: Route ID not found
```
</details>

---

## Challenge 6: Filtering DataFrames

**Background:** We use pandas to filter and analyze GTFS data.

**Task:** Given a DataFrame of bus stops, write code that:
1. Creates a sample DataFrame with columns: `stop_id`, `stop_name`, `wheelchair_accessible` (values: 0 or 1)
2. Filters to show only wheelchair accessible stops (where `wheelchair_accessible == 1`)
3. Prints the count and the stop names

**Sample data:**
```python
data = {
    'stop_id': ['001', '002', '003', '004'],
    'stop_name': ['Main St', 'Park Ave', 'Oak Rd', 'Elm St'],
    'wheelchair_accessible': [1, 0, 1, 1]
}
```

<details>
<summary>Solution</summary>

```python
import pandas as pd

data = {
    'stop_id': ['001', '002', '003', '004'],
    'stop_name': ['Main St', 'Park Ave', 'Oak Rd', 'Elm St'],
    'wheelchair_accessible': [1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Filter for wheelchair accessible stops
accessible_stops = df[df['wheelchair_accessible'] == 1]

print(f"Number of wheelchair accessible stops: {len(accessible_stops)}")
print("\nAccessible stops:")
print(accessible_stops['stop_name'].tolist())
```
</details>



## Learning Objectives Covered

By completing these challenges, you should be comfortable with:
- File system operations (`os` module)
- Working with file paths (`pathlib`)
- Reading CSV files with pandas
- Basic DataFrame operations (filtering, combining, selecting)
- Making HTTP requests with `requests`
- Working with JSON/dictionaries
- Input validation
- Function parameters and return values
- Basic data structures (lists, dictionaries)

Good luck!