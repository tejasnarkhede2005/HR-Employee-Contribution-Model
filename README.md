# HR-Employee-Contribution-Model

live link: 

```mermaid
graph TD
    A[Start: User runs 'streamlit run app.py'] --> B{Display Home Page};
    B --> C{User interacts with Sidebar Navi};
    
    C --> D[Selects 'Predict Churn' Page];
    D --> E[User fills in employee data form];
    E --> F{Clicks 'Predict Churn' Button};
    F --> G[Load AdaBoost_best_model.pkl];
    G --> H[Preprocess input data];
    H --> I[Model makes prediction];
    I --> J[Display Result: Churn / Stay with Confidence Score];
    
    C --> K[Selects 'About' Page];
    K --> L[Display project information];

    subgraph "Prediction Logic"
        G
        H
        I
        J
    end

    subgraph "Pages"
        B
        D
        K
    end

    J --> C;
    L --> C;

```
