import streamlit as st
import base64
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Employee Churn Predictor",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- INJECT CUSTOM CSS ---
# All CSS is now embedded directly in the app script
css = """
/* General App Styling */
.stApp {
    background-color: #f0f2f6;
}

/* --- SIDEBAR STYLING --- */

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #0c0c3a;
    color: #ffffff;
}

/* Sidebar Navigation Links */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn {
    padding: 1rem 1.5rem;
    border-radius: 0.5rem;
    margin: 0.2rem 0;
    transition: background-color 0.3s, color 0.3s;
    font-size: 1.1em;
    font-weight: 500;
}

/* Sidebar Navigation Links - Hover effect */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn:hover {
    background-color: #4a4a7f;
    color: #ffffff;
}

/* Sidebar Navigation Links - Active page */
[data-testid="stSidebar"] .st-emotion-cache-1aehpv3 {
    background-color: #2a2a68;
}

/* --- BUTTON STYLING --- */
.stButton>button {
    background-color: #0c0c3a;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}

.stButton>button:hover {
    background-color: #2a2a68;
}

/* --- SUCCESS/ERROR BOXES --- */
[data-testid="stSuccess"] {
    border-left: 5px solid #0c0c3a;
    background-color: #e6e6fa;
}

[data-testid="stError"] {
    border-left: 5px solid #990000;
    background-color: #ffe6e6;
}
"""
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# --- MAIN PAGE CONTENT ---
st.title("🚀 Welcome to the Employee Churn Predictor")
st.sidebar.success("Select a page from the navigation menu.")

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
    
    Select a page from the navigation bar on the left to get started.
    """
)

# --- FOOTER ---
current_year = datetime.datetime.now().year
st.markdown(f"---")
st.markdown(f"<div style='text-align: center; color: grey;'>© {current_year} Employee Churn Predictor | Built with Streamlit</div>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: center; color: grey;'>Current Time in India: {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p IST')}</div>", unsafe_allow_html=True)

