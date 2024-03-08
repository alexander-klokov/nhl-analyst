AXIS_X = 'xGoalsFor'
AXIS_Y = 'goalsFor'

def scoring_efficiency(df):
    x = df[AXIS_X].to_numpy()
    y = df[AXIS_Y].to_numpy()
       
    points_above_line = sum(y > x)
    total_points = len(y)
    
    scoring_efficiency = points_above_line / total_points

    return round(scoring_efficiency, 2)

def centroid(df):
    x = df[AXIS_X].to_numpy()
    y = df[AXIS_Y].to_numpy()
    
    center_x = sum(x) / len(x)
    center_y = sum(y) / len(y)
    
    return (center_x, center_y)