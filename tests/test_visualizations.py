from visualizations import *
import pytest
import pandas as pd


@pytest.fixture(scope="session")
def monthly_df():
   return pd.DataFrame({"year": [2015, 2018, 2021, 2024],
                       "month": [1, 2, 3, 4],
                       "Warszawa": [1.3, 20, 30, 5],
                        "Katowice": [4.2, 15, 3.1, 10],
                        "Lublin": [3.4, 8.1, 1.2, 2]})

def test_heatmap_run_without_err(monthly_df):
   fig = heatmaps(monthly_df)
   assert fig is not None

def test_city_trends_run_without_err(monthly_df):
   fig = plot_city_trends(monthly_df, cities=["Warszawa", "Katowice"], years=[2015, 2018], ylim=[0, 75])
   assert fig is not None
