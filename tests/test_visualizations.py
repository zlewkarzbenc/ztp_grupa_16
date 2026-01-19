from visualizations import *
import pytest
from compute_averages import *

@pytest.fixture
def monthly_df():
   monthly_df = pd.read_csv("monthly_average.csv")
   return monthly_df

@pytest.fixture
def data():
    data = pd.read_csv("all_data.csv")
    return data

def test_city_trends_run_without_err(monthly_df):
    fig = plot_city_trends(monthly_df)
    assert fig is not None

def test_heatmap_run_without_err(monthly_df):
    fig = heatmaps(monthly_df)
    assert fig is not None

def test_pm25_exceedance_run_without_err(data):
    counts = count_days_over_treshold(data)
    fig = plot_pm25_exceedance_bars(counts)
    assert fig is not None
