import matplotlib.pyplot as plt
import pandas as pd

import metrics

from utils.slice_df_for_analysis import slice_df_for_analysis
from utils.generate_filename import generate_filename_team

def get_metric_timeline(teams, filename):

    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["figure.figsize"] = (15,10)

    for team in teams:

        filename_team = generate_filename_team(team)

        df = pd.read_csv(filename_team)
        df = slice_df_for_analysis(df)

        rates = []

        for i in range(1, len(df) + 1):
            df_window = df[0:i]
            scoring_efficiency = metrics.scoring_efficiency(df_window)

            rates.append(scoring_efficiency)

        game_index = range(len(rates))
        plt.plot(game_index, rates, label=team, linewidth=4)

    plt.grid()
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Game Sequence', fontsize=18, fontweight='bold')
    plt.ylabel('Scoring Efficiency', fontsize=18, fontweight='bold')
    plt.legend(fontsize='x-large')
   
    # save and display
    plt.savefig(filename, bbox_inches='tight')
    plt.show()