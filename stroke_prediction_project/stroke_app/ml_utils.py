import joblib
import pandas as pd
import os

def load_model():
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'stroke_prediction_pipeline.pkl')
    return joblib.load(model_path)

def make_prediction(input_data):
    pipeline = load_model()
    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0][1]  # Probability of stroke
    return prediction, probability