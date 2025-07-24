import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("monthly_sales_summary.csv")
# Create YearMonth for X-axis
df['YearMonth'] = df['YEAR_ID'].astype(str) + '-' + df['MONTH_ID'].astype(str).str.zfill(2)
print(df)
# # Plot
# plt.figure(figsize=(12,6))
# plt.plot(df['YearMonth'], df['TOTAL PRICE'], marker='o', color='teal')
# plt.title("Monthly Sales Over Time", fontsize=16)
# plt.xlabel("Year-Month")
# plt.ylabel("Total Sales")
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.tight_layout()
# plt.show()