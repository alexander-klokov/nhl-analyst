import os
import pandas as pd

import metrics
from penguins_xg_config import AXIS_Y

from utils.fetch_nhl_data import fetch_nhl_data
from utils.generate_filename import generate_filename_team, generate_filename_teams_all
from utils.generate_url import generate_url_teams_all, generate_url_team
from utils.get_top_n_teams import get_top_n_teams
from utils.plot_teams import plot_teams

url_teams_all = generate_url_teams_all()
file_teams_all = generate_filename_teams_all()

SITUATION='5on5'
NTOP = 32

def init():
    # fetch teams stats
    if not os.path.exists('data'):
        os.makedirs('data')
    fetch_nhl_data(url_teams_all, file_teams_all)

def get_metric_goal_rate():
 
    # 'goalRate' - the metric to calculate 
    goal_rates = []

    # get top N teams
    df_top_n = get_top_n_teams(NTOP, situation=SITUATION, criterion=AXIS_Y)
  
    # handle teams
    teams = df_top_n['team'].astype(str).values
    for team in teams:
        url_team = generate_url_team(team)
        filename_team = generate_filename_team(team)

        fetch_nhl_data(url_team, filename_team)

        df = pd.read_csv(filename_team)
        df = df[(df['season'] >= 2023) & (df['situation'] == SITUATION)]

        goal_rate = metrics.get_goal_rate(df)

        goal_rates.append(goal_rate)

    # 
    df_top_n['goalRate'] = goal_rates
    df_with_goal_rate = df_top_n.sort_values(by='goalRate', ascending=False)

    print(df_with_goal_rate)
    plot_teams(df_with_goal_rate)

if __name__ == '__main__':
    init()
    get_metric_goal_rate()


