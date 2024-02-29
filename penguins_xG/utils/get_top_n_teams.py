import pandas as pd

from utils.generate_filename import generate_filename_teams_all

def get_top_n_teams(ntop, situation, criterion):
    file_teams_all = generate_filename_teams_all()

    df = pd.read_csv(file_teams_all)
    df = df[df['situation'] == situation]

    df_sorted = df.sort_values(by=criterion, ascending=False)
    df_n_top = df_sorted.head(ntop)

    return df_n_top