from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
import pandas as pd

# App banao
app = FastAPI(title='Customer Churn Prediction API')

# Model load karo
with open('model/churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Feature names load karo
with open('model/feature_names.json', 'r') as f:
    feature_names = json.load(f)

# Input format define karo
class CustomerData(BaseModel):
    tenure: int
    MonthlyCharges: float
    TotalCharges: float

# Home route
@app.get('/')
def home():
    return {'message': 'Churn Prediction API is running!'}

# Predict route
@app.post('/predict')
def predict(data: CustomerData):
    input_dict = dict(data)
    input_df = pd.DataFrame([input_dict], columns=feature_names).fillna(0)
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    
    return {
        'churn': bool(prediction),
        'probability': round(float(probability), 2),
        'message': 'Customer will churn!' if prediction == 1 else 'Customer will stay!'
    }