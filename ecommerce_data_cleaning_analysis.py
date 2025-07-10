import pandas as pd

ecom = pd.read_csv("ecommerce_sales_data.csv")
print("Original DataFrame (First 5 Rows):")
print(ecom.head(5))

print("\nNull Values Before Cleaning:")
print(ecom.isnull().sum())

before = len(ecom)
ecom = ecom.drop_duplicates()
after = len(ecom)
print("\nNumber of Rows Dropped After Removing Duplicates:")
print(before - after)

median_quantity = ecom['Quantity Ordered'].median()
ecom['Quantity Ordered'] = ecom['Quantity Ordered'].fillna(median_quantity)
mean_price = ecom['Price Each'].mean()
ecom['Price Each'] = ecom['Price Each'].fillna(mean_price)
ecom['City'] = ecom['City'].fillna("Unknown")
ecom['Quantity Ordered'] = ecom['Quantity Ordered'].astype(int)

print("\nNumber of Orders per City:")
print(ecom.groupby('City')['Quantity Ordered'].count())

print("\nAverage Price Per Category:")
avg_price_per_cat = ecom.groupby('Category')['Price Each'].mean()
print(avg_price_per_cat)

price = ecom['Price Each'] * ecom['Quantity Ordered']
ecom['Total Sales'] = price
sales = ecom.groupby('City')['Total Sales'].sum()
print("\nCity with Highest Total Sales:")
print(sales.idxmax())

ecom.to_csv("ecommerce_sales_cleaned.csv", index=False)
print("\nCleaned DataFrame Exported Successfully.")
