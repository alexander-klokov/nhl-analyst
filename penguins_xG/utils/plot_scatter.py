import seaborn as sns
import matplotlib.pyplot as plt
import metrics

def plot_scatter(df, filename, title=''):

    plt.rcParams['font.family'] = 'Serif'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["figure.figsize"] = (10,10)

    # sns.scatterplot(data=df, x='xGoalsFor', y='goalsFor', hue='category', size='size_var', palette='viridis', sizes=(100, 500), alpha=0.8)
    sns.scatterplot(data=df, x='xGoalsFor', y='goalsFor', palette='viridis', s=196, alpha=0.9)

    sns.kdeplot(data=df, x='xGoalsFor', y='goalsFor', cmap='viridis', fill=True, thresh=0, levels=10)
    # centroid
    c = metrics.centroid(df)
    plt.scatter(c[0], c[1], color='red', s=100, label='Additional Point')

    range = [0, 5]
    plt.plot(range, range, color='white', linestyle='--', linewidth=3)
    plt.plot(range, range, color='black', linestyle='--')
    plt.grid()
    plt.gca().set_aspect('equal')

    plt.xlabel('xG', fontsize=16, fontweight='bold')
    plt.ylabel('Goals', fontsize=16, fontweight='bold')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlim(0,5)
    plt.ylim(0,5)

    plt.title(title, fontsize=20, fontweight='bold')

    # save and display
    plt.savefig(filename, bbox_inches='tight')
    plt.show()
