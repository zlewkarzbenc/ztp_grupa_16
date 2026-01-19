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
    fig, ax = plot_city_trends(monthly_df, years=[2015, 2024])
    assert fig is not None

def test_city_trends_correct_data(monthly_df):
    ax = plot_city_trends(monthly_df, years=[2015, 2024])

    labels = [t.get_text() for t in ax.get_legend().get_texts()]
    lines = ax.get_lines()

    lines_map = {label: line for label, line in zip(labels, lines)}

    assert np.all(lines_map["Warszawa 2015"].get_ydata() == monthly_df.loc[2015, "Warszawa"].to_numpy())
    assert np.all(lines_map["Warszawa 2024"].get_ydata() == monthly_df.loc[2024, "Warszawa"].to_numpy())
    assert np.all(lines_map["Katowice 2015"].get_ydata() == monthly_df.loc[2015, "Katowice"].to_numpy())
    assert np.all(lines_map["Katowice 2024"].get_ydata() == monthly_df.loc[2024, "Katowice"].to_numpy())


def test_heatmap_run_without_err(monthly_df):
    fig = heatmaps(monthly_df)
    assert fig is not None

def test_heatmap_if_every_location(monthly_df):
    fig = heatmaps(monthly_df)
    locations = [c for c in monthly_df.columns if c not in ["year", "month"]]
    assert len(fig.data) == len(locations)

def test_pm25_exceedance_run_without_err(data):
    counts = count_days_over_treshold(data)
    fig = plot_pm25_exceedance_bars(counts)
    assert fig is not None

    assert heights == expected
