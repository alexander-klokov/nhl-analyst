import seaborn as sns
import matplotlib.pyplot as plt

def plot_scatter(df, filename, title='', is_kde=False):

    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["figure.figsize"] = (10,10)

    sns.scatterplot(data=df, x='xGoalsFor', y='goalsFor', s=196, alpha=0.9)
    
    if is_kde:
        sns.kdeplot(data=df, x='xGoalsFor', y='goalsFor', cmap='viridis', fill=True, thresh=0, levels=10)

    range = [0, 5]
    plt.plot(range, range, color='white', linestyle='--', linewidth=3)
    plt.plot(range, range, color='black', linestyle='--')

    if not is_kde:
        plt.fill_between(range, range, 5, color='lightblue', alpha=0.4)
        plt.fill_between(range, range, 0, color='pink', alpha=0.4)

    plt.grid()
    plt.gca().set_aspect('equal')

    plt.xlabel('xG', fontsize=16, fontweight='bold')
    plt.ylabel('Goals For', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlim(0,5)
    plt.ylim(0,5)

    plt.title(title, fontsize=20, fontweight='bold')

    # save and display
    plt.savefig(filename, bbox_inches='tight')
    plt.show()
