import streamlit as st
import base64
import datetime

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

/* Sidebar Navigation Links - Hover effect */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn:hover {
    background-color: rgba(255, 255, 255, 0.1);
    color: #FFFFFF;
}

/* Sidebar Navigation Links - Active page */
[data-testid="stSidebar"] .st-emotion-cache-1aehpv3 {
    background: linear-gradient(90deg, #1D976C, #93F9B9);
    color: #0f0c29;
    font-weight: 700;
}

/* Sidebar Success Box */
[data-testid="stSidebar"] [data-testid="stAlert"] {
    background-color: rgba(29, 151, 108, 0.2);
    color: #93F9B9;
    border-radius: 10px;
    border: 1px solid #1D976C;
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
    padding: 20px 0;
}
"""
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# --- MAIN PAGE CONTENT ---
st.title("💎 Welcome to the Employee Churn Predictor")
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
# Note: The time zone is set to IST (India Standard Time).
st.markdown(f"---")
st.markdown(f"<div class='footer'>© {current_year} Employee Churn Predictor | Built with Streamlit</div>", unsafe_allow_html=True)
st.markdown(f"<div class='footer'>Current Time (IST): {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}</div>", unsafe_allow_html=True)

