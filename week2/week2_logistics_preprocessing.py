import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def main():
    print("--- YuvaIntern Week 2: Logistics Data Preprocessing Pipeline ---")
    
    # 1. Load data
    print("\n[1] Loading dataset...")
    df = pd.read_csv("logistics_sample_data.csv")
    
    # 2. Inspect data
    print("\n[2] Initial Data Profiling")
    print(f"Shape: {df.shape}")
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # 3. Remove duplicates
    print("\n[3] Handling Duplicates")
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate rows.")
    
    # 4. Convert data types
    print("\n[4] Converting Data Types")
    # Convert 'Order_Date' to datetime, coerce errors to NaT
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    
    # 5. Clean categorical values
    print("\n[5] Cleaning Categorical Data")
    df['Origin'] = df['Origin'].astype(str).str.strip().str.title()
    df['Destination'] = df['Destination'].astype(str).str.strip().str.title()
    
    # 6. Handle missing values
    print("\n[6] Handling Missing Values")
    # Median imputation for numerical
    median_time = df['Delivery_Time_Hours'].median()
    df['Delivery_Time_Hours'] = df['Delivery_Time_Hours'].fillna(median_time)
    
    median_cost = df['Transportation_Cost'].median()
    df['Transportation_Cost'] = df['Transportation_Cost'].fillna(median_cost)
    
    # Mode imputation for categorical
    mode_status = df['Delivery_Status'].mode()[0]
    df['Delivery_Status'] = df['Delivery_Status'].fillna(mode_status)
    
    # 7. Detect outliers (using IQR on Delivery_Time_Hours)
    print("\n[7] Handling Outliers")
    Q1 = df['Delivery_Time_Hours'].quantile(0.25)
    Q3 = df['Delivery_Time_Hours'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    
    outliers = df[(df['Delivery_Time_Hours'] > upper_bound) | (df['Delivery_Time_Hours'] < lower_bound)]
    print(f"Detected {len(outliers)} potential outliers in Delivery_Time_Hours.")
    # For demonstration, cap extreme outliers to upper bound
    df['Delivery_Time_Hours'] = np.where(df['Delivery_Time_Hours'] > upper_bound, upper_bound, df['Delivery_Time_Hours'])
    
    # 8. Create relevant features
    print("\n[8] Feature Engineering")
    df['Delivery_Delay'] = df['Delivery_Time_Hours'] - df['Expected_Delivery_Hours']
    df['Cost_Per_Km'] = df['Transportation_Cost'] / df['Distance_km']
    
    # 9. Scale selected numerical variables
    print("\n[9] Scaling Numerical Variables")
    scaler = MinMaxScaler()
    df[['Distance_km', 'Shipment_Weight_kg']] = scaler.fit_transform(df[['Distance_km', 'Shipment_Weight_kg']])
    
    # 10. Final validation
    print("\n[10] Final Validation")
    print(f"Final Shape: {df.shape}")
    print("Missing values after cleaning:")
    print(df.isnull().sum())
    
    # 11. Save cleaned dataset
    print("\n[11] Saving Cleaned Dataset")
    output_filename = "cleaned_logistics_data.csv"
    df.to_csv(output_filename, index=False)
    print(f"Dataset successfully saved as {output_filename}")

if __name__ == '__main__':
    main()
