# E-commerce Data Cleaning & Analysis

This project focuses on cleaning and analyzing a sample E-commerce sales dataset using **Pandas**. The dataset includes order details such as product names, categories, quantities, prices, and customer cities.

## 📋 Project Highlights
- **Duplicate Removal**  
- **Missing Data Handling**
- **Data Type Conversion**
- **Data Aggregation & Analysis**
- **Exporting Cleaned Dataset**

## ✅ Cleaning Steps:
1. Loaded CSV dataset.
2. Removed duplicate records.
3. Filled missing values:
   - Median for `Quantity Ordered`
   - Mean for `Price Each`
   - 'Unknown' for missing cities
4. Converted `Quantity Ordered` to integer type.

## ✅ Analysis Tasks:
- Total orders per city.
- Average product price per category.
- Identified the city with the highest total sales.

## 📂 Files Included:
- `ecommerce_sales_data.csv` — Original messy dataset.
- `ecommerce_sales_cleaned.csv` — Cleaned and processed dataset.
- `ecommerce_data_cleaning.py` — Python script for data cleaning and analysis.

## 🚀 Technologies Used:
- Python
- Pandas

## ✅ How to Run:
```bash
python ecommerce_data_cleaning.py
