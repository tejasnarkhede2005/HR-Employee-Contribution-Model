import streamlit as st
import base64
import datetime

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Employee Churn Predictor",
    page_icon="🌙",
    layout="wide", 
    initial_sidebar_state="expanded",
)

# --- INJECT CUSTOM CSS ---
# New, refreshed CSS for a sleek, modern dark theme
css = """
/* --- General App Styling --- */
body {
    color: #E0E0E0; /* Light text for readability on dark background */
}

/* --- Main Content Area --- */
.stApp {
    background-color: #121212; /* A common, comfortable dark background */
}

h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF; /* Brighter white for headers */
}

/* --- Sidebar Styling --- */
[data-testid="stSidebar"] {
    background-color: #1E1E1E; /* Slightly lighter dark for the sidebar */
    border-right: 1px solid #2E2E2E;
}

[data-testid="stSidebar"] .st-emotion-cache-17lntkn {
    color: #E0E0E0;
    padding: 0.75rem 1.5rem;
    border-radius: 0.5rem;
    margin: 0.1rem 0;
    transition: background-color 0.2s, color 0.2s;
    font-size: 1.0em;
    font-weight: 500;
}

/* Sidebar Navigation Links - Hover effect */
[data-testid="stSidebar"] .st-emotion-cache-17lntkn:hover {
    background-color: #333333;
    color: #FFFFFF;
}

/* Sidebar Navigation Links - Active page */
[data-testid="stSidebar"] .st-emotion-cache-1aehpv3 {
    background-color: #007ACC; /* Vibrant blue for active page */
    color: #FFFFFF; 
    font-weight: 600;
}

/* Sidebar Success Box */
[data-testid="stSidebar"] [data-testid="stAlert"] {
    background-color: rgba(0, 122, 204, 0.2);
    color: #00A2FF;
    border-radius: 0.5rem;
    border: 1px solid #007ACC;
}

/* --- Button Styling --- */
.stButton>button {
    background-color: #007ACC;
    color: #FFFFFF;
    border: none;
    padding: 12px 24px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.1s, box-shadow 0.3s;
    box-shadow: 0 0 15px rgba(0, 122, 204, 0.5);
}

.stButton>button:hover {
    background-color: #008DD1;
    transform: translateY(-2px);
    box-shadow: 0 0 25px rgba(0, 122, 204, 0.7);
}

.stButton>button:active {
    transform: translateY(0px);
    box-shadow: 0 0 10px rgba(0, 122, 204, 0.5);
}

/* --- SUCCESS/ERROR BOXES in Main Area --- */
[data-testid="stAlert"] {
    border-radius: 0.5rem;
    border-left: 5px solid;
    background-color: #1E1E1E; /* Match sidebar bg */
}

[data-testid="stSuccess"] {
    border-color: #28a745;
    color: #28a745;
}

[data-testid="stError"] {
    border-color: #dc3545;
    color: #dc3545;
}

/* --- Footer Styling --- */
.footer {
    text-align: center;
    color: #6c6c6c; /* Lighter grey for footer text */
    font-size: 0.9em;
    padding: 20px 0;
}
"""
st.markdown(f"<style>{css}</style>", unsafe_html=True)


# --- MAIN PAGE CONTENT ---
st.title("🌙 Welcome to the Employee Churn Predictor")
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
st.markdown(f"<div class='footer'>© {current_year} Employee Churn Predictor | Built with Streamlit</div>", unsafe_html=True)
st.markdown(f"<div class='footer'>Current Time (IST): {datetime.datetime.now().strftime('%d %B %Y, %I:%M %p')}</div>", unsafe_html=True)

