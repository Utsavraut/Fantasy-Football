import requests
import pandas as pd
import os
import time

# Directory to save the CSV file
save_directory = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\raw"  # Use raw string or forward slashes

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

# Define a function to fetch data from the FPL API
def fetch_fpl_data(season):
    # Endpoint to get the overall data
    url = f"https://fantasy.premierleague.com/api/bootstrap-static/"
    
    # Fetch data
    response = requests.get(url)
    data = response.json()

    # Convert data to DataFrame
    players_df = pd.DataFrame(data['elements'])
    teams_df = pd.DataFrame(data['teams'])
    events_df = pd.DataFrame(data['events'])
    positions_df = pd.DataFrame(data['element_types'])
    
    return players_df, teams_df, events_df, positions_df

# Fetch data for the 2022-23 season
season = "2022-23"
players_df, teams_df, events_df, positions_df = fetch_fpl_data(season)

# Merge player data with team data to get club names
players_df = players_df.merge(teams_df[['id', 'name']], left_on='team', right_on='id', suffixes=('', '_team'))
players_df.rename(columns={'name': 'club_name'}, inplace=True)

# Merge player data with positions data to get player positions
players_df = players_df.merge(positions_df[['id', 'singular_name']], left_on='element_type', right_on='id', suffixes=('', '_position'))
players_df.rename(columns={'singular_name': 'position'}, inplace=True)

# Convert cost to points (e.g., 55 to 5.5)
players_df['now_cost'] = players_df['now_cost'] / 10

# Select relevant columns for players
relevant_columns = [
    'first_name', 'second_name', 'club_name', 'position', 'now_cost', 'points_per_game', 'total_points', 'minutes',
    'goals_scored', 'assists', 'clean_sheets', 'goals_conceded', 'own_goals', 'penalties_saved',
    'penalties_missed', 'yellow_cards', 'red_cards', 'saves', 'bonus', 'bps', 'influence',
    'creativity', 'threat', 'ict_index', 'starts', 'expected_goals', 'expected_assists',
    'expected_goal_involvements', 'expected_goals_conceded'
]
players_df = players_df[relevant_columns]

# Save data to a CSV file
csv_file_path = os.path.join(save_directory, '2022-23_raw.csv')
players_df.to_csv(csv_file_path, index=False)

# Verify if the file is saved
if os.path.exists(csv_file_path):
    print(f"Data for the 2022-23 season saved successfully at {csv_file_path}.")
else:
    print(f"Failed to save data at {csv_file_path}.")

# Print the contents of the directory to check if the file exists
print("Contents of the save directory:", os.listdir(save_directory))
