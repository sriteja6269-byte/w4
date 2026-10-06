import pandas as pd
import matplotlib.pyplot as plt

# Load the COVID-19 dataset
df = pd.read_csv("covid_data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Sort countries by total cases
top_5 = df.sort_values(
    by="total_cases",
    ascending=False
).head(5)

# Display top 5 countries
print("\nTop 5 Countries by Total COVID-19 Cases:")
print(top_5[["location", "total_cases"]].to_string(index=False))

# Create bar chart
plt.figure(figsize=(10, 6))

plt.bar(
    top_5["location"],
    top_5["total_cases"]
)

plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.title("Top 5 Countries by Total COVID-19 Cases")

plt.xticks(rotation=30)
plt.tight_layout()

plt.show()