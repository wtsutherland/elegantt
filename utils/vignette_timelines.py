import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.dates as dt
import pandas as pd
import csv


data = pd.read_csv("timelines.csv")

data.Start = pd.to_datetime(data.Start, format="%Y")
data.End = pd.to_datetime(data.End, format="%Y")
data = data.loc[::-1]

fig, ax = plt.subplots(figsize=(8, 2.8))
ax.set_title('Test', fontsize=14)

ax = ax.xaxis_date()
ax = plt.hlines(data.Vignette, dt.date2num(data.Start), dt.date2num(data.End), linewidth=14, color="black")

plt.margins(0.02, 0.2)
fig.tight_layout(rect=[0, 0, 1, .80])
plt.show()
