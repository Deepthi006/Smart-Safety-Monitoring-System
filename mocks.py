import streamlit as st
import base64
import os
import time

def play_alert_sound(sound_path="assets/alert.mp3"):
    """
    Plays the audio file.
    """
    # Check if audio is enabled in session state (supports your 'sound_on' or the new 'audio_alert')
    if not st.session_state.get("audio_alert", True) and not st.session_state.get("sound_on", True):
        return

    if not os.path.exists(sound_path):
        return

    try:
        with open(sound_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()

        # HTML5 Audio Player (Hidden)
        st.markdown(f"""
            <audio autoplay>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        print(f"Error playing sound: {e}")

def check_and_play_alert(msg, last_alert_time):
    """
    Checks if enough time (3 seconds) has passed since the last alert 
    before playing it again.
    """
    current_time = time.time()
    
    # If there is a threat message
    if msg:
        # Check 3-second cooldown
        if (current_time - last_alert_time) > 3:
            play_alert_sound()
            return current_time  # Return new timestamp
            
    return last_alert_time  # Return old timestamp (no change)