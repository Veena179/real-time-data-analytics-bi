# KPI Analysis Script
# Author: A Veena

import pandas as pd

# Sample business data
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [1200, 1500, 1800, 1700],
    "Revenue": [30000, 38000, 45000, 42000],
    "Customers": [100, 120, 140, 135]
}

df = pd.DataFrame(data)

# KPI Calculations
total_sales = df["Sales"].sum()
total_revenue = df["Revenue"].sum()
avg_customers = df["Customers"].mean()

print("📊 KPI SUMMARY")
print("----------------------")
print(f"Total Sales     : {total_sales}")
print(f"Total Revenue   : {total_revenue}")
print(f"Avg Customers   : {avg_customers:.2f}")
