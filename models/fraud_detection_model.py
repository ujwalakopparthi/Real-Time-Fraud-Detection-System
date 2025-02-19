from sklearn.ensemble import IsolationForest
import pandas as pd

def train_isolation_forest(data):
    model = IsolationForest(contamination=0.05)
    model.fit(data)
    return model

def predict_fraud(model, data):
    return model.predict(data)
