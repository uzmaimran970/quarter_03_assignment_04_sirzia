import streamlit as st

st.title("💪 BMI Calculator")

# Sidebar inputs
st.sidebar.header("Enter your Details:")

# Use number_input for manual entry instead of slider
height = st.sidebar.number_input("Enter your height (in cm):", min_value=100, max_value=250, value=175)
weight = st.sidebar.number_input("Enter your weight (in kg):", min_value=40, max_value=200, value=70)

# BMI calculation
height_m = height / 100
bmi = weight / (height_m ** 2)

# BMI category
if bmi < 18.5:
    category = "Underweight"
    color = "blue"
elif 18.5 <= bmi < 24.9:
    category = "Normal weight"
    color = "green"
elif 25 <= bmi < 29.9:
    category = "Overweight"
    color = "orange"
else:
    category = "Obese"
    color = "red"

# Output
st.subheader("📊 Results")
st.write(f"Height: **{height} cm**")
st.write(f"Weight: **{weight} kg**")
st.markdown(f"<h3 style='color:{color}'>Your BMI is: {bmi:.2f} ({category})</h3>", unsafe_allow_html=True)

st.info("✅ Tip: Maintain a balanced diet and regular exercise for a healthy BMI.")
