import pandas as pd

# Sample data
data = [
    {"Date": "2023-08-11", "Home Team": "Burnley", "Away Team": "Manchester City", "Home Goals": 0, "Away Goals": 3, "Outcome": "Away Win"},
    {"Date": "2023-08-12", "Home Team": "Arsenal", "Away Team": "Nottingham Forest", "Home Goals": 2, "Away Goals": 1, "Outcome": "Home Win"},
    {"Date": "2023-08-12", "Home Team": "Bournemouth", "Away Team": "West Ham", "Home Goals": 1, "Away Goals": 1, "Outcome": "Draw"},
    {"Date": "2023-08-13", "Home Team": "Chelsea", "Away Team": "Liverpool", "Home Goals": 1, "Away Goals": 1, "Outcome": "Draw"},
    {"Date": "2023-08-14", "Home Team": "Manchester United", "Away Team": "Wolves", "Home Goals": 1, "Away Goals": 0, "Outcome": "Home Win"},
    {"Date": "2023-08-19", "Home Team": "Tottenham", "Away Team": "Brentford", "Home Goals": 2, "Away Goals": 2, "Outcome": "Draw"},
    {"Date": "2023-08-19", "Home Team": "Everton", "Away Team": "Fulham", "Home Goals": 0, "Away Goals": 1, "Outcome": "Away Win"},
    {"Date": "2023-08-20", "Home Team": "Aston Villa", "Away Team": "Newcastle", "Home Goals": 3, "Away Goals": 1, "Outcome": "Home Win"},
    {"Date": "2023-08-21", "Home Team": "Brighton", "Away Team": "Sheffield United", "Home Goals": 4, "Away Goals": 1, "Outcome": "Home Win"},
    {"Date": "2023-08-22", "Home Team": "Leicester", "Away Team": "Southampton", "Home Goals": 2, "Away Goals": 0, "Outcome": "Home Win"},
    {"Date": "2023-08-26", "Home Team": "Crystal Palace", "Away Team": "Burnley", "Home Goals": 1, "Away Goals": 2, "Outcome": "Away Win"},
    {"Date": "2023-08-26", "Home Team": "Manchester City", "Away Team": "Arsenal", "Home Goals": 3, "Away Goals": 2, "Outcome": "Home Win"},
    {"Date": "2023-08-27", "Home Team": "Liverpool", "Away Team": "Wolves", "Home Goals": 2, "Away Goals": 1, "Outcome": "Home Win"},
    {"Date": "2023-08-27", "Home Team": "Chelsea", "Away Team": "West Ham", "Home Goals": 1, "Away Goals": 0, "Outcome": "Home Win"},
    {"Date": "2023-08-28", "Home Team": "Leeds", "Away Team": "Nottingham Forest", "Home Goals": 0, "Away Goals": 1, "Outcome": "Away Win"},
    {"Date": "2023-09-02", "Home Team": "Fulham", "Away Team": "Tottenham", "Home Goals": 1, "Away Goals": 3, "Outcome": "Away Win"},
    {"Date": "2023-09-03", "Home Team": "Newcastle", "Away Team": "Brighton", "Home Goals": 2, "Away Goals": 2, "Outcome": "Draw"},
    {"Date": "2023-09-04", "Home Team": "Sheffield United", "Away Team": "Aston Villa", "Home Goals": 0, "Away Goals": 2, "Outcome": "Away Win"},
    {"Date": "2023-09-09", "Home Team": "West Ham", "Away Team": "Manchester United", "Home Goals": 1, "Away Goals": 1, "Outcome": "Draw"},
    {"Date": "2023-09-10", "Home Team": "Arsenal", "Away Team": "Chelsea", "Home Goals": 3, "Away Goals": 1, "Outcome": "Home Win"},
    {"Date": "2023-09-10", "Home Team": "Burnley", "Away Team": "Everton", "Home Goals": 0, "Away Goals": 1, "Outcome": "Away Win"},
    {"Date": "2023-09-11", "Home Team": "Wolves", "Away Team": "Leicester", "Home Goals": 2, "Away Goals": 2, "Outcome": "Draw"},
]


# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_filename = "premier_league_historical_data.csv"
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' created successfully!")
