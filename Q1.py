import pandas as pd
import matplotlib.pyplot as plt

#read dataset
df = pd.read_csv("student_data.csv")

#display first 5 rows
print(df.head())

#display column names
print("\nColumn names:")
print(df.columns.tolist())

#correct column names
height_col = "Height(cm)"
weight_col = "Weight(kg)"
gender_col = "Gender"

#convert height and weight to numeric
df[height_col] = pd.to_numeric(df[height_col], errors="coerce")
df[weight_col] = pd.to_numeric(df[weight_col], errors="coerce")

#remove missing values
df = df.dropna(subset=[height_col, weight_col, gender_col])

#convert height from cm to metres
df["Height(m)"] = df[height_col] / 100

#calculate height squared in m²
df["Height²(m²)"] = df["Height(m)"] ** 2

#calculate BMI
df["BMI"] = df[weight_col] / df["Height²(m²)"]

#create scatter plot
plt.figure(figsize=(8, 6))

#plot separately for each gender
for gender in df[gender_col].unique():
    subset = df[df[gender_col] == gender]

    plt.scatter(
        subset["Height²(m²)"],
        subset[weight_col],
        label=gender
    )

#labels and title
plt.xlabel("Height² (m²)")
plt.ylabel("Weight (kg)")
plt.title("Scatter Plot of Weight vs Height² by Gender")

#legend and grid
plt.legend(title="Gender")
plt.grid(True, alpha=0.3)

plt.tight_layout()

#save the plot
plt.savefig("Q1_BMI_scatter.png", dpi=300)

#display the plot
plt.show()
