import streamlit as st
from datetime import datetime

# Placeholder data for soil types and average temperatures based on District and Tehsil
soil_data = {
    ('Islamabad', 'Rural'): 'Silt Loam',
    ('Rawalpindi', 'Gujar Khan'): 'Clay Loam',
    ('Lahore', 'Shalimar'): 'Sandy Loam',
    # Add more District and Tehsil combinations as needed
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

# Function to get soil type based on District and Tehsil
def get_soil_type(district, tehsil):
    return soil_data.get((district, tehsil), 'Unknown')

# Function to get average temperature for the current month
def get_avg_temperature():
    current_month = datetime.now().strftime('%B')
    return temperature_data.get(current_month, 'Data not available')

# Function to get vegetables to plant for the current month
def get_vegetables():
    current_month = datetime.now().strftime('%B')
    return vegetables_data.get(current_month, 'Data not available')

# Streamlit app interface
st.title("Soil, Temperature, and Vegetable Suggestions by District and Tehsil")

# User input: District and Tehsil
st.write("Enter the District and Tehsil of your location:")
district = st.selectbox("District", options=['Islamabad', 'Rawalpindi', 'Lahore'])  # Add more districts
tehsil = st.selectbox("Tehsil", options=['Rural', 'Gujar Khan', 'Shalimar'])  # Add corresponding tehsils

# Get soil type, temperature, and vegetables
if st.button("Get Information"):
    soil_type = get_soil_type(district, tehsil)
    avg_temp = get_avg_temperature()
    vegetables = get_vegetables()

    # Display results
    st.write(f"**Soil Type in {tehsil}, {district}**: {soil_type}")
    st.write(f"**Average Temperature (for this month)**: {avg_temp} °C")
    st.write(f"**Vegetables to Plant this Month**: {', '.join(vegetables)}")
