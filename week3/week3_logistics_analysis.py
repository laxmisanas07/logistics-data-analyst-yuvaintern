import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os

def load_data():
    df = pd.read_csv("cleaned_logistics_data.csv")
    return df

def calculate_kpis(df):
    total_deliveries = len(df)
    on_time = len(df[df['Delivery_Status'].str.lower() == 'on-time'])
    on_time_rate = (on_time / total_deliveries) * 100 if total_deliveries > 0 else 0
    
    avg_delivery_time = df['Delivery_Time_Hours'].mean()
    avg_transport_cost = df['Transportation_Cost'].mean()
    
    df['Cost_Per_Km_Raw'] = df['Transportation_Cost'] / df['Distance_km']
    # If distance was scaled, this might be weird, but let's calculate based on actual values if possible.
    # Since Distance_km was min-max scaled in week 2, let's just use what's there.
    avg_cost_per_km = df['Cost_Per_Km'].mean() if 'Cost_Per_Km' in df.columns else df['Cost_Per_Km_Raw'].mean()
    
    shipment_volume = total_deliveries
    
    kpis = {
        'On_Time_Delivery_Rate': float(on_time_rate),
        'Average_Delivery_Time': float(avg_delivery_time),
        'Average_Transportation_Cost': float(avg_transport_cost),
        'Average_Cost_per_Kilometer': float(avg_cost_per_km),
        'Shipment_Volume': int(shipment_volume)
    }
    return kpis

def perform_eda(df):
    stats = {}
    stats['rows'] = int(df.shape[0])
    stats['cols'] = int(df.shape[1])
    
    desc = df.describe().to_dict()
    stats['describe'] = desc
    
    # Missing values
    missing = df.isnull().sum().to_dict()
    stats['missing'] = {k: int(v) for k, v in missing.items()}
    
    stats['duplicates'] = int(df.duplicated().sum())
    
    # Categorical and numerical columns
    stats['numerical'] = df.select_dtypes(include=[np.number]).columns.tolist()
    stats['categorical'] = df.select_dtypes(include=['object']).columns.tolist()
    
    # Central Tendency and Dispersion for Delivery_Time_Hours
    del_time = df['Delivery_Time_Hours']
    stats['delivery_time'] = {
        'mean': float(del_time.mean()),
        'median': float(del_time.median()),
        'std': float(del_time.std()),
        'min': float(del_time.min()),
        'max': float(del_time.max()),
        'range': float(del_time.max() - del_time.min()),
        'q1': float(del_time.quantile(0.25)),
        'q3': float(del_time.quantile(0.75))
    }
    
    return stats

def create_visualizations(df):
    os.makedirs('figures', exist_ok=True)
    sns.set_theme(style="whitegrid")
    
    # 1. Delivery Time Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Delivery_Time_Hours'], bins=10, kde=True, color='skyblue')
    plt.title('Delivery Time Distribution')
    plt.xlabel('Delivery Time (Hours)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('figures/delivery_time_distribution.png')
    plt.close()
    
    # 2. Transportation Cost Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Transportation_Cost'], bins=10, kde=True, color='salmon')
    plt.title('Transportation Cost Distribution')
    plt.xlabel('Transportation Cost')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.savefig('figures/transportation_cost_distribution.png')
    plt.close()
    
    # 3. Vehicle Type Analysis (Average Delivery Time by Vehicle Type)
    plt.figure(figsize=(8, 5))
    vehicle_time = df.groupby('Vehicle_Type')['Delivery_Time_Hours'].mean().reset_index()
    sns.barplot(x='Vehicle_Type', y='Delivery_Time_Hours', data=vehicle_time, palette='viridis')
    plt.title('Average Delivery Time by Vehicle Type')
    plt.xlabel('Vehicle Type')
    plt.ylabel('Average Delivery Time (Hours)')
    plt.tight_layout()
    plt.savefig('figures/vehicle_type_analysis.png')
    plt.close()
    
    # 4. Distance vs Delivery Time
    plt.figure(figsize=(8, 5))
    sns.regplot(x='Distance_km', y='Delivery_Time_Hours', data=df, scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
    plt.title('Distance vs Delivery Time')
    plt.xlabel('Distance (Scaled)')
    plt.ylabel('Delivery Time (Hours)')
    plt.tight_layout()
    plt.savefig('figures/distance_vs_delivery_time.png')
    plt.close()
    
    # 5. Distance vs Transportation Cost
    plt.figure(figsize=(8, 5))
    sns.regplot(x='Distance_km', y='Transportation_Cost', data=df, scatter_kws={'alpha':0.6}, line_kws={'color':'green'})
    plt.title('Distance vs Transportation Cost')
    plt.xlabel('Distance (Scaled)')
    plt.ylabel('Transportation Cost')
    plt.tight_layout()
    plt.savefig('figures/distance_vs_cost.png')
    plt.close()
    
    # 6. Delivery Status
    plt.figure(figsize=(8, 5))
    sns.countplot(x='Delivery_Status', data=df, palette='pastel')
    plt.title('Delivery Status Distribution')
    plt.xlabel('Delivery Status')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig('figures/delivery_status.png')
    plt.close()
    
    # 7. Time Trend (Order Date vs Delivery Time)
    plt.figure(figsize=(10, 5))
    if 'Order_Date' in df.columns:
        df['Order_Date'] = pd.to_datetime(df['Order_Date'])
        time_df = df.dropna(subset=['Order_Date']).sort_values('Order_Date')
        sns.lineplot(x='Order_Date', y='Delivery_Time_Hours', data=time_df, marker='o')
        plt.title('Delivery Time Over Time')
        plt.xlabel('Order Date')
        plt.ylabel('Delivery Time (Hours)')
        plt.xticks(rotation=45)
    else:
        plt.text(0.5, 0.5, "Order_Date not available", ha='center', va='center')
    plt.tight_layout()
    plt.savefig('figures/logistics_time_trend.png')
    plt.close()
    
    # 8. Correlation Heatmap
    plt.figure(figsize=(8, 6))
    num_df = df.select_dtypes(include=[np.number])
    corr = num_df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('figures/correlation_heatmap.png')
    plt.close()
    
    return corr.to_dict()

def main():
    print("Loading data...")
    df = load_data()
    
    print("Performing EDA...")
    stats = perform_eda(df)
    
    print("Calculating KPIs...")
    kpis = calculate_kpis(df)
    stats['kpis'] = kpis
    
    print("Creating visualizations...")
    corr_dict = create_visualizations(df)
    stats['correlations'] = corr_dict
    
    print("Saving statistics...")
    with open('stats.json', 'w') as f:
        json.dump(stats, f, indent=4)
        
    print("Analysis complete. Visualizations saved in 'figures/' directory.")

if __name__ == '__main__':
    main()
