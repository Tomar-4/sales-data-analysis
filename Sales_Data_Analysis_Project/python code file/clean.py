import pandas as pd 
#read csv file
df = pd.read_csv("C:\\Users\\prash\\Downloads\\panda project\\sales_data_sample.csv",encoding='latin1')
#Fill missing POSTALCODE with 0000 & clean code
df['POSTALCODE'] = df['POSTALCODE'].astype(str).str.replace(r'\D','',regex=True)
#Mark values with less than 5 digits as 'Invalid'
df['POSTALCODE'] = df['POSTALCODE'].str[:5]
df['POSTALCODE'] = df['POSTALCODE'].apply(lambda x:x if len(x) >=5 else'Invalid')
df['POSTALCODE'].fillna(0000, inplace=True)
#removing unwanted coloumns 
df=df.drop(columns = ["ADDRESSLINE2", "STATE", "TERRITORY"])
# Clean the PHONE column – remove all non-digits
df['PHONE'] = df['PHONE'].str.replace(r'\D','',regex=True)
# Filter phone numbers with at least 10 digits
df['PHONE'] = df['PHONE'].apply(lambda x:x if len(x)>=10 else 'Invalid') 
df['PHONE'] = df['PHONE'].apply(lambda x: f"{x[-10:-7]}-{x[-7:-4]}-{x[-4:]}" if x!='Invalid'else x)
#saving file
df.to_csv("cleaned_sales_data.csv", index=False)
