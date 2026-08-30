import pandas as pd
import matplotlib.pyplot as plt

#read the dataset
df = pd.read_csv("student_data.csv")

#convert height to numeric
df["Height(cm)"] = pd.to_numeric(
    df["Height(cm)"],
    errors="coerce"
)

#map states to regions
state_region = {
    #NORTH
    "Jammu and Kashmir": "N",
    "Ladakh": "N",
    "Himachal Pradesh": "N",
    "Punjab": "N",
    "Chandigarh": "N",
    "Haryana": "N",
    "Delhi": "N",
    "New Delhi": "N",
    "Uttarakhand": "N",
    "Uttar Pradesh": "N",
    "Rajasthan": "N",

    #EAST
    "Bihar": "E",
    "Jharkhand": "E",
    "Odisha": "E",
    "West Bengal": "E",
    "Sikkim": "E",
    "Assam": "E",
    "Arunachal Pradesh": "E",
    "Nagaland": "E",
    "Manipur": "E",
    "Mizoram": "E",
    "Tripura": "E",
    "Meghalaya": "E",

    #WEST
    "Gujarat": "W",
    "Maharashtra": "W",
    "Goa": "W",
    "Madhya Pradesh": "W",
    "Dadra and Nagar Haveli and Daman and Diu": "W",

    #SOUTH
    "Andhra Pradesh": "S",
    "Telangana": "S",
    "Karnataka": "S",
    "Kerala": "S",
    "Tamil Nadu": "S",
    "Puducherry": "S",
    "Pondicherry": "S",
    "Lakshadweep": "S",
    "Andaman and Nicobar Islands": "S"
}

#create region column
df["Region"] = df["State"].map(state_region)

#check for states that were not mapped
print("Unmapped states:")
print(df[df["Region"].isna()]["State"].unique())

#remove missing height/region values
df = df.dropna(
    subset=["Height(cm)", "Region"]
)

#display number of students in each region
print("\nNumber of students in each region:")
print(df["Region"].value_counts())

#arrange regions in N, E, W, S order
regions = ["N", "E", "W", "S"]

#extract height data for each region
height_data = [
    df[df["Region"] == region]["Height(cm)"]
    for region in regions
]

#create box plot
plt.figure(figsize=(8, 6))

plt.boxplot(
    height_data,
    labels=regions
)

plt.xlabel("Region")
plt.ylabel("Height (cm)")
plt.title(
    "Distribution of Heights Across N, E, W and S Regions"
)

plt.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

#save the plot
plt.savefig(
    "Q4_height_regions.png",
    dpi=300
)

#display the plot
plt.show()
