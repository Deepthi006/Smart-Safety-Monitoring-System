import numpy as np

class MockBox: 
    def __init__(self, cls_id=0): 
        self.conf = 0.9
        self.cls = np.array([cls_id]) # Mock Class ID

class MockResult:
    def __init__(self): 
        self.boxes = [MockBox(0), MockBox(0), MockBox(67)] # 2 Persons, 1 Cell Phone
    def plot(self): return np.zeros((480, 640, 3), dtype=np.uint8)

class MockModelEngine: 
    def train(self, df): return df

def mock_detect_threat(frame, model):
    return MockResult(), None, 0

def mock_fetch_history():
    return [
        {"Timestamp": "2025-12-20 09:15:00", "Module": "System", "Event": "System Startup", "Status": "Success"},
        {"Timestamp": "2025-12-20 09:20:15", "Module": "Surveillance", "Event": "Camera Activated", "Status": "Active"},
    ]