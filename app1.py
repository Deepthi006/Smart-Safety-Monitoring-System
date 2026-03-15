🛡️ Women Safety Analytics & Smart Surveillance System
📌 Project Overview

Women Safety Analytics is an AI-powered system designed to analyze crime data related to women, identify high-risk locations, detect abnormal crime patterns, and provide real-time surveillance alerts using Computer Vision.
The project combines Machine Learning, Anomaly Detection, and Deep Learning-based Object Detection to support proactive safety planning and decision-making.

🎯 Objectives

Analyze crimes committed against women using historical data

Identify unsafe zones using clustering techniques

Detect unusual or extreme crime patterns

Calculate a Safety Score (0–100) for locations

Provide real-time threat detection using live surveillance

Visualize insights through dashboards and heatmaps

🧠 System Architecture
Historical Crime Data
        ↓
Exploratory Data Analysis (EDA)
        ↓
Feature Engineering & Scaling
        ↓
KMeans Clustering ──→ Risk Zones
        ↓
Isolation Forest ──→ Anomaly Detection
        ↓
Rule-Based Logic ──→ Safety Score (0–100)
        ↓
Dashboard | Heatmaps | Reports

Live Camera Feed
        ↓
YOLO Object Detection
        ↓
Threat Identification
        ↓
Real-Time Alerts

🛠️ Technologies Used
🔹 Programming & Frameworks

Python

Streamlit (Web Dashboard)

OpenCV (Camera Processing)

🔹 Machine Learning & AI

KMeans Clustering (Risk Zone Identification)

Isolation Forest (Anomaly Detection)

YOLO (You Only Look Once) – Real-Time Object Detection

🔹 Data & Visualization

Pandas, NumPy

Plotly (Charts & Graphs)

Folium (Geospatial Heatmaps)

🔹 Storage & Utilities

Joblib (Model Persistence)

CSV-based datasets

Firebase (Event Logging – optional)

📂 Project Structure
women-safety-analytics/
│
├── data/
│   └── processed_women_safety.csv
│
├── models/
│   ├── kmeans_model.pkl
│   ├── isolation_forest.pkl
│   ├── scaler.pkl
│   └── city_encoder.pkl
│
├── notebooks/
│   └── women_safety_eda.ipynb
│
├── src/
│   ├── model_engine.py
│   ├── yolo_engine.py
│   ├── analytics_engine.py
│   ├── alert_engine.py
│   └── utils.py
│
├── app.py
├── requirements.txt
└── README.md

📊 Machine Learning Models Explained
1️⃣ KMeans Clustering

Groups crime incidents based on time, age, and location

Identifies high, medium, and low-risk zones

Works without labeled data (unsupervised learning)

2️⃣ Isolation Forest

Detects unusual or abnormal crime incidents

Flags rare but dangerous patterns

Used to penalize safety scores

3️⃣ YOLO (You Only Look Once)

Real-time object detection from camera feed

Detects people, crowds, and weapons

Enables instant alerts for unsafe situations

🔢 Safety Score Calculation

The safety score ranges from 0 (very unsafe) to 100 (very safe).

Logic Used:

Start with score = 100

Night-time crime → −20

Anomaly detected → −30

Higher risk cluster → −(cluster × 5)

Final score clipped between 0 and 100

✔ Lower score = Higher danger
✔ Higher score = Safer area

📈 Key Features

📍 City-wise safety ranking

🔥 Risk heatmaps

📊 Crime analytics dashboard

🎥 Live surveillance monitoring

🚨 Real-time alerts

📄 Downloadable reports

🧠 Saved ML models for reuse

🚀 How to Run the Project
🔹 Install Dependencies
pip install -r requirements.txt

🔹 Run the Dashboard
streamlit run app.py

📌 Applications

Smart city safety systems

Police patrolling optimization

Women safety monitoring platforms

Urban crime analytics

Academic & research use

⚠️ Limitations

Depends on quality of crime data

Requires camera hardware for live surveillance

Cannot predict crimes with 100% accuracy

Real-time deployment requires computational resources

🔮 Future Enhancements

Behavior-based threat detection

SOS mobile app integration

Face recognition for offender tracking

Cloud-based city-scale deployment

Predictive crime forecasting models

👨‍💻 Author

Mohan Kiran
B.Tech – Computer Science Engineering
AI | Machine Learning | Data Analytics

⭐ Final Note

This project demonstrates how AI, data analytics, and real-time surveillance can be combined to move from reactive policing to proactive women safety systems.
