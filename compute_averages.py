# liczenie średnich i wskazywanie dni z przekroczeniem normy
import pandas as pd

def monthly_average(data, metadata_idx=3):
    """
    Function used to compute monthly averages of PM2.5 concentration in Zad2.
    Averages over measurements in all stations for a given city in a given month (in a given year)
    Args:
        data (pandas.DataFrame): a dataframe of PM2.5 levels
        metadata_idx (int): index of the first non-metadata row in the `data` DataFrame

    Returns:
        result (pandas.DataFrame): a dataframe of average monthly PM2.5 in each city
    """
    # add "year" an "month" columns for downstream indexing
    dt = pd.to_datetime(
        data["Miejscowość"],
        format="%Y-%m-%d %H:%M:%S",
        errors="coerce"
    )

    data["year"] = dt.dt.year
    data["month"] = dt.dt.month

    ## prepare the "city" column
    meta_cols = {"Miejscowość", "year", "month"}
    station_cols = [c for c in data.columns if c not in meta_cols]

    # construct a dictionary for mapping stations to cities
    city_names = (
        pd.Series(station_cols)
        .str.replace(r"\.\d+$", "", regex=True) # this converts eg. "Kraków.1" to "Kraków"
    )

    station_to_city = dict(zip(station_cols, city_names))

    # drop metadata, then melt
    metadata_idx = 3
    no_metadata_df = data[metadata_idx:].drop("Miejscowość", axis=1)

    long = no_metadata_df.melt(id_vars=["year", "month"], value_vars=station_cols, var_name="station", value_name="pm2.5")

    # ensure all stations are assigned to a city
    long["city"] = long["station"].map(station_to_city)
    long.drop("station", axis=1, inplace=True)

    ## perform the actual aggregation
    long["pm2.5"] = pd.to_numeric(long["pm2.5"], errors="coerce")
    monthly_avg = long.groupby(["year", "month", "city"], as_index=False).mean(numeric_only=True)

    # pivot back to a readable, wide format
    result = (
        monthly_avg
        .pivot(
            index=["year", "month"],
            columns="city",
            values="pm2.5"
        )
        .sort_index()
    )

    # convert Multindex from float to int
    idx = result.index

    idx = idx.set_levels(
        idx.levels[idx.names.index("year")].astype(int),
        level="year"
    )

    idx = idx.set_levels(
        idx.levels[idx.names.index("month")].astype(int),
        level="month"
    )

    result.index = idx

    return result

def main():
    print("compute_averages module. This is only to be used through an import.")

if __name__ == "__main__":
    main()