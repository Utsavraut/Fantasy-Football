# import pandas as pd
# import os
# import joblib

# # Directories for features data and model
# features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
# model_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\models\trained_model.pkl"

# # Paths for features and output files
# features_path = os.path.join(features_dir, '2022-23_features.csv')
# top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')

# def get_top_players(data, position, num_required):
#     players = []
#     total_cost = 0
#     club_count = {}
    
#     # Filter players by position and sort by cost
#     position_data = data[data['position'] == position].sort_values(by='cost', ascending=True)
    
#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']
        
#         if club_count.get(club, 0) < 3 and total_cost + cost <= 100:
#             players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1
            
#             if len(players) == num_required:
#                 break

#     return players, total_cost, club_count

# def get_top_15_players(data):
#     all_players = []
#     total_cost = 0
#     club_count = {}
    
#     # Define position requirements
#     position_requirements = {
#         'Goalkeeper': 2,
#         'Defender': 5,
#         'Midfielder': 5,
#         'Forward': 3
#     }
    
#     for position, num_required in position_requirements.items():
#         players, cost, clubs = get_top_players(data, position, num_required)
#         all_players.extend(players)
#         total_cost += cost
        
#         for club, count in clubs.items():
#             club_count[club] = club_count.get(club, 0) + count
            
#     # Ensure the budget constraint is met
#     if total_cost > 100:
#         print("Total cost exceeds 100, reducing players.")
#         all_players = all_players[:15]

#     selected_players_df = pd.DataFrame(all_players)

#     return selected_players_df

# def main():
#     # Load features data
#     data = pd.read_csv(features_path)

#     # Get top 15 players
#     top_15_players = get_top_15_players(data)

#     # Save the top 15 players to CSV
#     top_15_players.to_csv(top_15_players_path, index=False)
#     print(f"Top 15 players saved to {top_15_players_path}")

# if __name__ == "__main__":
#     main()



# 15 ota players dincha tara cost dherai gayooo

# import pandas as pd
# import os
# import joblib

# # Directories for features data and model
# features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
# model_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\models\trained_model.pkl"

# # Paths for features and output files
# features_path = os.path.join(features_dir, '2022-23_features.csv')
# top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')

# def get_top_players(data, position, num_required):
#     players = []
#     total_cost = 0
#     club_count = {}
    
#     # Filter players by position and sort by cost
#     position_data = data[data['position'] == position].sort_values(by='predicted_points', ascending=False)
    
#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']
        
#         if club_count.get(club, 0) < 3 and total_cost + cost <= 100:
#             players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1
            
#             if len(players) == num_required:
#                 break

#     return players, total_cost, club_count

# def get_top_15_players(data):
#     all_players = []
#     total_cost = 0
#     club_count = {}
    
#     # Define position requirements
#     position_requirements = {
#         'Goalkeeper': 2,
#         'Defender': 5,
#         'Midfielder': 5,
#         'Forward': 3
#     }
    
#     for position, num_required in position_requirements.items():
#         players, cost, clubs = get_top_players(data, position, num_required)
#         all_players.extend(players)
#         total_cost += cost
        
#         for club, count in clubs.items():
#             club_count[club] = club_count.get(club, 0) + count
            
#     # Ensure the budget constraint is met
#     if total_cost > 100:
#         print("Total cost exceeds 100, reducing players.")
#         all_players = all_players[:15]

#     selected_players_df = pd.DataFrame(all_players)

#     # Drop the 'predicted_points' column from the final output
#     selected_players_df = selected_players_df.drop(columns=['predicted_points'])

#     return selected_players_df

# def main():
#     # Load features data
#     data = pd.read_csv(features_path)

#     # Load the trained model
#     model = joblib.load(model_path)

#     # Predict points for each player
#     features = data[['cost']]
#     data['predicted_points'] = model.predict(features)

#     # Get top 15 players
#     top_15_players = get_top_15_players(data)

#     # Save the top 15 players to CSV
#     top_15_players.to_csv(top_15_players_path, index=False)
#     print(f"Top 15 players saved to {top_15_players_path}")

# if __name__ == "__main__":
#     main()




# ali ali milya cha

# import pandas as pd
# import os
# import joblib

# # Directories for features data and model
# features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
# model_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\models\trained_model.pkl"

# # Paths for features and output files
# features_path = os.path.join(features_dir, '2022-23_features.csv')
# top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')

# def get_top_players(data, position, num_required, remaining_budget, club_count):
#     players = []
#     total_cost = 0

#     # Filter players by position and sort by predicted points
#     position_data = data[data['position'] == position].sort_values(by='predicted_points', ascending=False)

#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']

#         if club_count.get(club, 0) < 3 and total_cost + cost <= remaining_budget:
#             players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1

#             if len(players) == num_required:
#                 break

#     return players, total_cost, club_count

# def get_top_15_players(data):
#     all_players = []
#     total_cost = 0
#     club_count = {}

#     # Define position requirements
#     position_requirements = {
#         'Goalkeeper': 2,
#         'Defender': 5,
#         'Midfielder': 5,
#         'Forward': 3
#     }

#     print("Starting initial selection...")
#     for position, num_required in position_requirements.items():
#         players, cost, club_count = get_top_players(data, position, num_required, 100 - total_cost, club_count)
#         all_players.extend(players)
#         total_cost += cost
#         print(f"Selected {len(players)} {position}s, total cost: {total_cost}, club count: {club_count}")

#     selected_players_df = pd.DataFrame(all_players)
#     print(f"Initial selection: {len(selected_players_df)} players, total cost: {total_cost}")

#     # Ensure we have 15 players
#     if len(selected_players_df) < 15:
#         remaining_budget = 100 - total_cost
#         remaining_players = data[~data.index.isin(selected_players_df.index)]
#         remaining_players = remaining_players.sort_values(by='cost')

#         print(f"Filling remaining slots with budget: {remaining_budget}")
#         for _, row in remaining_players.iterrows():
#             if len(selected_players_df) == 15:
#                 break
#             club = row['club_name']
#             cost = row['cost']

#             if club_count.get(club, 0) < 3 and total_cost + cost <= remaining_budget:
#                 selected_players_df = pd.concat([selected_players_df, pd.DataFrame([row])], ignore_index=True)
#                 total_cost += cost
#                 club_count[club] = club_count.get(club, 0) + 1

#         print(f"Filled selection: {len(selected_players_df)} players, total cost: {total_cost}")

#     # If total cost exceeds 100, remove the most expensive players until within budget
#     while total_cost > 100:
#         selected_players_df = selected_players_df.sort_values(by='cost', ascending=False)
#         most_expensive = selected_players_df.iloc[0]
#         selected_players_df = selected_players_df.iloc[1:]
#         total_cost -= most_expensive['cost']
#         print(f"Removed most expensive player. New total cost: {total_cost}")

#     # Drop the 'predicted_points' column from the final output
#     if 'predicted_points' in selected_players_df.columns:
#         selected_players_df = selected_players_df.drop(columns=['predicted_points'])

#     print(f"Final selection: {len(selected_players_df)} players, total cost: {total_cost}")

#     return selected_players_df, club_count, total_cost

# def main():
#     # Load features data
#     data = pd.read_csv(features_path)

#     # Load the trained model
#     model = joblib.load(model_path)

#     # Predict points for each player
#     features = data[['cost']]
#     data['predicted_points'] = model.predict(features)

#     # Get top 15 players
#     top_15_players, club_count, total_cost = get_top_15_players(data)

#     # Ensure exactly 15 players
#     if len(top_15_players) != 15:
#         print(f"Initial selection has {len(top_15_players)} players. Filling up to 15.")
#         # Fill remaining slots with cheapest players
#         remaining_budget = 100 - total_cost
#         remaining_players = data[~data.index.isin(top_15_players.index)]
#         remaining_players = remaining_players.sort_values(by='cost')

#         for _, row in remaining_players.iterrows():
#             if len(top_15_players) == 15:
#                 break
#             club = row['club_name']
#             cost = row['cost']

#             if club_count.get(club, 0) < 3 and top_15_players['cost'].sum() + cost <= 100:
#                 top_15_players = pd.concat([top_15_players, pd.DataFrame([row])], ignore_index=True)
#                 club_count[club] = club_count.get(club, 0) + 1

#         print(f"Filled selection has {len(top_15_players)} players. Total cost: {top_15_players['cost'].sum()}")

#     if len(top_15_players) != 15:
#         print(f"Could not select 15 players within the budget. Trying to fill with cheapest remaining players.")
#         # If still not 15 players, add the cheapest remaining players without considering budget
#         remaining_players = data[~data.index.isin(top_15_players.index)]
#         remaining_players = remaining_players.sort_values(by='cost')

#         for _, row in remaining_players.iterrows():
#             if len(top_15_players) == 15:
#                 break
#             club = row['club_name']
#             if club_count.get(club, 0) < 3:
#                 top_15_players = pd.concat([top_15_players, pd.DataFrame([row])], ignore_index=True)
#                 club_count[club] = club_count.get(club, 0) + 1

#         print(f"Final attempt selection has {len(top_15_players)} players. Total cost: {top_15_players['cost'].sum()}")

#     if len(top_15_players) != 15:
#         raise ValueError(f"Selected players count is {len(top_15_players)}, expected 15")

#     # Save the top 15 players to CSV
#     top_15_players.to_csv(top_15_players_path, index=False)
#     print(f"Top 15 players saved to {top_15_players_path}")

# if __name__ == "__main__":
#     main()



# import pandas as pd
# import os
# import joblib

# # Directories for features data and model
# features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
# model_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\models\trained_model.pkl"

# # Paths for features and output files
# features_path = os.path.join(features_dir, '2022-23_features.csv')
# top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')

# def get_top_players(data, position, num_required, remaining_budget, club_count):
#     players = []
#     total_cost = 0

#     # Filter players by position and sort by predicted points
#     position_data = data[data['position'] == position].sort_values(by='predicted_points', ascending=False)

#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']

#         if club_count.get(club, 0) < 3 and total_cost + cost <= remaining_budget:
#             players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1

#             if len(players) == num_required:
#                 break

#     return players, total_cost, club_count

# def get_low_budget_players(data, position, num_required, remaining_budget, club_count):
#     players = []
#     total_cost = 0

#     # Filter players by position and sort by cost
#     position_data = data[data['position'] == position].sort_values(by='cost')

#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']

#         if club_count.get(club, 0) < 3 and total_cost + cost <= remaining_budget:
#             players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1

#             if len(players) == num_required:
#                 break

#     return players, total_cost, club_count

# def get_top_15_players(data):
#     high_budget_players = []
#     low_budget_players = []
#     total_cost = 0
#     club_count = {}

#     # Define position requirements
#     position_requirements = {
#         'Goalkeeper': 2,
#         'Defender': 5,
#         'Midfielder': 5,
#         'Forward': 3
#     }

#     # Select high budget players
#     print("Selecting high budget players...")
#     high_budget_count = 8
#     for position, num_required in position_requirements.items():
#         high_budget_num_required = min(num_required, high_budget_count)
#         players, cost, club_count = get_top_players(data, position, high_budget_num_required, 100 - total_cost, club_count)
#         high_budget_players.extend(players)
#         total_cost += cost
#         high_budget_count -= len(players)
#         print(f"Selected {len(players)} {position}s, total cost: {total_cost}, club count: {club_count}")

#     # Select low budget players
#     print("Filling remaining slots with low budget players...")
#     remaining_budget = 100 - total_cost
#     for position, num_required in position_requirements.items():
#         low_budget_num_required = num_required - len([p for p in high_budget_players if p['position'] == position])
#         players, cost, club_count = get_low_budget_players(data, position, low_budget_num_required, remaining_budget, club_count)
#         low_budget_players.extend(players)
#         total_cost += cost
#         remaining_budget = 100 - total_cost
#         print(f"Selected {len(players)} {position}s, total cost: {total_cost}, club count: {club_count}")

#     all_players = high_budget_players + low_budget_players
#     selected_players_df = pd.DataFrame(all_players)

#     # Ensure we have exactly 15 players
#     if len(selected_players_df) < 15:
#         remaining_budget = 100 - total_cost
#         remaining_players = data[~data.index.isin(selected_players_df.index)]
#         remaining_players = remaining_players.sort_values(by='cost')

#         print(f"Filling remaining slots with budget: {remaining_budget}")
#         for position, num_required in position_requirements.items():
#             current_count = len(selected_players_df[selected_players_df['position'] == position])
#             if current_count < num_required:
#                 players, cost, club_count = get_low_budget_players(remaining_players, position, num_required - current_count, remaining_budget, club_count)
#                 selected_players_df = pd.concat([selected_players_df, pd.DataFrame(players)], ignore_index=True)
#                 total_cost += cost
#                 remaining_budget = 100 - total_cost
#                 remaining_players = data[~data.index.isin(selected_players_df.index)]
#                 remaining_players = remaining_players.sort_values(by='cost')

#         print(f"Filled selection: {len(selected_players_df)} players, total cost: {total_cost}")

#     # Drop the 'predicted_points' column from the final output
#     if 'predicted_points' in selected_players_df.columns:
#         selected_players_df = selected_players_df.drop(columns=['predicted_points'])

#     print(f"Final selection: {len(selected_players_df)} players, total cost: {total_cost}")

#     return selected_players_df, club_count, total_cost

# def main():
#     # Load features data
#     data = pd.read_csv(features_path)

#     # Load the trained model
#     model = joblib.load(model_path)

#     # Predict points for each player
#     features = data[['cost']]
#     data['predicted_points'] = model.predict(features)

#     # Get top 15 players
#     top_15_players, club_count, total_cost = get_top_15_players(data)

#     # Ensure exactly 15 players
#     if len(top_15_players) != 15:
#         print(f"Initial selection has {len(top_15_players)} players. Filling up to 15.")
#         # Fill remaining slots with cheapest players
#         remaining_budget = 100 - total_cost
#         remaining_players = data[~data.index.isin(top_15_players.index)]
#         remaining_players = remaining_players.sort_values(by='cost')

#         for _, row in remaining_players.iterrows():
#             if len(top_15_players) == 15:
#                 break
#             club = row['club_name']
#             cost = row['cost']

#             if club_count.get(club, 0) < 3 and top_15_players['cost'].sum() + cost <= 100:
#                 top_15_players = pd.concat([top_15_players, pd.DataFrame([row])], ignore_index=True)
#                 club_count[club] = club_count.get(club, 0) + 1

#         print(f"Filled selection has {len(top_15_players)} players. Total cost: {top_15_players['cost'].sum()}")

#     if len(top_15_players) != 15:
#         print(f"Could not select 15 players within the budget. Trying to fill with cheapest remaining players.")
#         # If still not 15 players, add the cheapest remaining players without considering budget
#         remaining_players = data[~data.index.isin(top_15_players.index)]
#         remaining_players = remaining_players.sort_values(by='cost')

#         for _, row in remaining_players.iterrows():
#             if len(top_15_players) == 15:
#                 break
#             club = row['club_name']
#             if club_count.get(club, 0) < 3:
#                 top_15_players = pd.concat([top_15_players, pd.DataFrame([row])], ignore_index=True)
#                 club_count[club] = club_count.get(club, 0) + 1

#         print(f"Final attempt selection has {len(top_15_players)} players. Total cost: {top_15_players['cost'].sum()}")

#     if len(top_15_players) != 15:
#         raise ValueError(f"Selected players count is {len(top_15_players)}, expected 15")

#     # Save the top 15 players to CSV
#     top_15_players.to_csv(top_15_players_path, index=False)
#     print(f"Top 15 players saved to {top_15_players_path}")

# if __name__ == "__main__":
#     main()




# import pandas as pd
# import os
# import joblib

# # Define paths
# features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
# model_path = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\models\trained_model.pkl"
# features_path = os.path.join(features_dir, '2022-23_features.csv')
# top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')

# def select_players(data, position, num_required, club_count, total_cost, max_budget, sort_by='predicted_points'):
#     selected_players = []
#     position_data = data[data['position'] == position].sort_values(by=sort_by, ascending=(sort_by != 'predicted_points'))
    
#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']
        
#         if club_count.get(club, 0) < 3 and total_cost + cost <= max_budget:
#             selected_players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1
            
#             if len(selected_players) == num_required:
#                 break

#     return selected_players, total_cost, club_count

# def main():
#     # Load data and model
#     data = pd.read_csv(features_path)
#     model = joblib.load(model_path)

#     # Predict points
#     features = data[['cost']]
#     data['predicted_points'] = model.predict(features)

#     # Initialize parameters
#     max_budget = 100
#     total_cost = 0
#     club_count = {}
#     top_15_players = []

#     # Configuration for player selection
#     setup = [
#         ('Goalkeeper', 2), ('Defender', 5), ('Midfielder', 5), ('Forward', 3)
#     ]

#     for position, num_required in setup:
#         selected_players, total_cost, club_count = select_players(data, position, num_required, club_count, total_cost, max_budget)
#         top_15_players.extend(selected_players)

#     selected_players_df = pd.DataFrame(top_15_players)
#     selected_players_df = selected_players_df.drop(columns=['predicted_points'])

#     # Ensure total cost is within budget
#     while selected_players_df['cost'].sum() > max_budget:
#         most_expensive = selected_players_df[selected_players_df['cost'] == selected_players_df['cost'].max()].iloc[0]
#         replacement_candidates = data[(data['cost'] <= most_expensive['cost']) & (~data.index.isin(selected_players_df.index))]
#         replacement = replacement_candidates.nlargest(1, 'predicted_points')
#         selected_players_df = selected_players_df[selected_players_df.index != most_expensive.name].append(replacement, ignore_index=True)

#     # Save to CSV
#     selected_players_df.to_csv(top_15_players_path, index=False)
#     print(f"Top 15 players saved to {top_15_players_path}")

# if __name__ == "__main__":
#     main()

# import pandas as pd
# import os

# # Define paths
# features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
# features_path = os.path.join(features_dir, '2022-23_features.csv')
# top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')

# def get_top_players(data, position, num_required):
#     players = []
#     total_cost = 0
#     club_count = {}
    
#     # Sort players by cost (descending to assume higher cost means better performance)
#     position_data = data[data['position'] == position].sort_values(by='cost', ascending=False)
    
#     for _, row in position_data.iterrows():
#         club = row['club_name']
#         cost = row['cost']
        
#         if club_count.get(club, 0) < 3 and total_cost + cost <= 100:
#             players.append(row)
#             total_cost += cost
#             club_count[club] = club_count.get(club, 0) + 1
            
#             if len(players) == num_required:
#                 break

#     return players, total_cost, club_count

# def get_top_15_players(data):
#     all_players = []
#     total_cost = 0
#     club_count = {}
    
#     # Define position requirements
#     position_requirements = {
#         'Goalkeeper': 2,
#         'Defender': 5,
#         'Midfielder': 5,
#         'Forward': 3
#     }
    
#     for position, num_required in position_requirements.items():
#         players, cost, clubs = get_top_players(data, position, num_required)
#         all_players.extend(players)
#         total_cost += cost
        
#         for club, count in clubs.items():
#             club_count[club] = club_count.get(club, 0) + count

#     # Ensure the budget constraint is met
#     if total_cost > 100:
#         print("Total cost exceeds 100, reducing players.")
#         all_players = all_players[:15]  # Simple cut-off, not optimal

#     selected_players_df = pd.DataFrame(all_players)
#     return selected_players_df

# def main():
#     # Load features data
#     data = pd.read_csv(features_path)

#     # Get top 15 players
#     top_15_players = get_top_15_players(data)

#     # Save the top 15 players to CSV
#     top_15_players.to_csv(top_15_players_path, index=False)
#     print(f"Top 15 players saved to {top_15_players_path}")

# if __name__ == "__main__":
#     main()



import pandas as pd
import os

# Define paths
features_dir = r"C:\Users\Upama Raut\OneDrive\Desktop\THesis Final\data\features"
features_path = os.path.join(features_dir, '2022-23_features.csv')
top_15_players_path = os.path.join(features_dir, 'top_15_players.csv')
best_XI_path = os.path.join(features_dir, 'best_XI.csv')

def get_top_players(data, position, num_required):
    players = []
    total_cost = 0
    club_count = {}
    
    position_data = data[data['position'] == position].sort_values(by='cost', ascending=False)
    
    for _, row in position_data.iterrows():
        club = row['club_name']
        cost = row['cost']
        
        if club_count.get(club, 0) < 3 and total_cost + cost <= 100:
            players.append(row.to_dict())  # Ensure row is appended as a dictionary
            total_cost += cost
            club_count[club] = club_count.get(club, 0) + 1
            
            if len(players) == num_required:
                break

    return players, total_cost, club_count

def get_top_15_players(data):
    all_players = []
    total_cost = 0
    club_count = {}
    
    position_requirements = {
        'Goalkeeper': 2,
        'Defender': 5,
        'Midfielder': 5,
        'Forward': 3
    }
    
    for position, num_required in position_requirements.items():
        players, cost, clubs = get_top_players(data, position, num_required)
        all_players.extend(players)
        total_cost += cost
        
        for club, count in clubs.items():
            club_count[club] = club_count.get(club, 0) + count

    if total_cost > 100:
        print("Total cost exceeds 100, reducing players.")
        all_players = sorted(all_players, key=lambda x: x['cost'], reverse=True)[:15]

    return pd.DataFrame(all_players)

def select_best_XI(data):
    formation = {'Goalkeeper': 1, 'Defender': 4, 'Midfielder': 4, 'Forward': 2}
    best_XI = []
    
    for position, required_count in formation.items():
        position_players = data[data['position'] == position][:required_count]
        best_XI.append(position_players)
    
    return pd.concat(best_XI)

def main():
    data = pd.read_csv(features_path)
    
    if data.empty:
        print("No data loaded. Please check your CSV file.")
        return
    
    top_15_players = get_top_15_players(data)
    top_15_players.to_csv(top_15_players_path, index=False)
    print(f"Top 15 players saved to {top_15_players_path}")

    best_XI = select_best_XI(top_15_players)
    best_XI.to_csv(best_XI_path, index=False)
    print(f"Best XI players saved to {best_XI_path}")

if __name__ == "__main__":
    main()
