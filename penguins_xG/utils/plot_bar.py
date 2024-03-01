import matplotlib.pyplot as plt

def plot_bar(df, filename, index_to_highlight):

    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["figure.figsize"] = (20,10)

    df = df.reset_index(drop=True)

    colors = ['blue'] * len(df)
    colors[index_to_highlight] = 'gray'

    df.plot(x='team', y='scoringEff', kind='bar', color=colors) 
    
    plt.legend().set_visible(False)
    plt.xlabel('Team', fontsize=16, fontweight='bold')
    plt.ylabel('Scoring Efficiency', fontsize=16, fontweight='bold')

    plt.grid(True)

    # save and display
    plt.savefig(filename, bbox_inches='tight')
    plt.show()


def plot_bar_teams_scoring_efficiency(df, filename):

    df = df.reset_index(drop=True)
    pit_row_index = df.loc[df['team'] == 'PIT'].index[0]

    plot_bar(df, filename, pit_row_index)