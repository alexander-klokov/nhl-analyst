import os
import pandas as pd

import metrics
from penguins_xg_config import AXIS_Y, SITUATION

from utils.fetch_nhl_data import fetch_nhl_data
from utils.generate_filename import generate_filename_team, generate_filename_teams_all
from utils.generate_url import generate_url_teams_all, generate_url_team
from utils.get_top_n_teams import get_top_n_teams

from utils.plot_bar import plot_bar_teams_scoring_efficiency
from utils.plot_table import plot_table_xg, plot_table_goals
from utils.plot_scatter import plot_scatter

from utils.get_metric_timeline import get_metric_timeline

url_teams_all = generate_url_teams_all()
file_teams_all = generate_filename_teams_all()


def init():

    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists('figs'):
        os.makedirs('figs')

    # fetch teams stats
    fetch_nhl_data(url_teams_all, file_teams_all)

    df = pd.read_csv(file_teams_all)
    df = df.drop_duplicates(subset=['team'])

    teams = df['team'].astype(str).values
    for team in teams:
        url_team = generate_url_team(team)
        filename_team = generate_filename_team(team)

        fetch_nhl_data(url_team, filename_team)


def get_top_n_by_xg():

    criterion = 'xGoalsFor'
    filename = 'figs/top_n_by_xg.png'
    n = 8

    df_top_n = get_top_n_teams(n, situation=SITUATION, criterion=criterion)
    df_top_n = df_top_n[['team', criterion]]
    df_top_n.insert(0, 'rank', range(1, n + 1))

    plot_table_xg(df_top_n, filename)
    

def get_top_n_by_goal():

    criterion = 'goalsFor'
    filename = 'figs/top_n_by_goal.png'
    n = 32

    df_top_n = get_top_n_teams(n, situation=SITUATION, criterion=criterion)
    df_top_n = df_top_n[['team', criterion]]
    df_top_n.insert(0, 'rank', range(1, n + 1))

    plot_table_goals(df_top_n, filename)


def get_metric_scoring_efficiency():
 
    # 'scoring efficiency' - the metric to calculate 
    scoring_efficiency_all = []
    n = 32 # for all teams

    # get top N teams
    df_top_n = get_top_n_teams(n, situation=SITUATION, criterion=AXIS_Y)
  
    # handle teams
    teams = df_top_n['team'].astype(str).values
    for team in teams:
        filename_team = generate_filename_team(team)

        df = pd.read_csv(filename_team)
        df = df[(df['season'] >= 2023) & (df['situation'] == SITUATION)]

        scoring_efficiency = metrics.scoring_efficiency(df)

        scoring_efficiency_all.append(scoring_efficiency)

    # 
    df_top_n['scoringEff'] = scoring_efficiency_all
    df_with_scoring_efficiency = df_top_n.sort_values(by='scoringEff', ascending=False)

    filename = 'figs/teams_scoring_efficiency.png'
    plot_bar_teams_scoring_efficiency(df_with_scoring_efficiency, filename)

def get_metric_timeline_leaders():
    filename = 'figs/timeline_leaders.png'
    teams = ['DET', 'VGK', 'VAN', 'PIT']
    get_metric_timeline(teams, filename)

def get_metric_timeline_wildcard():
    filename = 'figs/timeline_wildcard.png'
    teams = ['DET', 'TBL', 'WSH', 'NJD', 'PIT']
    get_metric_timeline(teams, filename)

def get_centroid():
    teams = ['PIT', 'VAN']

    for team in teams:
        filename_team = generate_filename_team(team)
        filename = f'figs/scatter_{team}.png'.lower()

        df = pd.read_csv(filename_team)
        df = df[(df['season'] >= 2023) & (df['situation'] == SITUATION)]

        plot_scatter(df, filename, team)

if __name__ == '__main__':
    init()
    get_top_n_by_xg()
    get_top_n_by_goal()
    get_metric_scoring_efficiency()
    get_centroid()
    get_metric_timeline_leaders()
    get_metric_timeline_wildcard()


