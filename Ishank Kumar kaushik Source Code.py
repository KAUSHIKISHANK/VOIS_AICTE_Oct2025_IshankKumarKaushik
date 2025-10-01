import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_excel("Airbnb.xlsx", sheet_name="in")

# Basic Info
print("Shape:", df.shape)
print(df.head())
print(df.info())

# Clean data
df = df.drop_duplicates()
df['reviews per month'] = df['reviews per month'].fillna(0)

# --- 1. Aggregates ---
print("Min Price:", df['price'].min())
print("Max Price:", df['price'].max())
print("Average Price:", df['price'].mean())
print("Total Listings:", df['id'].nunique())

# --- 2. Group Analysis ---
# Avg price by neighbourhood group (like Manhattan, Brooklyn etc.)
avg_price_group = df.groupby('neighbourhood group')['price'].mean().sort_values(ascending=False)
print(avg_price_group)

# Room type distribution
room_types = df['room type'].value_counts()
print(room_types)

# --- 3. Visualizations ---
# Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['price'], bins=50, kde=True)
plt.xlim(0, 500)   # limit extreme values
plt.title("Price Distribution of Airbnb Listings")
plt.show()

# Avg Price per Neighbourhood Group
plt.figure(figsize=(8,5))
avg_price_group.plot(kind='bar', color='skyblue')
plt.title("Average Price per Neighbourhood Group")
plt.ylabel("Avg Price")
plt.show()

# Room Type Pie Chart
room_types.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Room Type Distribution")
plt.ylabel("")
plt.show()

# Top Hosts by Listings
plt.figure(figsize=(10,5))
df['host id'].value_counts().head(10).plot(kind='bar', color='orange')
plt.title("Top 10 Hosts by Number of Listings")
plt.xlabel("Host ID")
plt.ylabel("Number of Listings")
plt.show()
