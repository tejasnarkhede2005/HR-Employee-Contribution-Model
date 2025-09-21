import streamlit as st
import pickle
import pandas as pd
import numpy as np

# --- PAGE CONFIG for this specific page ---
st.set_page_config(page_title="Predict Churn", page_icon="🔮", layout="wide")


# --- APPLY THEME FROM app.py ---
# This is a little trick to keep the styling consistent across pages
try:
    with open('app.py', 'r') as f:
        code = f.read()
        css_block = code.split('css = """')[1].split('"""')[0]
        st.markdown(f'<style>{css_block}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Could not find app.py to load styles. Styles may not be applied correctly.")


# --- LOAD THE MODEL ---
try:
    with open('AdaBoost_best_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file 'AdaBoost_best_model.pkl' not found. Please ensure it's in the root directory.")
    st.stop()
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    st.stop()

# --- PAGE TITLE AND DESCRIPTION ---
st.title("🔮 Predict Employee Churn")
st.markdown("Enter the employee's details below to get a churn prediction.")

# --- CREATE INPUT FIELDS FOR THE MODEL ---
# Using columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Personal & Financial")
    Age = st.number_input("Age", min_value=18, max_value=70, value=30, step=1)
    MonthlyIncome = st.number_input("Monthly Income ($)", min_value=1000, max_value=20000, value=5000, step=100)
    DailyRate = st.number_input("Daily Rate ($)", min_value=100, max_value=1500, value=800, step=10)
    HourlyRate = st.number_input("Hourly Rate ($)", min_value=30, max_value=100, value=65, step=1)
    PercentSalaryHike = st.number_input("Percent Salary Hike (%)", min_value=10, max_value=25, value=15, step=1)
    Gender = st.selectbox("Gender", ["Male", "Female"])
    MaritalStatus = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])


with col2:
    st.subheader("Job & Role Information")
    TotalWorkingYears = st.number_input("Total Working Years", min_value=0, max_value=40, value=10, step=1)
    YearsAtCompany = st.number_input("Years at Company", min_value=0, max_value=40, value=5, step=1)
    NumCompaniesWorked = st.number_input("Number of Companies Worked", min_value=0, max_value=10, value=2, step=1)
    DistanceFromHome = st.number_input("Distance From Home (km)", min_value=1, max_value=30, value=10, step=1)
    Department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
    JobRole = st.selectbox("Job Role", [
        "Sales Executive", "Research Scientist", "Laboratory Technician",
        "Manufacturing Director", "Healthcare Representative", "Manager",
        "Sales Representative", "Research Director", "Human Resources"
    ])
    OverTime = st.selectbox("Overtime", ["Yes", "No"])
    BusinessTravel = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])


# --- Sliders for satisfaction and involvement in a separate section ---
st.markdown("---")
st.subheader("Ratings & Satisfaction (1 = Low, 4 = High)")
s_col1, s_col2, s_col3 = st.columns(3)

with s_col1:
    EnvironmentSatisfaction = st.slider("Environment Satisfaction", 1, 4, 3)
    JobSatisfaction = st.slider("Job Satisfaction", 1, 4, 3)
    RelationshipSatisfaction = st.slider("Relationship Satisfaction", 1, 4, 3)

with s_col2:
    JobInvolvement = st.slider("Job Involvement", 1, 4, 3)
    PerformanceRating = st.slider("Performance Rating", 1, 4, 3)
    WorkLifeBalance = st.slider("Work Life Balance", 1, 4, 3)
    
with s_col3:
    StockOptionLevel = st.slider("Stock Option Level", 0, 3, 1)
    TrainingTimesLastYear = st.slider("Training Times Last Year", 0, 6, 2)
    Education = st.slider("Education Level", 1, 5, 3)


st.markdown("---")
# --- PREDICTION BUTTON ---
if st.button("Predict Churn", type="primary"):
    # ... (Rest of the prediction logic from previous steps) ...
    # This is the same data processing logic as before
    input_data = {
        'Age': Age, 'DailyRate': DailyRate, 'DistanceFromHome': DistanceFromHome,
        'Education': Education, 'EnvironmentSatisfaction': EnvironmentSatisfaction,
        'HourlyRate': HourlyRate, 'JobInvolvement': JobInvolvement,
        'JobSatisfaction': JobSatisfaction, 'MonthlyIncome': MonthlyIncome,
        'NumCompaniesWorked': NumCompaniesWorked, 'PercentSalaryHike': PercentSalaryHike,
        'PerformanceRating': PerformanceRating, 'RelationshipSatisfaction': RelationshipSatisfaction,
        'StockOptionLevel': StockOptionLevel, 'TotalWorkingYears': TotalWorkingYears,
        'TrainingTimesLastYear': TrainingTimesLastYear, 'WorkLifeBalance': WorkLifeBalance,
        'YearsAtCompany': YearsAtCompany, 'YearsInCurrentRole': 0, # Assuming 0, can be added as input
        'YearsSinceLastPromotion': 0, # Assuming 0, can be added as input
        'YearsWithCurrManager': 0, # Assuming 0, can be added as input
        'Department_Human Resources': 1 if Department == 'Human Resources' else 0,
        'Department_Research & Development': 1 if Department == 'Research & Development' else 0,
        'Department_Sales': 1 if Department == 'Sales' else 0,
        'EducationField_Human Resources': 0, 'EducationField_Life Sciences': 0, 'EducationField_Marketing': 0,
        'EducationField_Medical': 0, 'EducationField_Other': 0, 'EducationField_Technical Degree': 0,
        'Gender_Female': 1 if Gender == 'Female' else 0, 'Gender_Male': 1 if Gender == 'Male' else 0,
        'JobRole_Healthcare Representative': 1 if JobRole == 'Healthcare Representative' else 0,
        'JobRole_Human Resources': 1 if JobRole == 'Human Resources' else 0,
        'JobRole_Laboratory Technician': 1 if JobRole == 'Laboratory Technician' else 0,
        'JobRole_Manager': 1 if JobRole == 'Manager' else 0,
        'JobRole_Manufacturing Director': 1 if JobRole == 'Manufacturing Director' else 0,
        'JobRole_Research Director': 1 if JobRole == 'Research Director' else 0,
        'JobRole_Research Scientist': 1 if JobRole == 'Research Scientist' else 0,
        'JobRole_Sales Executive': 1 if JobRole == 'Sales Executive' else 0,
        'JobRole_Sales Representative': 1 if JobRole == 'Sales Representative' else 0,
        'MaritalStatus_Divorced': 1 if MaritalStatus == 'Divorced' else 0,
        'MaritalStatus_Married': 1 if MaritalStatus == 'Married' else 0,
        'MaritalStatus_Single': 1 if MaritalStatus == 'Single' else 0,
        'OverTime_No': 1 if OverTime == 'No' else 0, 'OverTime_Yes': 1 if OverTime == 'Yes' else 0,
        'BusinessTravel_Non-Travel': 1 if BusinessTravel == 'Non-Travel' else 0,
        'BusinessTravel_Travel_Frequently': 1 if BusinessTravel == 'Travel_Frequently' else 0,
        'BusinessTravel_Travel_Rarely': 1 if BusinessTravel == 'Travel_Rarely' else 0,
        'EmployeeCount': 1, 'StandardHours': 80, 'Over18_Y': 1
    }

    model_features = ['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EmployeeCount',
       'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement',
       'JobSatisfaction', 'MonthlyIncome', 'NumCompaniesWorked', 'Over18_Y',
       'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
       'StandardHours', 'StockOptionLevel', 'TotalWorkingYears',
       'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
       'YearsInCurrentRole', 'YearsSinceLastPromotion',
       'YearsWithCurrManager', 'BusinessTravel_Non-Travel',
       'BusinessTravel_Travel_Frequently', 'BusinessTravel_Travel_Rarely',
       'Department_Human Resources', 'Department_Research & Development',
       'Department_Sales', 'EducationField_Human Resources',
       'EducationField_Life Sciences', 'EducationField_Marketing',
       'EducationField_Medical', 'EducationField_Other',
       'EducationField_Technical Degree', 'Gender_Female', 'Gender_Male',
       'JobRole_Healthcare Representative', 'JobRole_Human Resources',
       'JobRole_Laboratory Technician', 'JobRole_Manager',
       'JobRole_Manufacturing Director', 'JobRole_Research Director',
       'JobRole_Research Scientist', 'JobRole_Sales Executive',
       'JobRole_Sales Representative', 'MaritalStatus_Divorced',
       'MaritalStatus_Married', 'MaritalStatus_Single', 'OverTime_No',
       'OverTime_Yes']

    input_df = pd.DataFrame([input_data]).reindex(columns=model_features, fill_value=0)
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error(f"This employee is likely to **CHURN**. (Confidence: {prediction_proba[0][1]*100:.2f}%)", icon="🚨")
    else:
        st.success(f"This employee is likely to **STAY**. (Confidence: {prediction_proba[0][0]*100:.2f}%)", icon="✅")
