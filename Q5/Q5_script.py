import pandas as pd
import matplotlib.pyplot as plt

#read the dataset
df = pd.read_csv("student_data.csv")

#convert height and weight to numeric
df["Height(cm)"] = pd.to_numeric(
    df["Height(cm)"],
    errors="coerce"
)

df["Weight(kg)"] = pd.to_numeric(
    df["Weight(kg)"],
    errors="coerce"
)

#convert birth month to month number
month_number = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

df["Month_Number"] = df["Birth Month"].map(month_number)

#remove missing values
df = df.dropna(
    subset=["Height(cm)", "Weight(kg)", "Birth Month", "State"]
)

#assign a unique bubble size to each state
states = df["State"].unique()

state_sizes = {
    state: 50 + i * 20
    for i, state in enumerate(states)
}

df["State_Size"] = df["State"].map(state_sizes)

#create figure
plt.figure(figsize=(12, 8))

#create scatter plot
scatter = plt.scatter(
    df["Height(cm)"],
    df["Weight(kg)"],
    s=df["State_Size"],
    c=df["Month_Number"],
    cmap="viridis",
    alpha=0.7,
    edgecolors="black"
)

#axis labels and title
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height, Weight, Birth Month and State")

#add colour bar for birth month
cbar = plt.colorbar(scatter)
cbar.set_label("Birth Month")

cbar.set_ticks(range(1, 13))
cbar.set_ticklabels([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

#create legend for states
state_handles = []

for state in states:
    state_handles.append(
        plt.scatter(
            [],
            [],
            s=state_sizes[state],
            color="gray",
            edgecolors="black",
            alpha=0.7,
            label=state
        )
    )

plt.legend(
    handles=state_handles,
    title="State",
    bbox_to_anchor=(1.25, 1),
    loc="upper left",
    fontsize=8
)

#add grid
plt.grid(True, alpha=0.3)

plt.tight_layout()

#save the plot
plt.savefig(
    "Q5_height_weight_month_state.png",
    dpi=300,
    bbox_inches="tight"
)

#display the plot
plt.show()
