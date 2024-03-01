import matplotlib.pyplot as plt

def plot_table(df, filename, index_to_highlight, label2=''):
    
    _, ax = plt.subplots(figsize=(8, 8))
    ax.axis('off')

    # make the table
    colLabels=['','Team', label2]
    plt.rcParams['font.family'] = 'Serif'
    table = plt.table(cellText=df.values.tolist(),
                      colLabels=colLabels,
                      cellLoc='center',
                      loc='center',
                      colColours=['gray'] * len(df.columns),
                      bbox=[0, 0, 1, 1])
    table.set_fontsize(24)

    for i in range(len(df.columns)):
        cell = table[index_to_highlight, i]
        cell.set_facecolor('lightgray')
        cell.set_text_props(weight='bold')

    # save and display
    plt.savefig(filename, bbox_inches='tight')
    plt.show()



def plot_table_xg(df, filename):
    
    df = df.reset_index(drop=True)
    df = df.drop(df.index[7:10])
    df = df.reset_index(drop=True)
    df = df.iloc[:-19]
    df = df.reset_index(drop=True)

    df['xGoalsFor'] = df['xGoalsFor'].round(1)

    pit_row_index = df.loc[df['team'] == 'PIT'].index[0] + 1

    plot_table(df, filename, pit_row_index, 'xG')


def plot_table_goals(df, filename):
    
    df = df.reset_index(drop=True)
    df = df.drop(df.index[7:24])
    df = df.reset_index(drop=True)
    df = df.iloc[:-5]
    df = df.reset_index(drop=True)
    df['goalsFor'] = df['goalsFor'].astype(int)

    pit_row_index = df.loc[df['team'] == 'PIT'].index[0] + 1

    plot_table(df, filename, pit_row_index, 'Goals For')