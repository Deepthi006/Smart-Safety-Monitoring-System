# src/gps_engine.py

def get_coords(city_name):
    """
    Returns (lat, lon) for a given city name.
    Uses a local dictionary for speed. Returns None if not found.
    """
    # Normalize input
    if not isinstance(city_name, str):
        return None
    
    city = city_name.strip().lower()

    # Database of Indian City Coordinates
    # Format: "lowercase_name": [latitude, longitude]
    coords_db = {
        "delhi": [28.7041, 77.1025],
        "new delhi": [28.6139, 77.2090],
        "mumbai": [19.0760, 72.8777],
        "bangalore": [12.9716, 77.5946],
        "bengaluru": [12.9716, 77.5946],
        "hyderabad": [17.3850, 78.4867],
        "ahmedabad": [23.0225, 72.5714],
        "chennai": [13.0827, 80.2707],
        "kolkata": [22.5726, 88.3639],
        "surat": [21.1702, 72.8311],
        "pune": [18.5204, 73.8567],
        "jaipur": [26.9124, 75.7873],
        "lucknow": [26.8467, 80.9462],
        "kanpur": [26.4499, 80.3319],
        "nagpur": [21.1458, 79.0882],
        "indore": [22.7196, 75.8577],
        "thane": [19.2183, 72.9781],
        "bhopal": [23.2599, 77.4126],
        "visakhapatnam": [17.6868, 83.2185],
        "patna": [25.5941, 85.1376],
        "vadodara": [22.3072, 73.1812],
        "ghaziabad": [28.6692, 77.4538],
        "ludhiana": [30.9010, 75.8573],
        "agra": [27.1767, 78.0081],
        "nashik": [19.9975, 73.7898],
        "ranchi": [23.3441, 85.3096],
        "meerut": [28.9845, 77.7064],
        "rajkot": [22.3039, 70.8022],
        "kalyan-dombivli": [19.2403, 73.1305],
        "vasai-virar": [19.3919, 72.8397],
        "varanasi": [25.3176, 82.9739],
        "srinagar": [34.0837, 74.7973],
        "aurangabad": [19.8762, 75.3433],
        "dhanbad": [23.7957, 86.4304],
        "amritsar": [31.6340, 74.8723],
        "navi mumbai": [19.0330, 73.0297],
        "allahabad": [25.4358, 81.8463],
        "prayagraj": [25.4358, 81.8463],
        "howrah": [22.5958, 88.2636],
        "gwalior": [26.2183, 78.1828],
        "jabalpur": [23.1815, 79.9864],
        "coimbatore": [11.0168, 76.9558],
        "vijayawada": [16.5062, 80.6480],
        "jodhpur": [26.2389, 73.0243],
        "madurai": [9.9252, 78.1198],
        "raipur": [21.2514, 81.6296],
        "kota": [25.2138, 75.8648],
        "chandigarh": [30.7333, 76.7794],
        "guwahati": [26.1445, 91.7362],
        "solapur": [17.6599, 75.9064],
        "hubli-dharwad": [15.3647, 75.1240],
        "mysore": [12.2958, 76.6394],
        "tiruchirappalli": [10.7905, 78.7047],
        "bareilly": [28.3670, 79.4304],
        "aligarh": [27.8974, 78.0880],
        "tiruppur": [11.1085, 77.3411],
        "gurgaon": [28.4595, 77.0266],
        "gurugram": [28.4595, 77.0266],
        "moradabad": [28.8386, 78.7733],
        "jalandhar": [31.3260, 75.5762],
        "bhubaneswar": [20.2961, 85.8245],
        "salem": [11.6643, 78.1460],
        "warangal": [17.9689, 79.5941],
        "mira-bhayandar": [19.2813, 72.8561],
        "jalgaon": [21.0077, 75.5626],
        "guntur": [16.3067, 80.4365],
        "thiruvananthapuram": [8.5241, 76.9366],
        "bhiwandi": [19.2813, 73.0488],
        "noida": [28.5355, 77.3910],
    }

    # Direct match or partial match fallback
    if city in coords_db:
        return coords_db[city]
    
    # Try finding partial key (e.g. "kanpur nagar" -> "kanpur")
    for key in coords_db:
        if key in city or city in key:
            return coords_db[key]

    return None