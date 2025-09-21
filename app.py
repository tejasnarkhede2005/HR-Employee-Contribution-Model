import streamlit as st
import datetime
import pickle
import pandas as pd
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Employee Churn Predictor",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- INJECT CUSTOM CSS ---
# A modern "Glassmorphism" theme with a background gradient
css = """
/* --- General App Styling & Gradient Background --- */
.stApp {
    background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
    color: #E0E0E0;
}

h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3); /* Add shadow to text for depth */
}

/* --- Glassmorphism Effect for Containers --- */
[data-testid="stSidebar"], .main .block-container {
    background: rgba(255, 255, 255, 0.08); /* Semi-transparent white */
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px); /* For Safari */
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}

/* Specific adjustments for main content area to have glass effect */
.main .block-container {
    padding: 2rem 3rem;
    margin-top: 2rem;
}

/* --- Sidebar Styling --- */
[data-testid="stSidebar"] {
    padding-top: 2rem;
}

/* Make radio buttons look like nav links */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn {
    color: #E0E0E0;
    padding: 0.75rem 1.5rem;
    border-radius: 10px;
    margin: 0.1rem 0;
    transition: background-color 0.3s, color 0.3s;
    font-size: 1.0em;
    font-weight: 500;
    background-color: transparent;
}

/* Radio buttons - Hover effect */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: #FFFFFF;
}

/* Radio buttons - Active selection */
[data-testid="stSidebar"] .st-emotion-cache-1aehpv3 {
    background: linear-gradient(90deg, #1D976C, #93F9B9);
    color: #0f0c29;
    font-weight: 700;
}

/* --- Button Styling --- */
.stButton>button {
    color: #FFFFFF;
    border: none;
    padding: 12px 24px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
    background: linear-gradient(90deg, #1D976C, #93F9B9);
    box-shadow: 0 4px 15px 0 rgba(29, 151, 108, 0.4);
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 7px 20px 0 rgba(29, 151, 108, 0.6);
}

.stButton>button:active {
    transform: translateY(0px);
}

/* --- SUCCESS/ERROR BOXES in Main Area --- */
[data-testid="stAlert"] {
    border-radius: 10px;
    border-left: 5px solid;
    background-color: rgba(0,0,0,0.2);
}

[data-testid="stSuccess"] {
    border-color: #28a745;
    color: #93F9B9;
}

[data-testid="stError"] {
    border-color: #e43a4b;
    color: #ff8a96;
}

/* --- Footer Styling --- */
.footer {
    text-align: center;
    color: #a0a0a0;
    font-size: 0.9em;
    padding: 10px 0;
}
"""
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# --- LOAD THE MODEL (CACHED) ---
@st.cache_resource
def load_model():
    try:
        with open('AdaBoost_best_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.error("Model file 'AdaBoost_best_model.pkl' not found. Please ensure it's in the root directory.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

model = load_model()


# --- PAGE DEFINITIONS ---

def home_page():
    st.title("💎 Welcome to the Employee Churn Predictor")
    st.markdown(
        """
        This interactive application leverages a machine learning model to predict the likelihood of employee churn within an organization.
        
        **To begin, please navigate to the 'Predict Churn' page using the sidebar menu.**
        
        ### How It Works
        1.  **Input Data**: On the prediction page, enter the relevant details for an employee.
        2.  **Make Prediction**: The underlying AdaBoost model will process this information.
        3.  **View Result**: Instantly receive a prediction indicating whether the employee is likely to stay or leave.
        
        ### About the Model
        - **Model Type:** AdaBoost Classifier
        - **Purpose:** To assist organizations in proactively identifying and retaining valuable employees who may be at risk of leaving.
        """
    )

def prediction_page():
    if model is None:
        st.warning("Model is not loaded. Prediction functionality is unavailable.")
        return

    st.title("🔮 Predict Employee Churn")
    st.markdown("Enter the employee's details below to get a churn prediction.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Personal & Financial")
        Age = st.number_input("Age", 18, 70, 30)
        MonthlyIncome = st.number_input("Monthly Income ($)", 1000, 20000, 5000)
        DailyRate = st.number_input("Daily Rate ($)", 100, 1500, 800)
        HourlyRate = st.number_input("Hourly Rate ($)", 30, 100, 65)
        PercentSalaryHike = st.number_input("Percent Salary Hike (%)", 10, 25, 15)
        Gender = st.selectbox("Gender", ["Male", "Female"])
        MaritalStatus = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])

    with col2:
        st.subheader("Job & Role Information")
        TotalWorkingYears = st.number_input("Total Working Years", 0, 40, 10)
        YearsAtCompany = st.number_input("Years at Company", 0, 40, 5)
        NumCompaniesWorked = st.number_input("Num of Companies Worked", 0, 10, 2)
        DistanceFromHome = st.number_input("Distance From Home (km)", 1, 30, 10)
        Department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])
        JobRole = st.selectbox("Job Role", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"])
        OverTime = st.selectbox("Overtime", ["Yes", "No"])
        BusinessTravel = st.selectbox("Business Travel", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"])

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
    if st.button("Predict Churn", type="primary"):
        input_data = {
            'Age': Age, 'DailyRate': DailyRate, 'DistanceFromHome': DistanceFromHome, 'Education': Education,
            'EnvironmentSatisfaction': EnvironmentSatisfaction, 'HourlyRate': HourlyRate, 'JobInvolvement': JobInvolvement,
            'JobSatisfaction': JobSatisfaction, 'MonthlyIncome': MonthlyIncome, 'NumCompaniesWorked': NumCompaniesWorked,
            'PercentSalaryHike': PercentSalaryHike, 'PerformanceRating': PerformanceRating, 'RelationshipSatisfaction': RelationshipSatisfaction,
            'StockOptionLevel': StockOptionLevel, 'TotalWorkingYears': TotalWorkingYears, 'TrainingTimesLastYear': TrainingTimesLastYear,
            'WorkLifeBalance': WorkLifeBalance, 'YearsAtCompany': YearsAtCompany, 'YearsInCurrentRole': 0,
            'YearsSinceLastPromotion': 0, 'YearsWithCurrManager': 0,
            'Department_Human Resources': 1 if Department == 'Human Resources' else 0,
            'Department_Research & Development': 1 if Department == 'Research & Development' else 0,
            'Department_Sales': 1 if Department == 'Sales' else 0, 'EducationField_Human Resources': 0,
            'EducationField_Life Sciences': 0, 'EducationField_Marketing': 0, 'EducationField_Medical': 0,
            'EducationField_Other': 0, 'EducationField_Technical Degree': 0,
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
            'MaritalStatus_Married': 1 if MaritalStatus == 'Married' else 0, 'MaritalStatus_Single': 1 if MaritalStatus == 'Single' else 0,
            'OverTime_No': 1 if OverTime == 'No' else 0, 'OverTime_Yes': 1 if OverTime == 'Yes' else 0,
            'BusinessTravel_Non-Travel': 1 if BusinessTravel == 'Non-Travel' else 0,
            'BusinessTravel_Travel_Frequently': 1 if BusinessTravel == 'Travel_Frequently' else 0,
            'BusinessTravel_Travel_Rarely': 1 if BusinessTravel == 'Travel_Rarely' else 0,
            'EmployeeCount': 1, 'StandardHours': 80, 'Over18_Y': 1
        }
        model_features = model.feature_names_in_
        input_df = pd.DataFrame([input_data]).reindex(columns=model_features, fill_value=0)
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        st.subheader("Prediction Result")
        if prediction[0] == 1:
            st.error(f"This employee is likely to CHURN. (Confidence: {prediction_proba[0][1]*100:.2f}%)", icon="🚨")
        else:
            st.success(f"This employee is likely to STAY. (Confidence: {prediction_proba[0][0]*100:.2f}%)", icon="✅")

def about_page():
    st.title("ℹ️ About This Project")
    st.markdown("""
        This application is an **Employee Churn Predictor** built using Streamlit, designed with a modern glassmorphism interface.

        ### Purpose
        The primary goal is to provide an intuitive and visually appealing tool for managers and HR professionals to predict employee attrition. By inputting key employee metrics, the application uses a pre-trained AdaBoost machine learning model to generate a churn likelihood score.

        ### Technology Stack
        - **Backend & Model:** Python, Scikit-learn (AdaBoost Classifier)
        - **Frontend:** Streamlit with custom CSS for styling.
        - **Data Handling:** Pandas, NumPy.

        ### How to Use
        1.  Navigate to the **Predict Churn** page from the sidebar.
        2.  Fill in the employee's details across the different sections.
        3.  Click the 'Predict Churn' button at the bottom.
        4.  The model's prediction and its confidence level will be displayed instantly.
        """)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Home", "🔮 Predict Churn", "ℹ️ About"])

if page == "Home":
    home_page()
elif page == "🔮 Predict Churn":
    prediction_page()
elif page == "ℹ️ About":
    about_page()

# --- FOOTER ---
current_year = datetime.datetime.now().year
st.markdown(f"---")
st.markdown(f"<div class='footer'>© {current_year} Employee Churn Predictor | Built with Streamlit</div>", unsafe_allow_html=True)

