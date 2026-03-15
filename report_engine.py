# src/data_loader.py

import pandas as pd
import streamlit as st

class DataLoader:
    def __init__(self):
        # Columns we absolutely need
        self.required_columns = ["City", "Date of Occurrence", "Time of Occurrence", "Victim Gender"]

    def load_data(self, uploaded_file):
        """Loads CSV and performs basic validation."""
        try:
            df = pd.read_csv(uploaded_file)
            
            # Check for missing columns
            missing = [col for col in self.required_columns if col not in df.columns]
            if missing:
                st.error(f"❌ Invalid CSV. Missing columns: {missing}")
                return None
            
            return df
        except Exception as e:
            st.error(f"Error loading data: {e}")
            return None

    def preprocess_data(self, df):
        """Extracts Hour, Month, Day for all records."""
        # Convert Date
        df["Date of Occurrence"] = pd.to_datetime(df["Date of Occurrence"], errors="coerce")
        
        # Convert Time to Hour
        df["hour"] = pd.to_datetime(df["Time of Occurrence"], errors="coerce", format="%H:%M").dt.hour
        df["hour"] = df["hour"].fillna(12.0) # Default to noon if missing
        
        # Extract Month/Day
        df["month"] = df["Date of Occurrence"].dt.month
        df["dayofweek"] = df["Date of Occurrence"].dt.dayofweek
        
        # Drop rows where date was invalid
        df = df.dropna(subset=["month", "dayofweek"])
        return df

    def get_female_data(self, df):
        """Returns only female victim records."""
        if "Victim Gender" in df.columns:
            return df[df["Victim Gender"] == "F"].copy()
        return df