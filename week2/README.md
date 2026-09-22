# Data Collection, Cleaning, and Preprocessing of Logistics Data Using Python

## Project Objective
The objective of this project is to prepare raw logistics data for further analytics and machine learning applications. Real-world logistics data often contains missing values, duplicate entries, outliers, and inconsistent categorical labels. This project demonstrates a comprehensive data preprocessing pipeline using Python to transform a raw dataset into a clean, analysis-ready format.

## Dataset / Source
This project uses a simulated logistics dataset (`logistics_sample_data.csv`) modeled after realistic supply chain and transportation open data sources (such as those available on Kaggle or the UCI Machine Learning Repository). 
The dataset contains information regarding shipments, origins, destinations, distances, vehicle types, shipment weights, delivery times, transportation costs, and delivery statuses. Intentionally introduced data-quality issues are included to demonstrate the cleaning pipeline.

## Data Preprocessing Steps
1. **Data Loading**: Reading raw CSV data.
2. **Initial Profiling**: Checking data shape, types, and missing values.
3. **Duplicate Removal**: Identifying and dropping identical records.
4. **Data Type Conversion**: Parsing string dates into proper `datetime` objects.
5. **Categorical Cleaning**: Standardizing text (e.g., stripping whitespace, title casing).
6. **Missing Value Handling**: Applying median imputation for continuous variables and mode imputation for categorical ones.
7. **Outlier Detection**: Using the Interquartile Range (IQR) method to cap extreme values (e.g., unrealistic delivery times).
8. **Feature Engineering**: Creating new calculated columns, such as `Delivery_Delay` and `Cost_Per_Km`.
9. **Normalization/Scaling**: Using `MinMaxScaler` to scale numerical features like `Distance_km` and `Shipment_Weight_kg` for algorithmic compatibility.
10. **Final Validation**: Verifying that the data is clean before exporting to `cleaned_logistics_data.csv`.

## Technologies Used
* **Python 3.x**
* **pandas** - Data manipulation and analysis
* **numpy** - Numerical operations
* **scikit-learn** - Data scaling and preprocessing tools

## Project Structure
* `logistics_sample_data.csv` - The raw, simulated dataset containing data issues.
* `week2_logistics_preprocessing.py` - The complete Python preprocessing script.
* `cleaned_logistics_data.csv` - The output dataset (generated after running the script).
* `Laxmi_Ananda_Sanas_Week_2_Data_Preprocessing_Report.docx` - The comprehensive Word report detailing the methodology.
* `README.md` - This file.

## How to Run the Python Script
1. Ensure Python 3.x is installed on your system.
2. Install the required dependencies via pip:
   ```bash
   pip install pandas numpy scikit-learn
   ```
3. Run the preprocessing script:
   ```bash
   python week2_logistics_preprocessing.py
   ```

## Expected Output
The script will output progress logs to the console detailing the number of duplicates removed, missing values handled, and outliers capped. Upon completion, a new file named `cleaned_logistics_data.csv` will be generated in the same directory.

**Note**: This project was prepared as part of the YuvaIntern Logistics Data Analyst Internship (Week 2 Task).
