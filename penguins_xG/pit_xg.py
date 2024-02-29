import os
import requests

import pandas as pd
import matplotlib.pyplot as plt

import metrics
from pit_xg_settings import AXIS_X, AXIS_Y, url_base, url_teams


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
    df_sorted = df_sorted[['team', 'xGoalsFor', 'goalsFor']].head(32)
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
 
    teams = df_top['team'].astype(str).values

    # fetch team stats
    for team in teams:
        url = url_base + team + '.csv'
        fetch_data(url, team + '.csv')

    goal_rates = []

    # plot team stats
    for team in teams:
       df = pd.read_csv(team + '.csv')
       df = df[(df['season'] >= 2023) & (df['situation'] == SITUATION)]

       goal_rate = metrics.get_goal_rate(df)

       goal_rates.append(goal_rate)

    df_top['goalRate'] = goal_rates
    df_top = df_top.sort_values(by='goalRate', ascending=False)

    colors = ['blue'] * len(df_top)
    highlight_index = -1
    colors[highlight_index] = 'black'

    df_top.plot(x='team', y='goalRate', kind='bar', color=colors, alpha=0.8) 
    
    plt.grid(True)
    plt.show()

    print(df_top)

if __name__ == '__main__':
    fetch_data(url_teams, 'teams.csv')
    get_top_by_xg()
    plot_goalsFor_vs_xg()


