from load_data import load_data
import pandas as pd

def test_load_data_returns_df():
    df = load_data()
    assert isinstance(df, pd.DataFrame)

def test_load_data_stations():
    df = load_data()

    if isinstance(df.columns, pd.MultiIndex):
        station = df.columns.get_level_values(1)
    else:
        station = df.columns

    assert len(station) > 0