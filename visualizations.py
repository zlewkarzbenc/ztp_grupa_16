# wizualizacje
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_city_pm25_trends(monthly_df, cities=["Warszawa", "Katowice"], years=[2015, 2024], ylim=[0, 75]):
    """
    Plot monthly PM2.5 trends for selected cities and years.

    Args:
        result (pd.DataFrame): DataFrame with MultiIndex (year, month) and cities as columns.
        cities (list[str]): Cities to include in the plot.
        years (list[int]): Years to include in the plot.
        ylim (list[int]): Y-axis limits.

    Returns:
        ax (matplotlib.axes.Axes): the desired lineplot to be shown in Zad2
    """

    # data preparation
    df = monthly_df.loc[years, cities].reset_index()

    df_long = df.melt(
        id_vars=["year", "month"],
        var_name="city",
        value_name="pm25"
    )

    df_long["series"] = (
        df_long["city"] + " " + df_long["year"].astype(str)
    )

    # coloring
    palette = sns.color_palette("coolwarm", 4)

    city_colors = {
        cities[0]: palette[:2][::-1], # reverse the pallete here for more consistent coloring (darker lines for later years)
        cities[1]: palette[2:],
    }

    year_order = sorted(years)
    color_map = {
        f"{city} {year}": city_colors[city][i]
        for city in cities
        for i, year in enumerate(year_order)
    }

    # plotting
    fig, ax = plt.subplots(figsize=(12, 6))

    sns.lineplot(
        data=df_long,
        x="month",
        y="pm25",
        hue="series",
        palette=color_map,
        marker="o",
        alpha=0.85,
        ax=ax,
    )

    ax.set_title(f"Wykres stężenia PM2.5 (µg/m³) w {cities[0]} i {cities[-1]} w latach {years[0]} oraz {years[-1]}", fontsize=13)
    ax.set_xlabel("Miesiąc")
    ax.set_ylabel("PM2.5 (µg/m³)")
    ax.set_xlim(1, 12)
    ax.set_ylim(*ylim)

    ax.set_xticks(range(1,13))
    ax.grid(alpha=0.4)

    ax.legend(title="", frameon=False)
    fig.tight_layout()

    return ax

def main():
    print("visualizations module. This is only to be used through an import.")

if __name__ == "__main__":
    main()