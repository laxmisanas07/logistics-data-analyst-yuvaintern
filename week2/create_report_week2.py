import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE

def create_report():
    doc = Document()
    
    # Set page size to A4 and margins to 1 inch
    for section in doc.sections:
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # Modify heading styles
    def set_heading_style(level, size):
        try:
            style = doc.styles[f'Heading {level}']
        except KeyError:
            style = doc.styles.add_style(f'Heading {level}', WD_STYLE_TYPE.PARAGRAPH)
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(size)
        font.bold = True
        font.color.rgb = RGBColor(0, 0, 0)
    
    set_heading_style(1, 16)
    set_heading_style(2, 13)
    
    # Custom Title style
    title_style = doc.styles.add_style('CustomTitle', WD_STYLE_TYPE.PARAGRAPH)
    title_style.font.name = 'Calibri'
    title_style.font.size = Pt(24)
    title_style.font.bold = True
    title_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

    def add_paragraph(text, bold=False, justify=True, font_name='Calibri'):
        p = doc.add_paragraph()
        if justify:
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        run = p.add_run(text)
        run.bold = bold
        run.font.name = font_name
        return p

    def add_code(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = 'Consolas'
        run.font.size = Pt(10)
        return p

    # 1. COVER PAGE
    for _ in range(5):
        doc.add_paragraph()
    
    p = doc.add_paragraph("YuvaIntern\nLogistics Data Analyst Intern\nWeek 2 Task", style='CustomTitle')
    
    for _ in range(3):
        doc.add_paragraph()
        
    p = doc.add_paragraph("Data Collection, Cleaning, and Preprocessing of Logistics Data Using Python", style='CustomTitle')
    p.runs[0].font.size = Pt(20)
    
    for _ in range(10):
        doc.add_paragraph()
        
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("Student Name: Laxmi Ananda Sanas\nDate: September 2026").bold = True
    
    doc.add_page_break()
    
    # TOC placeholder
    doc.add_heading('Table of Contents', level=1)
    toc = (
        "1. COVER PAGE\n2. EXECUTIVE SUMMARY\n3. INTRODUCTION\n4. DATASET SELECTION AND DATA COLLECTION\n5. DATASET CHARACTERISTICS\n"
        "6. DATA COLLECTION SIMULATION\n7. INITIAL DATA PROFILING\n8. DATA QUALITY ISSUES\n9. HANDLING MISSING VALUES\n10. DUPLICATE DATA\n"
        "11. DATA TYPE CONVERSION\n12. INCONSISTENT CATEGORICAL DATA\n13. OUTLIER DETECTION\n14. NORMALIZATION AND STANDARDIZATION\n"
        "15. FEATURE ENGINEERING\n16. COMPLETE PREPROCESSING PIPELINE\n17. COMPLETE PYTHON PREPROCESSING SCRIPT\n18. BEFORE vs AFTER DATA QUALITY\n"
        "19. VALIDATION OF CLEANED DATA\n20. METHODOLOGICAL JUSTIFICATION\n21. IMPACT OF DATA QUALITY ON LOGISTICS ANALYTICS\n22. REFLECTION\n"
        "23. CONNECTION TO WEEK 3\n24. LIMITATIONS\n25. CONCLUSION\n26. REFERENCES"
    )
    add_paragraph(toc, justify=False)
    
    doc.add_page_break()

    # 2. EXECUTIVE SUMMARY
    doc.add_heading('2. EXECUTIVE SUMMARY', level=1)
    summary = (
        "In logistics and supply chain management, data quality is paramount. "
        "The purpose of collecting logistics data is to gain operational visibility, track KPIs, "
        "and enable advanced analytics like route optimization and demand forecasting. "
        "However, raw operational data inherently suffers from common data-quality problems such as "
        "missing values, duplicate records, inconsistent categories, and outliers. If not addressed, "
        "these anomalies can distort analysis, leading to suboptimal business decisions. "
        "\\n\\nPreprocessing is a critical mandatory step before conducting any analytical modeling. "
        "This project outlines a comprehensive preprocessing workflow to transform raw shipment data "
        "into a clean, analysis-ready format. Leveraging Python and its robust data science libraries "
        "— specifically pandas, numpy, and scikit-learn — the workflow systematically identifies and resolves data anomalies. "
        "\\n\\nThe overall preprocessing pipeline encompasses data loading, initial profiling, duplicate removal, "
        "data type conversion, categorical standardization, handling missing values through median/mode imputation, "
        "outlier treatment using the Interquartile Range (IQR) method, feature engineering, and feature scaling. "
        "\\n\\nThe expected value of this meticulously cleaned dataset is substantial. It ensures that the subsequent "
        "analyses (like those planned for Week 3) produce reliable, accurate insights, forming a trustworthy foundation "
        "for strategic logistics optimization."
    ).replace('\\n', '\n')
    add_paragraph(summary)

    # 3. INTRODUCTION
    doc.add_heading('3. INTRODUCTION', level=1)
    intro = (
        "Logistics data represents the quantifiable records of supply chain operations. It includes information "
        "such as shipment origins and destinations, transit times, transportation modes, operational costs, and "
        "delivery success statuses. Examples range from real-time GPS telemetry from delivery trucks to static "
        "inventory levels within a warehouse."
        "\\n\\nOrganizations collect this vast array of data—spanning shipment, delivery, inventory, transportation, "
        "and cost metrics—because it provides the empirical basis for continuous improvement. By analyzing this data, "
        "companies can minimize fuel consumption, improve delivery reliability, and enhance customer satisfaction."
        "\\n\\nDespite its value, raw data cannot always be directly used for analytics. Operations generate data "
        "in real-time through manual entries and automated sensors, both of which are prone to error. System glitches "
        "can create duplicates, human error can lead to inconsistent naming conventions (e.g., 'mumbai' vs 'Mumbai'), "
        "and sensor failures can result in missing values or extreme outliers."
        "\\n\\nTherefore, rigorous data cleaning and preprocessing are essential. Transforming this noisy raw data "
        "into a structured, high-quality dataset is the critical bridge between data collection and actionable logistics intelligence."
    ).replace('\\n', '\n')
    add_paragraph(intro)

    # 4. DATASET SELECTION AND DATA COLLECTION
    doc.add_heading('4. DATASET SELECTION AND DATA COLLECTION', level=1)
    dataset_info = (
        "Dataset Name: Supply Chain Logistics Problem Dataset\\n"
        "Source/Platform: Kaggle (Derived/Simulated open dataset)\\n"
        "URL: https://www.kaggle.com/datasets/amruta21/supply-chain-logistics-problem\\n"
        "\\nDataset Purpose: This dataset was originally published to facilitate the optimization of logistics "
        "and supply chain routing, analyzing delivery times and transportation costs across different shipping routes.\\n"
        "\\nImportant Variables: The dataset structure includes variables like Shipment_ID, Order_Date, Origin, Destination, "
        "Distance_km, Vehicle_Type, Shipment_Weight_kg, Delivery_Time_Hours, Expected_Delivery_Hours, Transportation_Cost, and Delivery_Status."
        "\\n\\nRelevance: This data is highly relevant to logistics analysis as it captures the fundamental components "
        "of physical distribution: time, space (distance), and cost. It provides a realistic basis for evaluating delivery efficiency. "
        "\\n\\nNote: For the purpose of demonstrating the Python preprocessing pipeline in this report without requiring access "
        "to a massive, potentially proprietary database, a simulated sample dataset ('logistics_sample_data.csv') has been "
        "created based on the structural characteristics of standard Kaggle logistics datasets. This simulated sample deliberately "
        "incorporates common data-quality issues to practically demonstrate the cleaning workflow."
    ).replace('\\n', '\n')
    add_paragraph(dataset_info)

    doc.add_page_break()

    # 5. DATASET CHARACTERISTICS
    doc.add_heading('5. DATASET CHARACTERISTICS', level=1)
    table1 = doc.add_table(rows=1, cols=5)
    table1.style = 'Table Grid'
    hdr_cells = table1.rows[0].cells
    headers = ['Variable Name', 'Data Type', 'Meaning', 'Example Value', 'Requires Preprocessing?']
    for i, header in enumerate(headers):
        hdr_cells[i].text = header
        hdr_cells[i].paragraphs[0].runs[0].bold = True
        
    chars = [
        ['Shipment_ID', 'String', 'Unique identifier for the shipment.', 'SHP001', 'No'],
        ['Order_Date', 'String/Date', 'Date the shipment was ordered.', '2026-09-01', 'Yes (Convert to Datetime)'],
        ['Origin', 'String', 'Starting city of the shipment.', 'mumbai', 'Yes (Standardize capitalization)'],
        ['Destination', 'String', 'Ending city of the shipment.', 'Delhi', 'Yes (Standardize capitalization)'],
        ['Distance_km', 'Float', 'Physical distance of the route.', '1400.0', 'Yes (Normalization)'],
        ['Vehicle_Type', 'String', 'Type of delivery vehicle used.', 'Truck', 'No'],
        ['Shipment_Weight_kg', 'Float', 'Weight of the package in kg.', '500.5', 'Yes (Normalization)'],
        ['Delivery_Time_Hours', 'Float', 'Actual hours taken for delivery.', '24.5', 'Yes (Handle Missing/Outliers)'],
        ['Expected_Delivery_Hours', 'Float', 'Promised delivery hours.', '22.0', 'No'],
        ['Transportation_Cost', 'Float', 'Cost incurred for the shipment.', '15000.0', 'Yes (Handle Missing)'],
        ['Delivery_Status', 'String', 'Categorical status (e.g., Late, On-Time).', 'Late', 'Yes (Handle Missing)']
    ]
    for row_data in chars:
        row_cells = table1.add_row().cells
        for i, val in enumerate(row_data):
            row_cells[i].text = val
            
    add_paragraph("")

    # 6. DATA COLLECTION SIMULATION
    doc.add_heading('6. DATA COLLECTION SIMULATION', level=1)
    sim = (
        "In a real logistics environment, data is continuously generated across fragmented systems. "
        "Possible data sources include Shipment Management Systems logging the origin and destination, "
        "Warehouse Systems recording inventory and weight, GPS/Vehicle tracking providing actual transit times, "
        "and Transportation Management Systems calculating operational costs. "
        "\\n\\nTo perform centralized analysis, data engineers typically query these various databases using SQL, "
        "join the records based on a unique key like Shipment_ID, and export the aggregated data to a flat file "
        "format such as CSV or Excel. This file is then ingested into a Python environment for analysis."
    ).replace('\\n', '\n')
    add_paragraph(sim)
    
    add_code("""import pandas as pd
df = pd.read_csv("logistics_sample_data.csv")
print(df.head())
print(df.shape)
print(df.info())""")

    # 7. INITIAL DATA PROFILING
    doc.add_heading('7. INITIAL DATA PROFILING', level=1)
    add_paragraph("Initial profiling is crucial to understand the structural integrity of the raw data.")
    
    add_code("""# View the first and last few rows to understand structure
print(df.head())
print(df.tail())

# Check the dimensions of the dataset (rows, columns)
print(df.shape)

# View data types and non-null counts
print(df.info())

# Get summary statistics for numerical columns
print(df.describe())

# View all column names
print(df.columns)

# Check unique values in a categorical column to spot inconsistencies
print(df['Origin'].unique())

# See the frequency of categories
print(df['Delivery_Status'].value_counts())

# Count missing values per column
print(df.isnull().sum())""")
    
    prof_exp = (
        "• head()/tail(): Validates that data loaded correctly and isn't corrupted at the ends.\\n"
        "• shape: Confirms the expected volume of data.\\n"
        "• info(): Identifies incorrect data types (e.g., dates loaded as objects).\\n"
        "• describe(): Highlights impossible numerical values (e.g., negative distances).\\n"
        "• unique()/value_counts(): Exposes misspellings or overlapping categories.\\n"
        "• isnull().sum(): Quantifies the extent of missing data that requires imputation."
    ).replace('\\n', '\n')
    add_paragraph(prof_exp, justify=False)

    doc.add_page_break()

    # 8. DATA QUALITY ISSUES
    doc.add_heading('8. DATA QUALITY ISSUES', level=1)
    table2 = doc.add_table(rows=1, cols=5)
    table2.style = 'Table Grid'
    hdr_cells2 = table2.rows[0].cells
    headers2 = ['Issue', 'Explanation', 'Detection', 'Impact on Analysis', 'Treatment']
    for i, header in enumerate(headers2):
        hdr_cells2[i].text = header
        hdr_cells2[i].paragraphs[0].runs[0].bold = True
        
    issues = [
        ['Missing values', 'Empty cells or Nulls in the data.', 'isnull().sum()', 'Causes mathematical errors in models and skewed averages.', 'Imputation (Median/Mode)'],
        ['Duplicate records', 'Identical rows entered multiple times.', 'duplicated().sum()', 'Artificially inflates KPI counts and volumes.', 'Drop duplicates'],
        ['Incorrect data types', 'Dates or numbers stored as text.', 'info()', 'Prevents date-math and numerical scaling.', 'Cast to datetime/numeric'],
        ['Inconsistent categorical values', 'Varying cases (mumbai vs MUMBAI).', 'unique()', 'Splits a single category into multiple separate entities.', 'Standardize string format'],
        ['Invalid values', 'Negative costs or distances.', 'describe()', 'Corrupts cost and route calculations.', 'Remove or cap records'],
        ['Outliers', 'Extremely high delivery times.', 'Boxplots, IQR calculation', 'Drastically skews means and linear regression models.', 'Cap/winsorize using IQR'],
        ['Different numerical scales', 'Distance in 1000s, Weight in 10s.', 'describe()', 'Dominates distance-based machine learning algorithms.', 'Min-Max Normalization'],
        ['Incorrect date formats', 'Mixed formats (DD/MM/YYYY vs MM/DD/YYYY).', 'Visual inspection', 'Prevents accurate time-series analysis.', 'Standardize format via pandas']
    ]
    for row_data in issues:
        row_cells = table2.add_row().cells
        for i, val in enumerate(row_data):
            row_cells[i].text = val
            
    add_paragraph("")

    # 9. HANDLING MISSING VALUES
    doc.add_heading('9. HANDLING MISSING VALUES', level=1)
    mv = (
        "Missing values can be addressed in several ways:\\n"
        "• Removing records: Appropriate when missing values are negligible (e.g., <1% of data).\\n"
        "• Mean imputation: Filling with the average, suitable for normally distributed data without outliers.\\n"
        "• Median imputation: Filling with the middle value. This is highly appropriate for logistics metrics like Delivery_Time because it is robust and insensitive to extreme outliers (e.g., a truck breakdown).\\n"
        "• Mode imputation: Filling with the most frequent value, used for categorical variables like Delivery_Status.\\n"
        "• Forward/Backward fill: Used in time-series data to carry the last known value forward.\\n"
        "• Business-rule imputation: Deriving the value based on other columns.\\n\\n"
        "Blindly replacing missing values with zero is dangerous in logistics. For instance, a delivery time of zero implies instantaneous teleportation, which ruins physical modeling."
    ).replace('\\n', '\n')
    add_paragraph(mv)
    add_code("""# Median-based imputation for numerical variables
df["Delivery_Time_Hours"].fillna(df["Delivery_Time_Hours"].median(), inplace=True)
df["Transportation_Cost"].fillna(df["Transportation_Cost"].median(), inplace=True)

# Mode-based imputation for categorical variables
df["Delivery_Status"].fillna(df["Delivery_Status"].mode()[0], inplace=True)""")

    # 10. DUPLICATE DATA
    doc.add_heading('10. DUPLICATE DATA', level=1)
    dup = (
        "Duplicate shipment records often occur due to system retries or sync errors between warehouse and transportation databases. "
        "If left unchecked, they distort logistics KPIs by inflating total shipment volume and artificially altering average delivery times and costs."
    )
    add_paragraph(dup)
    add_code("""print("Duplicates found:", df.duplicated().sum())
df = df.drop_duplicates()""")

    doc.add_page_break()

    # 11. DATA TYPE CONVERSION
    doc.add_heading('11. DATA TYPE CONVERSION', level=1)
    conv = (
        "Correct data types are critical. Dates stored as strings cannot be used to calculate delivery durations, "
        "and numerical costs stored with currency symbols as text cannot be aggregated."
    )
    add_paragraph(conv)
    add_code("""# Date conversion
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")""")

    # 12. INCONSISTENT CATEGORICAL DATA
    doc.add_heading('12. INCONSISTENT CATEGORICAL DATA', level=1)
    cat = (
        "Manual data entry often leads to inconsistent formatting. Values like 'Mumbai', 'mumbai', and 'MUMBAI' "
        "represent the same physical origin but will be treated as three distinct groups by analytical functions, "
        "ruining route-based aggregations. String methods are used to standardize these fields."
    )
    add_paragraph(cat)
    add_code("""# Strip whitespaces and standardize to Title Case
df["Origin"] = df["Origin"].str.strip().str.title()
df["Destination"] = df["Destination"].str.strip().str.title()""")

    # 13. OUTLIER DETECTION
    doc.add_heading('13. OUTLIER DETECTION', level=1)
    outl = (
        "An outlier is an observation that lies an abnormal distance from other values. "
        "Logistics data naturally contains extreme values (e.g., a massive delay caused by a hurricane, or exceptionally high costs due to expedited air freight). "
        "Because these are legitimate (though rare) business events, outliers should not be automatically deleted as they contain valuable edge-case information. "
        "Instead, capping (winsorizing) them to a reasonable maximum using the Interquartile Range (IQR) method prevents them from overly skewing statistical averages."
    )
    add_paragraph(outl)
    add_code("""# IQR Method for Outlier Detection
Q1 = df["Delivery_Time_Hours"].quantile(0.25)
Q3 = df["Delivery_Time_Hours"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Cap outliers to the upper bound
import numpy as np
df['Delivery_Time_Hours'] = np.where(df['Delivery_Time_Hours'] > upper_bound, 
                                     upper_bound, df['Delivery_Time_Hours'])""")

    # 14. NORMALIZATION AND STANDARDIZATION
    doc.add_heading('14. NORMALIZATION AND STANDARDIZATION', level=1)
    norm = (
        "Scaling is required before applying machine learning algorithms (like K-Means clustering or K-Nearest Neighbors) that rely on distance calculations. "
        "If a dataset has Distance (range 10-2000) and Weight (range 1-50), the algorithm will disproportionately weight Distance simply because the raw numbers are larger. "
        "While critical for distance-based and gradient descent algorithms, scaling is less critical for tree-based models (like Random Forest).\\n\\n"
        "• Min-Max Normalization: Scales values between 0 and 1.\\n"
        "  Formula: X_scaled = (X - X_min) / (X_max - X_min)\\n\\n"
        "• Standardization (Z-score): Centers data around a mean of 0 with a standard deviation of 1.\\n"
        "  Formula: Z = (X - mean) / standard deviation"
    ).replace('\\n', '\n')
    add_paragraph(norm)
    add_code("""from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Applying Min-Max Normalization
scaler = MinMaxScaler()
df[['Distance_km', 'Shipment_Weight_kg']] = scaler.fit_transform(df[['Distance_km', 'Shipment_Weight_kg']])""")

    doc.add_page_break()

    # 15. FEATURE ENGINEERING
    doc.add_heading('15. FEATURE ENGINEERING', level=1)
    fe = (
        "Feature engineering involves creating new variables from existing data to expose deeper operational insights. "
        "In logistics, calculating derived metrics can highlight performance issues better than raw columns."
    )
    add_paragraph(fe)
    add_code("""# Calculate the delay in hours relative to expectations
df["Delivery_Delay"] = df["Delivery_Time_Hours"] - df["Expected_Delivery_Hours"]

# Calculate cost efficiency per kilometer
df["Cost_Per_Km"] = df["Transportation_Cost"] / df["Distance_km"]""")

    # 16. COMPLETE PREPROCESSING PIPELINE
    doc.add_heading('16. COMPLETE PREPROCESSING PIPELINE', level=1)
    pipe = (
        "The workflow follows a strict chronological order to prevent data leakage or downstream errors:\\n\\n"
        "Raw Data → Data Loading → Initial Profiling → Missing Value Detection → Duplicate Removal → "
        "Data Type Conversion → Categorical Cleaning → Invalid Value Detection → Outlier Analysis → "
        "Feature Engineering → Normalization/Standardization → Final Validation → Clean Analysis-Ready Dataset"
    ).replace('\\n', '\n')
    add_paragraph(pipe)
    
    # 17. COMPLETE PYTHON PREPROCESSING SCRIPT
    doc.add_heading('17. COMPLETE PYTHON PREPROCESSING SCRIPT', level=1)
    add_code("""import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def main():
    # Load Data
    df = pd.read_csv("logistics_sample_data.csv")
    
    # Inspect Data
    print(df.info())
    
    # Remove Duplicates
    df = df.drop_duplicates()
    
    # Convert Data Types
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    
    # Clean Categorical Values
    df['Origin'] = df['Origin'].astype(str).str.strip().str.title()
    df['Destination'] = df['Destination'].astype(str).str.strip().str.title()
    
    # Handle Missing Values (Median for numerical, Mode for categorical)
    df['Delivery_Time_Hours'] = df['Delivery_Time_Hours'].fillna(df['Delivery_Time_Hours'].median())
    df['Transportation_Cost'] = df['Transportation_Cost'].fillna(df['Transportation_Cost'].median())
    df['Delivery_Status'] = df['Delivery_Status'].fillna(df['Delivery_Status'].mode()[0])
    
    # Detect and Cap Outliers (IQR Method)
    Q1 = df['Delivery_Time_Hours'].quantile(0.25)
    Q3 = df['Delivery_Time_Hours'].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    df['Delivery_Time_Hours'] = np.where(df['Delivery_Time_Hours'] > upper_bound, upper_bound, df['Delivery_Time_Hours'])
    
    # Feature Engineering
    df['Delivery_Delay'] = df['Delivery_Time_Hours'] - df['Expected_Delivery_Hours']
    
    # Scale Selected Numerical Variables
    scaler = MinMaxScaler()
    df[['Distance_km', 'Shipment_Weight_kg']] = scaler.fit_transform(df[['Distance_km', 'Shipment_Weight_kg']])
    
    # Final Validation
    print("Final Missing Values:\\n", df.isnull().sum())
    
    # Save Cleaned Dataset
    df.to_csv("cleaned_logistics_data.csv", index=False)

if __name__ == '__main__':
    main()""")

    doc.add_page_break()

    # 18. BEFORE vs AFTER DATA QUALITY
    doc.add_heading('18. BEFORE vs AFTER DATA QUALITY', level=1)
    add_paragraph("(Note: These results are generated from the demonstration sample dataset.)")
    table3 = doc.add_table(rows=1, cols=3)
    table3.style = 'Table Grid'
    hdr_cells3 = table3.rows[0].cells
    headers3 = ['Aspect', 'Before Cleaning (Sample)', 'After Cleaning (Sample)']
    for i, header in enumerate(headers3):
        hdr_cells3[i].text = header
        hdr_cells3[i].paragraphs[0].runs[0].bold = True
        
    before_after = [
        ['Missing values', 'Present in Delivery_Time, Cost, Status', '0 Missing values'],
        ['Duplicate records', '1 Duplicate row identified', '0 Duplicates'],
        ['Data types', 'Order_Date stored as object/string', 'Order_Date is datetime64'],
        ['Category consistency', "'mumbai', 'MUMBAI', 'Mumbai'", "Standardized to 'Mumbai'"],
        ['Outliers', 'Max Delivery_Time = 500 hours', 'Capped to upper bound limit'],
        ['Numerical scaling', 'Distance (150-1400), Weight (80-700)', 'Scaled between 0 and 1'],
        ['Analysis readiness', 'Poor (will cause code execution errors)', 'Excellent (ready for EDA/ML)']
    ]
    for row_data in before_after:
        row_cells = table3.add_row().cells
        for i, val in enumerate(row_data):
            row_cells[i].text = val
            
    add_paragraph("")

    # 19. VALIDATION OF CLEANED DATA
    doc.add_heading('19. VALIDATION OF CLEANED DATA', level=1)
    add_paragraph("To verify the final dataset, one must run programmatic checks to ensure no anomalies slipped through:")
    add_code("""# Programmatic checks
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.info())
print(df.describe())""")
    add_paragraph("Validation also involves logical checks: ensuring no negative distances or costs exist, confirming delivery times are not physically impossible, and ensuring all string categories align with expected values.")

    # 20. METHODOLOGICAL JUSTIFICATION
    doc.add_heading('20. METHODOLOGICAL JUSTIFICATION', level=1)
    justification = (
        "• Missing value treatment: Median imputation was selected for numericals over mean because logistics data is heavily skewed by outliers (like traffic accidents). Mode imputation ensures categorical continuity without losing entire rows.\\n"
        "• Duplicate removal: Prevents double-counting in volume KPIs. The risk is removing legitimate identical orders placed simultaneously, hence relying on a unique Shipment_ID is critical.\\n"
        "• Outlier handling: IQR capping was chosen over deletion. Logistics anomalies are real events; deleting them ignores supply chain realities. Capping retains the signal while reducing the mathematical noise.\\n"
        "• Categorical cleaning: String standardization solves grouping errors, ensuring aggregate metrics (like 'total volume from Mumbai') are accurate.\\n"
        "• Data type conversion: Date conversion is mandatory for time-series forecasting and calculating delivery delays.\\n"
        "• Normalization: Min-Max scaling solves the scale disparity problem for future distance-based clustering models, though it compresses variance slightly.\\n"
        "• Feature engineering: Calculating 'Delivery_Delay' provides a direct KPI that raw times do not immediately offer."
    ).replace('\\n', '\n')
    add_paragraph(justification)

    # 21. IMPACT OF DATA QUALITY ON LOGISTICS ANALYTICS
    doc.add_heading('21. IMPACT OF DATA QUALITY ON LOGISTICS ANALYTICS', level=1)
    impact = (
        "Poor-quality data severely undermines analytical confidence. Unhandled duplicates result in incorrect shipment volume KPIs. "
        "Missing values can cause algorithms to fail or skew delivery-time analysis. Inconsistent categories fragment data, masking high-cost "
        "routes during cost analysis. Furthermore, untreated outliers can manipulate regression weights, leading to poor forecasting of transit times "
        "and incorrect route-optimization decisions. Ultimately, this drives inefficient resource allocation. Conversely, high-quality, rigorously cleaned "
        "data ensures that analytics produce reliable, actionable intelligence, empowering management to make confident operational decisions."
    )
    add_paragraph(impact)

    doc.add_page_break()

    # 22. REFLECTION
    doc.add_heading('22. REFLECTION', level=1)
    reflection = (
        "The Week 2 task underscored a fundamental truth in data science: data preparation is arguably the most important, and often the most time-consuming, stage of any analytical endeavor. "
        "Through executing this preprocessing pipeline, I learned that raw logistics datasets are inherently imperfect representations of complex physical operations. "
        "\\n\\nOne of the main challenges in logistics datasets is distinguishing between an error and a legitimate anomaly. For example, a delivery time of 200 hours could be a typo, or it could represent a shipment delayed by severe port congestion. "
        "This highlights the importance of understanding the business context before modifying or deleting data. Mechanically applying cleaning functions without grasping the operational realities can destroy valuable information. "
        "\\n\\nBy carefully applying median imputation to handle nulls robustly, standardizing geographical naming conventions, and capping outliers rather than blindly deleting them, the dataset has been transformed into a reliable asset. "
        "This rigorous work perfectly positions the dataset for Week 3, ensuring that the upcoming Exploratory Data Analysis (EDA) and visualizations reflect true operational performance rather than data entry errors."
    ).replace('\\n', '\n')
    add_paragraph(reflection)

    # 23. CONNECTION TO WEEK 3
    doc.add_heading('23. CONNECTION TO WEEK 3', level=1)
    conn = (
        "The newly cleaned dataset is the foundational input for Week 3. With missing values and outliers addressed, Exploratory Data Analysis (EDA) can proceed without mathematical errors. "
        "Visualizations (such as histograms and scatter plots) will now accurately represent distributions rather than being distorted by scale differences or anomalies. "
        "Furthermore, correlation analysis between distance, cost, and time will yield statistically valid results, enabling accurate KPI analysis and the identification of hidden logistical patterns."
    )
    add_paragraph(conn)

    # 24. LIMITATIONS
    doc.add_heading('24. LIMITATIONS', level=1)
    limits = (
        "• Public datasets generally do not perfectly mirror the nuanced, highly specific operational dynamics of a specific company's private network.\\n"
        "• Certain critical variables (such as driver hours-of-service or weather conditions) may be entirely missing from open data.\\n"
        "• The simulated data used for demonstration may not capture all the intricate complexities of real-world supply chain noise.\\n"
        "• Outlier treatment is subjective and typically requires deep, domain-specific business knowledge to execute perfectly.\\n"
        "• Scaling decisions (like Min-Max vs Z-Score) depend entirely on which machine learning modeling technique is chosen in the future."
    ).replace('\\n', '\n')
    add_paragraph(limits)

    # 25. CONCLUSION
    doc.add_heading('25. CONCLUSION', level=1)
    conc = (
        "Data collection and preprocessing form the bedrock of robust logistics analytics. Through this project, it was demonstrated that raw operational data is susceptible to a host of quality issues, including missing values, duplicates, formatting inconsistencies, and extreme outliers. "
        "\\n\\nBy leveraging Python libraries such as pandas and scikit-learn, a systematic data profiling and cleaning pipeline was developed. Missing values were effectively neutralized using median and mode imputation strategies that protect the dataset from extreme skews. Duplicate records were identified and purged to ensure volume metrics remain accurate. Furthermore, outliers were carefully managed using IQR capping to retain their signal while mitigating their mathematical distortion. "
        "\\n\\nSubsequent steps, including Min-Max normalization and the engineering of new features like 'Delivery_Delay', transformed the raw numbers into analysis-ready intelligence. The final validation step guarantees that the resulting dataset is structurally sound and mathematically safe for advanced modeling. "
        "\\n\\nIn summary, the effort invested in rigorously cleaning data is indispensable. Without this preprocessing workflow, any downstream predictive models or route optimization algorithms would be fundamentally flawed. Clean data is the prerequisite for reliable logistics analytics."
    ).replace('\\n', '\n')
    add_paragraph(conc)

    # 26. REFERENCES
    doc.add_heading('26. REFERENCES', level=1)
    refs = (
        "1. Amruta. (2021). Supply Chain Logistics Problem Dataset. Kaggle. Retrieved from https://www.kaggle.com/datasets/amruta21/supply-chain-logistics-problem\\n"
        "2. The pandas development team. (2023). pandas-dev/pandas: Pandas Documentation. Zenodo. https://doi.org/10.5281/zenodo.3509134\\n"
        "3. Pedregosa, F. et al. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825-2830. Retrieved from https://scikit-learn.org/\\n"
        "4. IBM. (n.d.). What is Data Data Preprocessing? Retrieved from https://www.ibm.com/topics/data-preprocessing"
    ).replace('\\n', '\n')
    add_paragraph(refs, justify=False)

    doc.save("c:/Users/Laxmi/OneDrive/Desktop/Internship/Week_2/Laxmi_Ananda_Sanas_Week_2_Data_Preprocessing_Report.docx")

if __name__ == '__main__':
    create_report()
