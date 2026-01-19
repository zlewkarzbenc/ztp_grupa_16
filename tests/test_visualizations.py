from visualizations import *
import pytest
from unittest.mock import patch
import matplotlib.pyplot as plt
import matplotlib

@pytest.fixture(scope="session")
def monthly_df():
   return pd.DataFrame({"year": [2015, 2018, 2021],
                        "month": [1, 2, 3],
                        "Warszawa": [1.3, 20, 30],
                        "Kraków": [4.2, 15, 3.1],
                        "Lublin": [3.4, 8.1, 1.2]})

def test_city_trends_run_without_err(monthly_df):
   with patch("matplotlib.pyplot.figure"):
      fig = plot_city_trends(monthly_df)
      assert fig is not None
      plt.close(fig)

def test_heatmap_run_without_err(monthly_df):
   with patch("matplotlib.pyplot.figure"):
      fig = heatmaps(monthly_df)
      assert fig is not None
      plt.close(fig)

def test_pm25_exceedance_run_without_err():
   with patch("matplotlib.pyplot.figure"):
      counts = pd.DataFrame({"count": [1, 2, 3]})
      fig = plot_pm25_exceedance_bars(counts)
      assert fig is not None
      plt.close(fig)
