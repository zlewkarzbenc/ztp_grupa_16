# wizualizacje

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from load_data import load_data
from compute_averages import monthly_average

def heatmaps():

    data = load_data()
    monthly = monthly_average(data)
    locations = monthly['location'].unique()
    zmin = monthly['pm25'].min()
    zmax = monthly['pm25'].max()
    years = [2015, 2018, 2019, 2024]

    n = len(locations)
    rows = int(np.ceil(n / 2))
    cols = 2

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f"{loc}" for loc in locations])
    colorscale = "Viridis"

    for i, loc in enumerate(locations):
        row = i // 2 + 1
        col = i % 2 + 1

        dfloc = monthly[(monthly['location'] == loc) & (monthly['year'].astype(int).isin(years))]

        heatmap_data = dfloc.pivot(index='year', columns='month', values='pm25')
        y = heatmap_data.index.astype(str)[::-1]

        showscale = True if i == 0 else False

        hm = go.Heatmap(z=heatmap_data.values[::-1, :], x=heatmap_data.columns, y=y,
                        colorscale=colorscale,
                        zmin=zmin, zmax=zmax,
                        colorbar=dict(title=dict(text="PM2.5 µg/m³"),
                                    tickmode="array",
                                    tickvals=np.linspace(zmin, zmax, 5),
                                    ticktext=[f"{v:.0f}" for v in np.linspace(zmin, zmax, 5)],
                                    len=0.2,
                                    y=0.7,
                                    x=1.05),
                        hovertemplate="Rok: %{y}<br>Miesiąc: %{x}<br>PM2.5: %{z} µg/m³",
                        showscale=showscale)

        fig.add_trace(hm, row=row, col=col)

    fig.update_xaxes(tickmode="array", tickvals=list(range(1, 13)), ticktext=list(range(1, 13)))

    for i in range(1, rows*cols + 1):
        fig.update_yaxes(title_text="Rok",
                        categoryorder='array',
                        categoryarray=[str(y) for y in years],
                        autorange="reversed",
                        row=(i-1) // 2 + 1,
                        col=(i-1) % 2 + 1)

    fig.update_layout(height=350 * rows, width=1000, title=dict(text='Średnie PM2.5 w latach 2015, 2018, 2021 i 2024', x=0.5, y=0.99), font=dict(size=12))

    fig.show()
