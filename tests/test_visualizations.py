from visualizations import heatmaps
import pytest
import pandas as pd


@pytest.fixture(scope="session")
def monthly_df():
   return pd.DataFrame({"year": [2015, 2018, 2021],
                        "month": [1, 2, 3],
                        "Warszawa": [1.3, 20, 30],
                        "Kraków": [4.2, 15, 3.1],
                        "Lublin": [3.4, 8.1, 1.2]})

def test_heatmap_run_without_err(monthly_df):
   fig = heatmaps(monthly_df)
   assert fig is not None
