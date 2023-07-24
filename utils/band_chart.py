import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import pandas as pd
import csv

color_cats = { "group 1": "tab:blue", "group 2": "tab:orange", "group 3": "tab:purple", "group 4": "tab:pink" }

# Position-based color cats
# color_cats = { "faculty": "tab:blue", "???": "tab:orange", "ph.d. student": "tab:green", "undergraduate": "tab:red", "research scientist": "tab:purple", "research consultant": "tab:pink" }

def colors(cat):
    return color_cats[cat.lower()]

def data_eval(data):
    uniques = pd.unique(data["Position"])
    sizes = []
    for i in uniques:
        sizes.append(len(data.loc[data['Position'] == i]) + 1)

    return uniques, sizes

data = pd.read_csv("contributors.csv")

# fig, axs = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})

uniques, sizes = data_eval(data)
fig, axs = plt.subplots(len(uniques), 1, gridspec_kw={'height_ratios': sizes}, sharex=True)

axis_count = 0

for i in uniques:
    rows = data.loc[data['Position'] == i]

    axs[axis_count].title.set_text(i)
    axs[axis_count].title.set_size(8)

    height = 2
    y_labels = []
    no_entries = 0

    for index, row in rows.iterrows():

        if row["End"] - row["Start"] == 0:
            extent = (row["End"] - row["Start"]) + 1
        else:
            extent = row["End"] - row["Start"]

        #axs[axis_count].broken_barh([(row["Start"], extent)], (height, 4), facecolors=colors(row["Org"]), zorder=3)
        axs[axis_count].broken_barh([(row["Start"], extent)], (height, 4), zorder=3)

        height += 5
        no_entries += 1
        y_labels.append(row["Name"])

    yticks = range(4, (no_entries * 5) + 2, 5)

    axs[axis_count].set_ylim(0, (no_entries * 5) + 4)
    axs[axis_count].set_xlim(2007.5, 2021.5)
    axs[axis_count].set_yticks(list(yticks))
    axs[axis_count].set_yticklabels(y_labels)
    axs[axis_count].invert_yaxis()
    axs[axis_count].grid(axis='x')
    # ax.grid(True, zorder=0)
    plt.tight_layout()
    # ax.legend(ldata, y_labels)

    axis_count += 1

plt.show()
