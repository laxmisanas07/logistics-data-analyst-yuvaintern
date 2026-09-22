# Predictive Modeling and Optimization in Logistics Using Python

## Project Objective
This project represents Week 4 of the YuvaIntern Logistics Data Analyst Internship. The core objective is to transition from descriptive analytics to prescriptive analytics by developing a predictive machine learning model. This model forecasts logistics delivery times using relevant shipment and operational features. The project implements, evaluates, and tunes multiple regression models and proposes strategic logistics optimizations based on the model's insights.

## Dataset
We utilized the preprocessed dataset `cleaned_logistics_data.csv` derived from the earlier stages of the internship.
**Note**: The dataset represents a simulated logistics scenario designed for analytical demonstration. Findings and model metrics should not be interpreted as actual company performance.

## Predictive Modeling Workflow
1. **Data Preparation**: Dropped non-predictive identifiers and applied One-Hot Encoding to categorical variables (`Vehicle_Type`, `Origin`, etc.).
2. **Train-Test Split**: Divided data 80/20 to train the model and test it on unseen data.
3. **Model Training**: Implemented baseline Linear Regression, Decision Tree Regression, and Random Forest Regression.
4. **Evaluation**: Scored models using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R²).
5. **Hyperparameter Tuning**: Used `GridSearchCV` to optimize the Random Forest model's parameters (e.g., `n_estimators`, `max_depth`).
6. **Feature Importance Analysis**: Extracted the most influential variables driving the delivery time predictions.

## Visualizations Created (in `figures/`)
1. `actual_vs_predicted.png`: Scatter plot comparing model predictions against real test data.
2. `residual_plot.png`: Evaluates model error distribution.
3. `model_comparison.png`: Dual-axis bar chart comparing RMSE and R² across algorithms.
4. `feature_importance.png`: Highlights top features driving the Random Forest model.

## Technologies Used
- Python 3.x
- scikit-learn (Machine Learning implementation)
- pandas & numpy (Data manipulation)
- matplotlib & seaborn (Visualization)
- Jupyter Notebook

## Project Structure
```
Week-4-Logistics-Modeling/
├── README.md
├── week4_logistics_modeling.py
├── week4_logistics_modeling.ipynb
├── cleaned_logistics_data.csv
├── figures/
│   ├── actual_vs_predicted.png
│   ├── residual_plot.png
│   ├── model_comparison.png
│   └── feature_importance.png
└── report/
    └── Laxmi_Ananda_Sanas_Week_4_Logistics_Modeling_Report.docx
```

## How to Run the Python Script
Ensure you have the required libraries installed:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```
Then, execute the modeling script:
```bash
python week4_logistics_modeling.py
```

## How to Open the Notebook
```bash
jupyter notebook week4_logistics_modeling.ipynb
```

## Logistics Optimization Strategies
Based on the predictive model, the project recommends:
- **Dynamic Route Planning**: Using predictions to reroute shipments prior to dispatch.
- **Resource Allocation**: Assigning highly reliable vehicle types to time-sensitive routes.
- **Cost Management**: Reducing reliance on expedited shipping buffers by trusting statistical delivery time windows.

---
*Prepared by Laxmi Ananda Sanas for the YuvaIntern Logistics Data Analyst Internship.*
