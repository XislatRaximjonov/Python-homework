import pandas as pd

# Load dataset
df = pd.read_csv("task/sales_data.csv")

# -----------------------------
# 1. Group by Category
# -----------------------------
category_stats = df.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
).reset_index()

print("Category statistics:")
print(category_stats)

# -----------------------------
# 2. Top-selling product per category
# -----------------------------
product_sales = df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()

top_products = product_sales.loc[
    product_sales.groupby("Category")["Quantity"].idxmax()
]

print("\nTop-selling product in each category:")
print(top_products)

# -----------------------------
# 3. Date with highest total sales
# -----------------------------
df["TotalSales"] = df["Quantity"] * df["Price"]

sales_by_date = df.groupby("Date")["TotalSales"].sum().reset_index()

highest_sales_date = sales_by_date.loc[sales_by_date["TotalSales"].idxmax()]

print("\nDate with highest total sales:")
print(highest_sales_date)


import pandas as pd

df = pd.read_csv("task/customer_orders.csv")

orders_per_customer = df.groupby("CustomerID").size()

active_customers = orders_per_customer[orders_per_customer >= 20]

print("Customers with at least 20 orders:")
print(active_customers)


avg_price_customer = df.groupby("CustomerID")["Price"].mean()

premium_customers = avg_price_customer[avg_price_customer > 120]

print("\nCustomers with average price > $120:")
print(premium_customers)


product_totals = df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", lambda x: (x * df.loc[x.index, "Quantity"]).sum())
)

filtered_products = product_totals[product_totals["total_quantity"] >= 5]

print("\nProducts with total quantity ≥ 5:")
print(filtered_products)


import sqlite3
import pandas as pd

conn = sqlite3.connect("task/population.db")

population_df = pd.read_sql(
    "SELECT State, Salary FROM population",
    conn
)

conn.close()

salary_bands = pd.read_excel("task/population salary analysis.xlsx")


def assign_band(salary):
    row = salary_bands[
        (salary_bands["MinSalary"] <= salary) &
        (salary_bands["MaxSalary"] >= salary)
    ]
    return row.iloc[0]["Band"] if not row.empty else "Unknown"

population_df["SalaryBand"] = population_df["Salary"].apply(assign_band)


summary = population_df.groupby("SalaryBand").agg(
    population_count=("Salary", "count"),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median")
).reset_index()

total_population = len(population_df)

summary["percentage"] = (summary["population_count"] / total_population) * 100

print(summary)


state_summary = population_df.groupby(["State", "SalaryBand"]).agg(
    population_count=("Salary", "count"),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median")
).reset_index()

state_totals = population_df.groupby("State").size().reset_index(name="total")

state_summary = state_summary.merge(state_totals, on="State")
state_summary["percentage"] = (
    state_summary["population_count"] / state_summary["total"] * 100
)

print(state_summary)
