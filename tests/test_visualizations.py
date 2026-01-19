from visualizations import heatmaps
import pytest
import pandas as pd


@pytest.fixture(scope="session")
def monthly_df():
   return pd.read_csv("monthly_average.csv")

def test_heatmap_run_without_err(monthly_df):
   fig = heatmaps(monthly_df)
   assert fig is not None
