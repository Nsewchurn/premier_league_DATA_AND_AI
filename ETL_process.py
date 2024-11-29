# Python script to perform the ETL (Extract, Transform, Load) process on the historical data.
# This will include loading the CSV, cleaning the data, 
# and transforming it into a format suitable for machine learning.

import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Extract - Load the data from the CSV file
def load_data(csv_filename):
    try:
        data = pd.read_csv(csv_filename)
        print(f"Data loaded successfully from {csv_filename}")
        return data
    except FileNotFoundError:
        print(f"Error: File {csv_filename} not found.")
        return None

# Step 2: Transform - Preprocess the data
def preprocess_data(data):
    # Drop rows with missing values
    data = data.dropna()

    # Map outcomes to numeric values for machine learning
    outcome_mapping = {"Home Win": 1, "Away Win": 2, "Draw": 0}
    data['Outcome'] = data['Outcome'].map(outcome_mapping)

    # Feature engineering (e.g., convert team names to categorical codes)
    data['Home Team'] = data['Home Team'].astype('category').cat.codes
    data['Away Team'] = data['Away Team'].astype('category').cat.codes

    # Extract features and labels
    features = data[['Home Team', 'Away Team', 'Home Goals', 'Away Goals']]
    labels = data['Outcome']

    return features, labels

# Step 3: Load - Split data into training and test sets
def split_data(features, labels):
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    print("Data split into training and test sets.")
    return X_train, X_test, y_train, y_test

# Main ETL workflow
def etl_workflow(csv_filename):
    # Extract
    data = load_data(csv_filename)
    if data is None:
        return None

    # Transform
    features, labels = preprocess_data(data)

    # Load
    X_train, X_test, y_train, y_test = split_data(features, labels)
    return X_train, X_test, y_train, y_test

# Run ETL process
csv_filename = "premier_league_historical_data.csv"
X_train, X_test, y_train, y_test = etl_workflow(csv_filename)

if X_train is not None:
    print("ETL process completed successfully.")
