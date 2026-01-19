from visualizations import *
import pytest

@pytest.fixture
def monthly_df():
   monthly_df = pd.read_csv("monthly_average.csv")
   return monthly_df

def test_city_trends_run_without_err(monthly_df):
    fig, ax = plot_city_trends(monthly_df, cities=["Warszawa", "Katowice"], years=[2015, 2024], ylim=[0, 75])
    assert fig is not None

def test_heatmap_run_without_err(monthly_df):
    fig = heatmaps(monthly_df)
    assert fig is not None

def test_heatmap_if_every_location(monthly_df):
    fig = heatmaps(monthly_df)
    locations = [c for c in monthly_df.columns if c not in ["year", "month"]]
    assert len(fig.data) == len(locations)

def test_pm25_exceedance_run_without_err(monthly_df):
    fig = plot_pm25_exceedance_bars(monthly_df, top_n=3,  base_year=2024, threshold=15, figsize=(12, 6))
    assert fig is not None