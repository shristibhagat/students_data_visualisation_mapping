import pandas as pd
import matplotlib.pyplot as plt

#read dataset
df = pd.read_csv("student_data.csv")

#display first few rows
print(df.head())

#display column names
print("\nColumn names:")
print(df.columns.tolist())

#convert height and weight to numeric
df["Height(cm)"] = pd.to_numeric(df["Height(cm)"], errors="coerce")
df["Weight(kg)"] = pd.to_numeric(df["Weight(kg)"], errors="coerce")

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
df = df.dropna(subset=["Height(cm)", "Weight(kg)", "Gender", "Quarter"])

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

quarters = ["Q1", "Q2", "Q3", "Q4"]

for ax, quarter in zip(axes.flatten(), quarters):

    quarter_data = df[df["Quarter"] == quarter]

    male = quarter_data[
        quarter_data["Gender"].str.lower() == "male"
    ]["Height(cm)"]

    female = quarter_data[
        quarter_data["Gender"].str.lower() == "female"
    ]["Height(cm)"]

    ax.hist(
        male,
        bins=8,
        alpha=0.5,
        label="Male"
    )

    ax.hist(
        female,
        bins=8,
        alpha=0.5,
        label="Female"
    )

    ax.set_title(f"{quarter} - Height")
    ax.set_xlabel("Height (cm)")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.suptitle("Quarter-Yearly Distribution of Heights by Gender", fontsize=15)
plt.tight_layout()

plt.savefig("Q2_height_histograms.png", dpi=300)

plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

for ax, quarter in zip(axes.flatten(), quarters):

    quarter_data = df[df["Quarter"] == quarter]

    male = quarter_data[
        quarter_data["Gender"].str.lower() == "male"
    ]["Weight(kg)"]

    female = quarter_data[
        quarter_data["Gender"].str.lower() == "female"
    ]["Weight(kg)"]

    ax.hist(
        male,
        bins=8,
        alpha=0.5,
        label="Male"
    )

    ax.hist(
        female,
        bins=8,
        alpha=0.5,
        label="Female"
    )

    ax.set_title(f"{quarter} - Weight")
    ax.set_xlabel("Weight (kg)")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.suptitle("Quarter-Yearly Distribution of Weights by Gender", fontsize=15)
plt.tight_layout()

#save the plot
plt.savefig("Q2_weight_histograms.png", dpi=300)

#display the plot
plt.show()
