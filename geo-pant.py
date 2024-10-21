import streamlit as st
from datetime import datetime
import geopy
from geopy.geocoders import Nominatim

# Placeholder data for soil types and average temperatures
# Real implementation should use appropriate APIs or datasets
soil_data = {
    '33.7075, 73.2112': 'Silt Loam',
    '34.0, 74.0': 'Clay Loam',  # Add more coordinates and soil types as needed
}

temperature_data = {
    'January': 15,
    'February': 17,
    'March': 23,
    'April': 28,
    'May': 34,
    'June': 37,
    'July': 35,
    'August': 34,
    'September': 33,
    'October': 30,
    'November': 23,
    'December': 17,
}

# Placeholder vegetable data for each month
vegetables_data = {
    'January': ['Spinach', 'Carrot', 'Beetroot'],
    'February': ['Lettuce', 'Peas', 'Radish'],
    'March': ['Tomatoes', 'Cucumber', 'Pepper'],
    'April': ['Cucumbers', 'Squash', 'Zucchini'],
    'May': ['Okra', 'Eggplant', 'Sweet Corn'],
    'June': ['Chili', 'Eggplant', 'Pumpkin'],
    'July': ['Cucumber', 'Spinach', 'Basil'],
    'August': ['Carrots', 'Spinach', 'Turnips'],
    'September': ['Broccoli', 'Cauliflower', 'Carrots'],
    'October': ['Radish', 'Spinach', 'Garlic'],
    'November': ['Lettuce', 'Cabbage', 'Carrots'],
    'December': ['Peas', 'Garlic', 'Onions'],
}

# Function to get soil type based on coordinates (example logic)
def get_soil_type(lat, lon):
    key = f'{round(lat, 4)}, {round(lon, 4)}'
    return soil_data.get(key, 'Unknown')

# Function to get average temperature for the current month
def get_avg_temperature():
    current_month = datetime.now().strftime('%B')
    return temperature_data.get(current_month, 'Data not available')

# Function to get vegetables to plant for the current month
def get_vegetables():
    current_month = datetime.now().strftime('%B')
    return vegetables_data.get(current_month, 'Data not available')

# Streamlit app interface
st.title("Soil, Temperature, and Vegetable Suggestions")

# User input: coordinates
st.write("Enter the coordinates of your location:")
lat = st.number_input("Latitude", format="%.6f", value=33.7075)
lon = st.number_input("Longitude", format="%.6f", value=73.2112)

# Get soil type, temperature, and vegetables
if st.button("Get Information"):
    soil_type = get_soil_type(lat, lon)
    avg_temp = get_avg_temperature()
    vegetables = get_vegetables()

    # Display results
    st.write(f"**Soil Type**: {soil_type}")
    st.write(f"**Average Temperature (for this month)**: {avg_temp} °C")
    st.write(f"**Vegetables to Plant this Month**: {', '.join(vegetables)}")
