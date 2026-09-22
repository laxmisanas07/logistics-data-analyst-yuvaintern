# Advanced Data Analysis and Visualization of Logistics Performance Using Python

## Project Objective
This project continues the YuvaIntern Logistics Data Analyst Internship task for Week 3. The objective is to perform Exploratory Data Analysis (EDA) on the preprocessed logistics dataset from Week 2. By systematically exploring distributions, calculating KPIs, and visualizing core relationships (such as distance vs. delivery time and transportation cost), this analysis provides actionable operational insights and sets the stage for predictive modeling in Week 4.

## Dataset
We utilized the cleaned and preprocessed dataset `cleaned_logistics_data.csv` prepared in Week 2. 
**Note**: The dataset represents a simulated logistics scenario designed for analytical demonstration. Findings should not be interpreted as actual company performance.

## EDA Performed
- **Central Tendency & Dispersion**: Calculated Mean, Median, Min, Max, and standard deviations for delivery times and transportation costs.
- **Frequency Analysis**: Analyzed delivery statuses (On-Time vs Late) and vehicle types.
- **Correlation**: Mapped the numerical relationships using a correlation matrix to identify strong predictors (e.g., Distance vs Cost).

## Visualizations Created (in `figures/`)
1. `delivery_time_distribution.png`: Histogram of Delivery Time.
2. `transportation_cost_distribution.png`: Histogram of Transportation Cost.
3. `vehicle_type_analysis.png`: Bar chart of Average Delivery Time by Vehicle Type.
4. `distance_vs_delivery_time.png`: Scatter plot tracking route length vs duration.
5. `distance_vs_cost.png`: Scatter plot highlighting cost drivers.
6. `delivery_status.png`: Count plot of On-Time vs Delayed shipments.
7. `logistics_time_trend.png`: Time-series view of delivery duration across order dates.
8. `correlation_heatmap.png`: Heatmap of numerical correlations.

## KPIs Calculated
- On-Time Delivery Rate
- Average Delivery Time
- Average Transportation Cost
- Average Cost per Kilometer
- Shipment Volume

## Technologies Used
- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- Jupyter Notebook

## Project Structure
```
Week-3-Logistics-Analysis/
├── README.md
├── week3_logistics_analysis.py
├── week3_logistics_analysis.ipynb
├── cleaned_logistics_data.csv
├── figures/
│   ├── delivery_time_distribution.png
│   ├── transportation_cost_distribution.png
│   ├── vehicle_type_analysis.png
│   ├── distance_vs_delivery_time.png
│   ├── distance_vs_cost.png
│   ├── delivery_status.png
│   ├── logistics_time_trend.png
│   └── correlation_heatmap.png
└── report/
    └── Laxmi_Ananda_Sanas_Week_3_Logistics_Analysis_Report.docx
```

## Installation Requirements
Ensure Python is installed along with the required analytical libraries:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

## How to Run the Python Script
To execute the analysis and regenerate all visualizations and KPIs:
```bash
python week3_logistics_analysis.py
```

## How to Open the Notebook
To view and interact with the analysis cell-by-cell:
```bash
jupyter notebook week3_logistics_analysis.ipynb
```

## Limitations
The primary limitation is the use of a simulated sample dataset. Complex real-world logistical nuances—such as unpredictable weather patterns, live traffic anomalies, or driver hours-of-service regulations—are not captured in this simulated snapshot.

---
*Prepared by Laxmi Ananda Sanas for the YuvaIntern Logistics Data Analyst Internship.*
