# HR-Employee-Contribution-Model

live link: 

```mermaid
graph TD
    A[Start] --> B{Run `streamlit run app.py`};
    B --> C[Application Initializes];
    C --> D[Load AdaBoost Model via Joblib];
    C --> E[Display UI with Sidebar Navigation];

    subgraph "User Interaction"
        E --> F{User Selects Page};
        F -- "Home" --> G[Display Welcome Page];
        F -- "About" --> H[Display Project Information];
        F -- "🔮 Predict Churn" --> I[Display Prediction Form];
    end

    subgraph "Prediction Process"
        I --> J[User Fills Employee Details];
        J --> K[User Clicks "Predict Churn"];
        K --> L[Preprocess Data into DataFrame];
        L --> M[Model Makes Prediction];
        M --> N{Display Result};
        N -- "Churn" --> O[Show Error Box with Confidence %];
        N -- "Stay" --> P[Show Success Box with Confidence %];
    end

    G --> F;
    H --> F;
    P --> F;
    O --> F;

```
