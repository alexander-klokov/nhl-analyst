import pandas as pd

import penguins_xg_metrics
from penguins_xg_config import AXIS_X, AXIS_Y

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

data_line = {
    AXIS_X: [1, 2, 3, 4, 5],
    AXIS_Y: [1, 2, 3, 4, 5],
}

df_05 = pd.DataFrame(data_05)
df_10 = pd.DataFrame(data_10)
df_line = pd.DataFrame(data_line)


def test_scoring_efficiency_05():
    assert penguins_xg_metrics.scoring_efficiency(df_05) == 0.5

def test_scoring_efficiency_10():
    assert penguins_xg_metrics.scoring_efficiency(df_10) == 1.0

def test_centroid():
    assert penguins_xg_metrics.centroid(df_line) == (3, 3)
