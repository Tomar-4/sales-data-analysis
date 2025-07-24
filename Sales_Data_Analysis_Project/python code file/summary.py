import pandas as pd
df = pd.read_csv("C:\\Users\\prash\\Downloads\\panda project\\Feature_Engineering.csv" ,encoding='latin1')
monthly_sales = df.groupby(['YEAR_ID','MONTH_ID'])['TOTAL PRICE'].sum().reset_index()
monthly_sales.to_csv("monthly_sales_summary.csv", index=False)

