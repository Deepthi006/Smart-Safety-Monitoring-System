import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

# Initialize Firebase only if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# --- THE CRITICAL FIX IS THIS FUNCTION DEFINITION ---
def log_event(event_type, details, risk_level):
    """
    Logs a security event to Firebase Firestore.
    Arguments must match the names used in main.py exactly.
    """
    try:
        db.collection("logs").add({
            "timestamp": datetime.now(),
            "event_type": event_type,
            "details": details,
            "risk_level": risk_level
        })
    except Exception as e:
        print(f"Failed to log event: {e}")

def fetch_history():
    try:
        docs = db.collection("logs") \
            .order_by("timestamp", direction=firestore.Query.DESCENDING) \
            .stream()

        rows = []
        for d in docs:
            r = d.to_dict()
            # Convert timestamp to readable string
            if "timestamp" in r:
                r["timestamp"] = r["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
            rows.append(r)

        return rows
    except Exception as e:
        print(f"Error fetching history: {e}")
        return []