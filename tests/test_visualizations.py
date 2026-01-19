from visualizations import *
import pytest
import pandas as pd


@pytest.fixture(scope="session")
def monthly_df():
   return pd.read_csv("monthly_average.csv")

def test_heatmap_run_without_err(monthly_df):
   fig = heatmaps(monthly_df)
   assert fig is not None

def test_city_trends_run_without_err(monthly_df, cities=["Warszawa", "Katowice"], years=[2015, 2024], ylim=[0, 75]):
   assert plot_city_trends(monthly_df, cities=["Warszawa", "Katowice"], years=[2015, 2024], ylim=[0, 75])) is not None
