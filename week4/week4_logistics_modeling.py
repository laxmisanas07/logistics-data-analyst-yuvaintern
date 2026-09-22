import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def load_and_preprocess_data():
    df = pd.read_csv("cleaned_logistics_data.csv")
    
    # Drop identifiers and date columns which aren't direct features for simple regression
    df_model = df.drop(['Shipment_ID', 'Order_Date'], axis=1, errors='ignore')
    
    # If Delivery_Delay is present, we should drop it to prevent data leakage because Delivery_Delay = Delivery_Time - Expected_Time
    df_model = df_model.drop(['Delivery_Delay'], axis=1, errors='ignore')
    
    # One-Hot Encoding for categorical variables
    categorical_cols = df_model.select_dtypes(include=['object']).columns
    df_encoded = pd.get_dummies(df_model, columns=categorical_cols, drop_first=True)
    
    return df_encoded

def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    return mae, rmse, r2, predictions

def main():
    print("Loading and preprocessing data...")
    df = load_and_preprocess_data()
    
    # Target variable is Delivery_Time_Hours
    X = df.drop('Delivery_Time_Hours', axis=1)
    y = df['Delivery_Time_Hours']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    stats = {}
    stats['data_shape'] = {'rows': df.shape[0], 'cols': df.shape[1]}
    
    print("Training models...")
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(random_state=42),
        'Random Forest': RandomForestRegressor(random_state=42)
    }
    
    results = {}
    predictions_dict = {}
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        mae, rmse, r2, preds = evaluate_model(model, X_test, y_test)
        results[name] = {'MAE': float(mae), 'RMSE': float(rmse), 'R2': float(r2)}
        predictions_dict[name] = preds
        print(f"{name} - MAE: {mae:.2f}, RMSE: {rmse:.2f}, R2: {r2:.2f}")

    stats['initial_results'] = results

    print("Performing Hyperparameter Tuning on Random Forest...")
    # Because sample size might be small, we keep cv small
    cv_folds = 3 if len(X_train) >= 9 else 2
    param_grid = {
        'n_estimators': [10, 50, 100],
        'max_depth': [None, 5, 10],
        'min_samples_split': [2, 5]
    }
    
    rf = RandomForestRegressor(random_state=42)
    grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=cv_folds, n_jobs=-1, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)
    
    best_rf = grid_search.best_estimator_
    best_mae, best_rmse, best_r2, best_preds = evaluate_model(best_rf, X_test, y_test)
    
    stats['best_rf_params'] = grid_search.best_params_
    stats['best_rf_results'] = {'MAE': float(best_mae), 'RMSE': float(best_rmse), 'R2': float(best_r2)}
    
    print(f"Best RF - MAE: {best_mae:.2f}, RMSE: {best_rmse:.2f}, R2: {best_r2:.2f}")

    # Generate Visualizations
    print("Generating visualizations...")
    os.makedirs('figures', exist_ok=True)
    sns.set_theme(style="whitegrid")
    
    # 1. Actual vs Predicted (Best Model)
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, best_preds, alpha=0.7, color='blue', label='Predictions')
    plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', label='Perfect Fit')
    plt.xlabel('Actual Delivery Time')
    plt.ylabel('Predicted Delivery Time')
    plt.title('Actual vs Predicted Delivery Time (Random Forest)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('figures/actual_vs_predicted.png')
    plt.close()
    
    # 2. Residual Plot
    residuals = y_test - best_preds
    plt.figure(figsize=(8, 6))
    plt.scatter(best_preds, residuals, alpha=0.7, color='purple')
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Predicted Delivery Time')
    plt.ylabel('Residuals')
    plt.title('Residual Plot (Random Forest)')
    plt.tight_layout()
    plt.savefig('figures/residual_plot.png')
    plt.close()
    
    # 3. Model Comparison
    models_names = list(results.keys())
    rmse_vals = [results[m]['RMSE'] for m in models_names]
    r2_vals = [results[m]['R2'] for m in models_names]
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    x = np.arange(len(models_names))
    width = 0.35
    
    ax1.bar(x - width/2, rmse_vals, width, label='RMSE', color='skyblue')
    ax1.set_ylabel('RMSE', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')
    
    ax2 = ax1.twinx()
    ax2.bar(x + width/2, r2_vals, width, label='R²', color='salmon')
    ax2.set_ylabel('R²', color='salmon')
    ax2.tick_params(axis='y', labelcolor='salmon')
    
    ax1.set_xticks(x)
    ax1.set_xticklabels(models_names)
    plt.title('Model Comparison (RMSE and R²)')
    fig.tight_layout()
    plt.savefig('figures/model_comparison.png')
    plt.close()
    
    # 4. Feature Importance
    feature_importances = best_rf.feature_importances_
    features = X.columns
    importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importances})
    importance_df = importance_df.sort_values(by='Importance', ascending=False).head(10) # Top 10
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=importance_df, palette='viridis')
    plt.title('Top 10 Feature Importances (Random Forest)')
    plt.xlabel('Importance Score')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.savefig('figures/feature_importance.png')
    plt.close()
    
    stats['top_features'] = importance_df.to_dict('records')

    # Save stats
    with open('stats.json', 'w') as f:
        json.dump(stats, f, indent=4)
        
    print("Analysis complete. Visualizations saved in 'figures/' directory.")

if __name__ == '__main__':
    main()
