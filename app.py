import streamlit as st
import base64
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Employee Churn Predictor",
    page_icon="✨",
    layout="wide", # Using a wider layout for a more modern feel
    initial_sidebar_state="expanded",
)

# --- INJECT CUSTOM CSS ---
# New, refreshed CSS for a light, modern theme
css = """
/* --- General App Styling --- */
body {
    color: #333; /* Darker text for readability */
}

/* --- Main Content Area --- */
.stApp {
    background-color: #F0F2F6; /* Light grey background */
}

/* --- Sidebar Styling --- */
[data-testid="stSidebar"] {
    background-color: #FFFFFF; /* White sidebar */
    border-right: 1px solid #e6e6e6;
}

[data-testid="stSidebar"] .st-emotion-cache-17lntkn {
    color: #333333;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    margin: 0.1rem 0;
    transition: background-color 0.2s, color 0.2s;
    font-size: 1.0em;
    font-weight: 500;
}

/* Sidebar Navigation Links - Hover effect */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn:hover {
    background-color: #F0F2F6;
    color: #0068C9;
}

/* Sidebar Navigation Links - Active page */
[data-testid="stSidebar"] .st-emotion-cache-1aehpv3 {
    background-color: #E3F2FD; /* Light blue for active page */
    color: #0068C9; /* Dark blue text for active page */
    font-weight: 600;
}

/* Sidebar Success Box */
[data-testid="stSidebar"] [data-testid="stAlert"] {
    background-color: #E3F2FD;
    color: #0068C9;
    border-radius: 0.5rem;
}

/* --- Button Styling --- */
.stButton>button {
    background-color: #0068C9;
    color: #FFFFFF;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.1s;
    box-shadow: 0 4px 14px 0 rgba(0, 118, 255, 0.39);
}

.stButton>button:hover {
    background-color: #0056b3;
    transform: translateY(-1px);
}

.stButton>button:active {
    transform: translateY(1px);
    box-shadow: 0 2px 8px 0 rgba(0, 118, 255, 0.39);
}

/* --- SUCCESS/ERROR BOXES in Main Area --- */
[data-testid="stAlert"] {
    border-radius: 0.5rem;
    border-left: 5px solid;
}

[data-testid="stSuccess"] {
    border-color: #28a745;
}

[data-testid="stError"] {
    border-color: #dc3545;
}

/* --- Footer Styling --- */
.footer {
    text-align: center;
    color: #888;
    font-size: 0.9em;
    padding: 20px 0;
}
"""
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# --- MAIN PAGE CONTENT ---
st.title("✨ Welcome to the Employee Churn Predictor")
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
# Note: The time zone is set to IST (India Standard Time) as requested in a previous interaction.
st.markdown(f"---")
st.markdown(f"<div class='footer'>© {current_year} Employee Churn Predictor | Built with Streamlit</div>", unsafe_allow_html=True)
st.markdown(f"<div class='footer'>Current Time (IST): {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}</div>", unsafe_allow_html=True)

