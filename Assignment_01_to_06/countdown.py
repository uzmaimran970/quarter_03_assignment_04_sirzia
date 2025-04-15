import streamlit as st
import time

# Countdown function
def countdown(seconds):
    while seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        # Display countdown in Streamlit
        st.write(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    st.write("Time's up!")

# Streamlit UI
st.title("⏳ Countdown Timer")

# Input for the user to set the timer
seconds = st.number_input("Enter the time in seconds:", min_value=1, max_value=3600, value=10)

# Start button to trigger countdown
if st.button("Start Countdown"):
    countdown(seconds)
