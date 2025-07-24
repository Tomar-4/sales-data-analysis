import pandas as pd
df = pd.read_csv("C:\\Users\\prash\\Downloads\\panda project\\cleaned_sales_data.csv", encoding="latin1")
df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE']).dt.date
# Create new column: Total price per order line
df['TOTAL PRICE'] = df['QUANTITYORDERED'] * df['PRICEEACH']
#save the file 
df.to_csv("Feature_Engineering.csv", index=False)