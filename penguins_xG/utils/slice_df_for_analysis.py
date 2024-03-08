from penguins_xg_config import SEASON, DATE_BY, SITUATION

def slice_df_for_analysis(df):

    return df[
        (df['season'] >= SEASON) &
        (df['gameDate'] <= DATE_BY) &
        (df['situation'] == SITUATION)
        ]
