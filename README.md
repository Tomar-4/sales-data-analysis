# sales-data-analysis
Beginner-friendly sales data analysis project using Python &amp; Pandas.
# 🧪 Sales Data Analysis using Python & Pandas

This project is a beginner-friendly data analysis project using **Python** and **Pandas**.  
It explores a real-world sales dataset to uncover patterns, clean data, and visualize trends.

## 📁 Dataset

- `sales_data_sample.csv`: Raw sales data
- `sales_data_feature_engineered.csv`: Cleaned and feature-enhanced version
- `monthly_sales_summary.csv`: Monthly grouped sales totals
- `monthly_sales_trend.png`: Line graph of monthly sales trends
## 🔧 Tools Used

- Python 3.x
- Pandas
- Matplotlib
- VS Code

## 🔍 What I Did

### ✅ Step 1: Data Cleaning
- Removed unused columns (`ADDRESSLINE2`, `STATE`, `TERRITORY`)
- Filled missing values in `POSTALCODE` with `00000`
- Cleaned `PHONE` numbers to digits only
- Converted `ORDERDATE` into datetime format

### ✅ Step 2: Feature Engineering
- Created `TOTAL PRICE` column = `QUANTITYORDERED` × `PRICEEACH`
- Extracted `YEAR` and `MONTH` from `ORDERDATE`
- Combined them into `YearMonth` for time series analysis

### ✅ Step 3: Analysis
- Grouped sales by `YEAR` and `MONTH`
- Summed `TOTAL PRICE` to get monthly sales
- Exported results to `monthly_sales_summary.csv`

### ✅ Step 4: Visualization
- Created a **line graph** to visualize monthly sales over time  
## 📈 Insights
- Sales increased in December across multiple years.
- There are seasonal patterns (high sales in Q4).
- Useful for forecasting and planning inventory.
## 📚 Learning Outcomes
- 🧹 Cleaned messy real-world data using Pandas
- 🏗️ Created new features from existing columns
- 📊 Grouped and aggregated data
- 📈 Created visual charts to show trends
- 💾 Exported and saved cleaned/summary data for reuse

## 🧑‍💻 Author
PRASHANT SINGH 
Aspiring Data Analyst | Python & Excel Enthusiast  
[LinkedIn](https://www.linkedin.com/in/prashant-singh-0911aa194/) | [GitHub](https://github.com/Tomar-4)
