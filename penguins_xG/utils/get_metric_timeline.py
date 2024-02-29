import matplotlib.pyplot as plt
import pandas as pd

import metrics

from utils.generate_filename import generate_filename_team

SITUATION='5on5'

def get_metric_timeline(teams):

    for team in teams:

        filename_team = generate_filename_team(team)

        df = pd.read_csv(filename_team)
        df = df[(df['season'] >= 2023) & (df['situation'] == SITUATION)]

        rates = []

        for i in range(1, len(df) + 1):
            df_window = df[0:i]
            goal_rate = metrics.get_goal_rate(df_window)

            rates.append(goal_rate)

        game_index = range(len(rates))
        plt.plot(game_index, rates, label=team)

    plt.grid()
    plt.xlabel('game number')
    plt.ylabel('goal rate')
    plt.legend()
    plt.show()