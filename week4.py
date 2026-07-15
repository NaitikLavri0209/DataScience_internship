import pandas as pd
import matplotlib.pyplot as plt

# FIXED: Added encoding to prevent UnicodeDecodeError
df = pd.read_csv("Sample - Superstore.csv", encoding='cp1252')

print("First 5 Records")
print(df.head())

print("\nShape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nInformation")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

df = df.drop_duplicates()

# IMPROVED: Added dayfirst=False to match standard Superstore USA date formats
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=False)

print("\nSummary")
print(df.describe())

print("\nTotal Sales")
print(round(df["Sales"].sum(), 2))

print("\nTotal Profit")
print(round(df["Profit"].sum(), 2))

print("\nAverage Sales")
print(round(df["Sales"].mean(), 2))

print("\nAverage Profit")
print(round(df["Profit"].mean(), 2))

print("\nCategory Wise Sales")
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)

print("\nCategory Wise Profit")
category_profit = df.groupby("Category")["Profit"].sum()
print(category_profit)

print("\nTop 10 States by Sales")
state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)
print(state_sales.head(10))

print("\nTop 10 Customers")
customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False)
print(customers.head(10))

print("\nRegion Wise Sales")
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

print("\nSegment Wise Sales")
segment_sales = df.groupby("Segment")["Sales"].sum()
print(segment_sales)

print("\nMost Sold Sub Categories")
sub_category = df["Sub-Category"].value_counts()
print(sub_category.head(10))

# IMPROVED: Sort monthly sales chronologically (Jan -> Dec) instead of alphabetically
df["Month_Num"] = df["Order Date"].dt.month
monthly_sales = df.groupby(["Month_Num", df["Order Date"].dt.month_name()])["Sales"].sum().reset_index(level=0, drop=True)

plt.figure(figsize=(7, 5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
category_profit.plot(kind="bar")
plt.title("Category Wise Profit")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
state_sales.head(10).plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 6))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Region Wise Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
segment_sales.plot(kind="bar")
plt.title("Segment Wise Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(range(len(monthly_sales)), monthly_sales.index)
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
plt.hist(df["Sales"], bins=20)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(7, 5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

summary = pd.DataFrame({
    "Total Orders": [len(df)],
    "Total Sales": [round(df["Sales"].sum(), 2)],
    "Total Profit": [round(df["Profit"].sum(), 2)],
    "Categories": [df["Category"].nunique()],
    "States": [df["State"].nunique()]
})

summary.to_csv("sales_summary.csv", index=False)
df.drop(columns=["Month_Num"]).to_csv("cleaned_superstore.csv", index=False)

print("\nSummary")
print(summary)

print("\nProject Completed Successfully")
