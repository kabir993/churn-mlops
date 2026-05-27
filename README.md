# Customer Churn Prediction — MLOps Project

A production-ready MLOps pipeline to predict customer churn using XGBoost,
served via FastAPI, containerized with Docker, and tracked with MLflow.

---

## Problem Statement

Predict which telecom customers are likely to churn (leave the service),
enabling the business to take proactive retention actions.

- **Dataset:** IBM Telco Customer Churn (7,043 customers, 21 features)
- **Target:** Binary classification — Churn: Yes/No
- **Business Impact:** Retaining a churning customer costs 5x less than acquiring a new one

---

## Project Architecture

Raw Data (CSV)
|
EDA & Visualization
|
Feature Engineering
|
Model Training (XGBoost + SMOTE)
|
Experiment Tracking (MLflow)
|
Model Export (.pkl)
|
REST API (FastAPI)
|
Containerization (Docker)
|
CI/CD Pipeline (GitHub Actions)
|
Model Monitoring (Drift Detection)

---

## Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 77% |
| ROC-AUC | 83% |
| Churn Recall | 84% |
| Cross-Val AUC | 92% |

---

## Tech Stack

| Category | Tools |
|----------|-------|
| ML Model | XGBoost, Scikit-learn, SMOTE |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| API | FastAPI, Uvicorn |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Monitoring | Evidently AI |
| Visualization | Matplotlib, Seaborn, SHAP |

---

## Project Structure


churn-mlops/
├── app/
│   └── main.py
├── model/
│   ├── churn_model.pkl
│   └── feature_names.json
├── notebooks/
│   ├── MLOPS.ipynb
│   └── model_monitoring.ipynb
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── requirements.txt
└── README.md



---

## How to Run

### Run Locally
```bash
pip install -r requirements.txt
cd app
uvicorn main:app --reload
```

### Run with Docker
```bash
docker build -t churn-mlops .
docker run -p 8000:8000 churn-mlops
```

API: `http://localhost:8000`  
Swagger UI: `http://localhost:8000/docs`

---

## API Usage

**Endpoint:** `POST /predict`

**Request:**
```json
{
  "tenure": 2,
  "MonthlyCharges": 85.0,
  "TotalCharges": 170.0
}
```

**Response:**
```json
{
  "churn": true,
  "probability": 0.97,
  "message": "Customer will churn!"
}
```

---

## Key Insights

- Month-to-month contract customers churn the most (~1650)
- New customers (tenure 0-5 months) have highest churn risk
- Higher monthly charges = higher churn probability
- Electronic check payment users churn more than others
- Customers without OnlineSecurity and TechSupport churn more

---

## Author

**Chandan Goswami**  
Data Scientist & MLOps Engineer  
[LinkedIn](https://www.linkedin.com/in/chandan-goswami-3372aa251/) | [GitHub](https://github.com/kabir993)