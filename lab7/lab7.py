"""
Arman Arya
Sep 28, 2026 - Monday
Lab 7: APIs and data collection
"""

import os
import pandas as pd
import requests
import matplotlib.pyplot as plt


# -------------------------
# 1. Example DataFrame
# -------------------------

dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}

df = pd.DataFrame(dict_)

print(df.head())
print(df.mean())


# -------------------------
# 2. Get NBA teams
# -------------------------

from static import get_teams

nba_teams = get_teams()

print(f"First 2 teams: {nba_teams[:2]}")

# convert list of dictionaries into a DataFrame
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())

# Filter the row that contains the 'Warriors' nickname
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']
print(df_warriors)

# access and save the id (first row, first column) of the Warriors
id_warriors = df_warriors[['id']].values[0][0]
print(f"Id of Warriors = {id_warriors}")


# -------------------------
# 3. Working with external API
# -------------------------

# a. Download the pickle file
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

# save the downloaded file as Golden_State.pkl
file_name = "Golden_State.pkl"

print("\nDownloading external data...")
response = requests.get(url)

if response.status_code == 200:
    with open(file_name, "wb") as f:
        f.write(response.content)
    print("Download complete")
else:
    print("Download failed")

# b. Load DataFrame from pickle
games = pd.read_pickle(file_name)
print("\nGames data from pickle file:")
print(games.head())

# c. Filter GSW vs Raptors
warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' vs. ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

# d. Calculate averages
home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"Warriors home average {home_avg_plus}")
print(f"Warriors away average {away_avg_plus}")
print(f"Warriors home points average {home_avg_pts}")
print(f"Warriors away points average {away_avg_pts}")

# e. Visualize
metrics = ['PLUS_MINUS', 'PTS']
home_values = [home_avg_plus, home_avg_pts]
away_values = [away_avg_plus, away_avg_pts]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width / 2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width / 2 for i in x], away_values, width=bar_width, label='Away', color='orange')
plt.xticks(x, metrics)
plt.title('Golden State Warriors vs. Raptors — Home vs Away Comparison')
plt.ylabel('Average Value')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)


print('\n--------------------- LAB EXERCISE ---------------------')
# Pick two teams to work on step a through e.
# Teams chosen: Arsenal vs Tottenham (English Premier League 2023/24)

# a. Download the CSV file
url = "https://datahub.io/core/english-premier-league/r/season-2324.csv"
file_name = "epl_matches.csv"

print("\nDownloading external data...")
try:
    response = requests.get(url, timeout=15)
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
        print("Download complete")
    else:
        print("Download failed - using local file if available")
except requests.RequestException:
    print("Download failed - using local file if available")

if not os.path.exists(file_name):
    raise SystemExit(f"{file_name} not found. Place the CSV in this folder.")

# b. Load DataFrame from CSV
matches = pd.read_csv(file_name)
print("\nMatches data from CSV file:")
print(matches.head())

# c. Filter Arsenal vs Tottenham (home and away)
team, opp = "Arsenal", "Tottenham"
arsenal_vs_spurs = matches[
    ((matches['HomeTeam'] == team) & (matches['AwayTeam'] == opp)) |
    ((matches['HomeTeam'] == opp) & (matches['AwayTeam'] == team))
]
arsenal_home = arsenal_vs_spurs[arsenal_vs_spurs['HomeTeam'] == team]
arsenal_away = arsenal_vs_spurs[arsenal_vs_spurs['AwayTeam'] == team]

# d. Calculate averages
# Goal difference from Arsenal's point of view (like PLUS_MINUS in the NBA data)
home_avg_diff = (arsenal_home['FTHG'] - arsenal_home['FTAG']).mean()
away_avg_diff = (arsenal_away['FTAG'] - arsenal_away['FTHG']).mean()
home_avg_goals = arsenal_home['FTHG'].mean()
away_avg_goals = arsenal_away['FTAG'].mean()

print(f"Arsenal home average goal difference {home_avg_diff}")
print(f"Arsenal away average goal difference {away_avg_diff}")
print(f"Arsenal home goals average {home_avg_goals}")
print(f"Arsenal away goals average {away_avg_goals}")

# e. Visualize
metrics = ['Goal Difference', 'Goals Scored']
home_values = [home_avg_diff, home_avg_goals]
away_values = [away_avg_diff, away_avg_goals]

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width / 2 for i in x], home_values, width=bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width / 2 for i in x], away_values, width=bar_width, label='Away', color='orange')
plt.xticks(x, metrics)
plt.title('Arsenal vs. Tottenham — Home vs Away Comparison (2023/24)')
plt.ylabel('Average Value')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)