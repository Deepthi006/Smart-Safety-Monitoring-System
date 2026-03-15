import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data
def process_data(file, _model_engine=None):
    # 1. Load Data
    df_raw = pd.read_csv(file)
    
    # 2. Basic Cleaning
    if "Victim Gender" in df_raw.columns:
        df_raw["Victim Gender"] = df_raw["Victim Gender"].fillna("Not Mentioned").replace("", "Not Mentioned")
        df_women = df_raw[df_raw["Victim Gender"] == "F"].copy()
    else:
        df_women = df_raw.copy()

    # 3. AI Processing (get Clusters/Anomalies if available)
    if _model_engine:
        try:
            df_processed = _model_engine.train(df_women)
        except Exception as e:
            st.error(f"AI Engine Error: {e}")
            df_processed = df_women
    else:
        df_processed = df_women

    # ========================================================
    # 4. SAFETY SCORE CALCULATION (The Fix)
    # ========================================================
    
    # A. Crime Frequency Penalty (More crimes = Lower Safety)
    # Count crimes per city
    city_counts = df_processed['City'].value_counts()
    max_crimes = city_counts.max() if not city_counts.empty else 1
    min_crimes = city_counts.min() if not city_counts.empty else 0
    
    # Calculate penalty (0 to 30 points based on volume)
    def get_freq_penalty(city):
        count = city_counts.get(city, 0)
        if max_crimes == min_crimes: return 0
        return ((count - min_crimes) / (max_crimes - min_crimes)) * 30

    df_processed['freq_penalty'] = df_processed['City'].apply(get_freq_penalty)

    # B. Time Penalty (Night crimes are riskier)
    # Parse hour if valid, else default to noon (safe)
    if 'Time of Occurrence' in df_processed.columns:
        # handle various time formats slightly robustly
        temp_time = pd.to_datetime(df_processed['Time of Occurrence'], format='%H:%M', errors='coerce')
        df_processed['hour_temp'] = temp_time.dt.hour.fillna(12)
    elif 'hour' in df_processed.columns:
         df_processed['hour_temp'] = df_processed['hour']
    else:
        df_processed['hour_temp'] = 12

    # -10 points if crime was between 10 PM (22) and 5 AM (5)
    df_processed['time_penalty'] = df_processed['hour_temp'].apply(
        lambda h: 15 if (h >= 22 or h <= 5) else 0
    )

    # C. Calculate Final Score
    # Base Score 100 (Perfect) - Penalties
    df_processed['safety_score'] = 100 - df_processed['freq_penalty'] - df_processed['time_penalty']
    
    # Add a tiny bit of random jitter (0-2%) so bars aren't visually identical for same-tier cities
    df_processed['safety_score'] -= np.random.uniform(0, 2, size=len(df_processed))
    
    # Ensure limits 0-100
    df_processed['safety_score'] = df_processed['safety_score'].clip(0, 100)

    # Cleanup temporary cols
    cols_to_drop = ['freq_penalty', 'time_penalty', 'hour_temp']
    df_processed.drop(columns=[c for c in cols_to_drop if c in df_processed.columns], inplace=True)

    return df_raw, df_processed