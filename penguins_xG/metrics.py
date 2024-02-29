AXIS_X = 'xGoalsFor'
AXIS_Y = 'goalsFor'

def get_goal_rate(df):
    x = df[AXIS_X].to_numpy()
    y = df[AXIS_Y].to_numpy()
       
    points_above_line = sum(y > x)
    total_points = len(y)
    
    goal_rate = points_above_line / total_points

    return round(goal_rate, 2)