import pandas as pd
import requests
import csv
import matplotlib.pyplot as plt
import os
import numpy as np

base_url = 'https://moneypuck.com/moneypuck/playerData/careers/gameByGame/regular/teams/'
url_teams = 'https://moneypuck.com/moneypuck/playerData/seasonSummary/2023/regular/teams.csv'

AXIS_X = 'xGoalsFor'
AXIS_Y = 'goalsFor'
SITUATION='5on5'


def fetch_data(url, fileName):

    if os.path.exists(fileName):
        print(f"skip fetch: {fileName}")
        return

    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse CSV data
        csv_data = response.text
    
        # Write CSV data to a file
        with open(fileName, 'w', newline='') as f:
            f.write(csv_data)
        
        print(f"Data has been fetched and written to {fileName}")
    else:
        print("Failed to fetch data. Status code:", response.status_code)

def get_top_by_xg():
    df = pd.read_csv('teams.csv')
    df = df[df['situation'] == SITUATION]
    df_sorted = df.sort_values(by='xGoalsFor', ascending=False)
    df_sorted = df_sorted[['team', 'xGoalsFor', 'goalsFor']].head(8)
    df_sorted.to_csv('top_8_by_xg.csv', index=False)

def get_proportion(df):
    x = df[AXIS_X].to_numpy()
    y = df[AXIS_Y].to_numpy()
       
    points_above_line = sum(y > x)
    total_points = len(y)
    proportion_above_line = points_above_line / total_points

    return round(proportion_above_line, 2)

def plot_goalsFor_vs_xg():
    df_top = pd.read_csv('top_8_by_xg.csv')
    df_top = df_top.sort_values(by='goalsFor', ascending=False)
    df_top.reset_index(drop=True, inplace=True)

    print(df_top)
    teams = ['DAL', 'COL', 'NJD', 'TOR', 'EDM', 'CAR', 'PIT', 'LAK']

    # fetch team stats
    for team in teams:
        url = base_url + team + '.csv'
        fetch_data(url, team + '.csv')

    proportions = []

    # plot team stats
    for team in teams:
       df = pd.read_csv(team + '.csv')
       df = df[(df['season'] >= 2023) & (df['situation'] == SITUATION)]

       proportion = get_proportion(df)

       print(team, ':', proportion)

       proportions.append(proportion)

    df_top['p'] = proportions
    df_top = df_top.sort_values(by='p', ascending=False)

    print(df_top)

if __name__ == '__main__':
    fetch_data(url_teams, 'teams.csv')
    get_top_by_xg()
    plot_goalsFor_vs_xg()


