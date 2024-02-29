import matplotlib.pyplot as plt

def plot_teams(df):
    colors = ['blue'] * len(df)
    highlight_index = -1
    colors[highlight_index] = 'black'

    df.plot(x='team', y='goalRate', kind='bar', color=colors, alpha=0.8) 
    
    plt.grid(True)
    plt.show()