import pandas as pd

import metrics
from pit_xg_config import AXIS_X, AXIS_Y

# goal rate 0.5
data_05 = {
    AXIS_X: [1.2, 2.1, 1.3, 2.5],
    AXIS_Y: [1, 3, 1, 3],
}

# goal rate 1.0
data_10 = {
    AXIS_X: [1, 3, 1, 3],
    AXIS_Y: [2, 4, 2, 5],
}

df_05 = pd.DataFrame(data_05)
df_10 = pd.DataFrame(data_10)


def test_goal_rate_05():
    assert metrics.get_goal_rate(df_05) == 0.5

def test_goal_rate_10():
    assert metrics.get_goal_rate(df_10) == 1.0