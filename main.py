import streamlit as st
import streamlit.components.v1 as components

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {"meter": 1, "kilometer": 0.001, "centimeter": 100, "mile": 0.000621371, "inch": 39.3701},
        "Weight": {"kilogram": 1, "gram": 1000, "pound": 2.20462, "ounce": 35.274},
        "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * conversions[category][to_unit] / conversions[category][from_unit]

# Add custom CSS for better styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stApp {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .stButton>button {
            background-color:rgb(3, 14, 3);
            color: white;
            border-radius: 5px;
            padding: 10px;
        }
        .stButton>button:hover {
            background-color:rgb(2, 10, 2);
        }
    </style>
""", unsafe_allow_html=True)

st.title("Unit Converter")
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])
from_unit = st.selectbox("From Unit", list(convert_units(1, "meter", "kilometer", "Length").keys()) if category != "Temperature" else ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("To Unit", list(convert_units(1, "meter", "kilometer", "Length").keys()) if category != "Temperature" else ["Celsius", "Fahrenheit", "Kelvin"])
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"Converted Value: {result} {to_unit}")


    

