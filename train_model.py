# src/feature_engine.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

class FeatureEngine:
    def __init__(self, model_dir="models"):
        self.model_dir = model_dir
        self.scaler = StandardScaler()
        self.le_city = LabelEncoder()
        os.makedirs(self.model_dir, exist_ok=True)

    def create_features(self, df, training=False):
        """Creates machine-readable features."""
        
        # 1. Cyclical Time Encoding (Better than raw numbers)
        df['hour_sin'] = np.sin(2 * np.pi * df['hour']/24)
        df['hour_cos'] = np.cos(2 * np.pi * df['hour']/24)

        # 2. City Encoding
        if training:
            df['city_encoded'] = self.le_city.fit_transform(df['City'])
            joblib.dump(self.le_city, os.path.join(self.model_dir, "city_encoder.pkl"))
        else:
            # Handle prediction (load existing encoder)
            try:
                self.le_city = joblib.load(os.path.join(self.model_dir, "city_encoder.pkl"))
                # Use a safe transform (map unknown cities to -1)
                df['city_encoded'] = df['City'].apply(
                    lambda x: self.le_city.transform([x])[0] if x in self.le_city.classes_ else -1
                )
            except:
                df['city_encoded'] = 0 # Fallback
        
        # Return only the columns needed for AI
        features = df[['hour_sin', 'hour_cos', 'city_encoded', 'Victim Age', 'month', 'dayofweek']].copy()
        return features.fillna(0)

    def scale_data(self, X, training=False):
        """Scales data to 0-1 range (Crucial for KMeans)."""
        if training:
            X_scaled = self.scaler.fit_transform(X)
            joblib.dump(self.scaler, os.path.join(self.model_dir, "scaler.pkl"))
        else:
            try:
                self.scaler = joblib.load(os.path.join(self.model_dir, "scaler.pkl"))
                X_scaled = self.scaler.transform(X)
            except:
                X_scaled = X # Fallback
        return X_scaled