import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read dataset
df = pd.read_csv("student_data.csv")

#convert height to numeric
df["Height(cm)"] = pd.to_numeric(df["Height(cm)"], errors="coerce")

#convert birth month to quarter
month_to_quarter = {
    "January": "Q1",
    "February": "Q1",
    "March": "Q1",
    "April": "Q2",
    "May": "Q2",
    "June": "Q2",
    "July": "Q3",
    "August": "Q3",
    "September": "Q3",
    "October": "Q4",
    "November": "Q4",
    "December": "Q4"
}

df["Quarter"] = df["Birth Month"].map(month_to_quarter)

#remove missing values
df = df.dropna(
    subset=["Height(cm)", "Quarter", "Roll Number"]
)

#arrange quarters in correct order
quarter_order = ["Q1", "Q2", "Q3", "Q4"]

df["Quarter"] = pd.Categorical(
    df["Quarter"],
    categories=quarter_order,
    ordered=True
)

df = df.sort_values("Quarter").reset_index(drop=True)

#number of students
N = len(df)

#angles for each student
angles = np.linspace(
    0,
    2 * np.pi,
    N,
    endpoint=False
)

#heights
heights = df["Height(cm)"].values

#ceate radial plot
fig, ax = plt.subplots(
    figsize=(10, 10),
    subplot_kw={"projection": "polar"}
)

#bar width
width = 2 * np.pi / N * 0.8

#create radial bars
ax.bar(
    angles,
    heights,
    width=width,
    alpha=0.7,
    edgecolor="black"
)

#add roll numbers around the circle
ax.set_xticks(angles)
ax.set_xticklabels(
    df["Roll Number"],
    fontsize=8
)

#start from the top
ax.set_theta_offset(np.pi / 2)

#clockwise direction
ax.set_theta_direction(-1)

#title
ax.set_title(
    "Radial Bar Plot of Heights Across Birth Quarters",
    pad=30,
    fontsize=15
)

#add quarter labels
for quarter in quarter_order:

    quarter_data = df[df["Quarter"] == quarter]

    if len(quarter_data) > 0:

        first_index = quarter_data.index[0]
        last_index = quarter_data.index[-1]

        middle_index = (first_index + last_index) / 2

        angle = angles[int(middle_index)]

        ax.text(
            angle,
            max(heights) + 8,
            quarter,
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold"
        )

#save the figure
plt.savefig(
    "Q3_radial_height_plot.png",
    dpi=300,
    bbox_inches="tight"
)

#display the plot
plt.show()
