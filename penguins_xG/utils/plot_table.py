import matplotlib.pyplot as plt

def plot_table(df, filename):
    
    _, ax = plt.subplots(figsize=(10, 15))
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
 
    plt.savefig(filename, bbox_inches='tight')
    plt.show()