import streamlit as st
import pandas as pd
import pickle
from PIL import Image


with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.image("Screenshot 2024-07-25 185502.png")
st.sidebar.title("Input Features")
st.sidebar.markdown("Please fill in the following details:")

age = st.sidebar.number_input('Age', min_value=18, max_value=100, value=30)

location = st.sidebar.radio('Location', ['Urban', 'Suburban', 'Rural'])

diet_type = st.sidebar.radio('Diet Type', ['Mostly Plant-Based', 'Balanced', 'Mostly Animal-Based'])

local_food_freq = st.sidebar.radio('Local Food Frequency', ['Always', 'Often', 'Sometimes', 'Rarely'])

transportation_mode = st.sidebar.radio('Transportation Mode', ['Bike', 'Public Transit', 'Car', 'Walk'])

energy_source = st.sidebar.radio('Energy Source', ['Renewable', 'Mixed', 'Non-Renewable'])

home_type = st.sidebar.radio('Home Type', ['Apartment', 'House'])

clothing_freq = st.sidebar.radio('Clothing Frequency', ['Always', 'Often', 'Sometimes', 'Rarely'])

sustainable_brands = st.sidebar.checkbox('Prefer Sustainable Brands', value=True)

community_involvement = st.sidebar.radio('Community Involvement', ['High', 'Moderate', 'Low'])

gender = st.sidebar.radio('Gender', ['Female', 'Male', 'Non-Binary'])

using_plastic_products = st.sidebar.radio('Using Plastic Products', ['Never', 'Rarely', 'Sometimes', 'Often'])

disposal_methods = st.sidebar.radio('Disposal Methods', ['Composting', 'Recycling', 'Landfill', 'Combination'])

physical_activities = st.sidebar.radio('Physical Activities', ['High', 'Moderate', 'Low'])

home_size = st.sidebar.number_input('Home Size (sqft)', min_value=100, max_value=10000, value=1500)

environmental_awareness = st.sidebar.slider('Environmental Awareness (1-5)', min_value=1, max_value=5, value=3)

monthly_electricity_consumption = st.sidebar.number_input('Monthly Electricity Consumption (kWh)', min_value=0, max_value=10000, value=250)

monthly_water_consumption = st.sidebar.number_input('Monthly Water Consumption (liters)', min_value=0, max_value=100000, value=3000)


st.title("🌍 Sustainability Rating Prediction")
st.subheader("By Shravan Kumar Polu")
st.markdown(
    """
    Welcome to the Sustainability Rating Prediction app. This tool helps you predict the sustainability rating
    based on various lifestyle factors. Please provide your inputs in the sidebar, and the predicted rating will be displayed below.
    """
)

# Display an image (optional)
image = Image.open('Social-Sustainability-5-Principles-Thumb.png')  # Replace with your own image path
st.image(image, caption='Sustainable Living', use_column_width=True)

# Create a dataframe with input data
input_data = pd.DataFrame({
    'Age': [age],
    'Location': [location],
    'DietType': [diet_type],
    'LocalFoodFrequency': [local_food_freq],
    'TransportationMode': [transportation_mode],
    'EnergySource': [energy_source],
    'HomeType': [home_type],
    'HomeSize': [home_size],
    'ClothingFrequency': [clothing_freq],
    'SustainableBrands': [sustainable_brands],
    'EnvironmentalAwareness': [environmental_awareness],
    'CommunityInvolvement': [community_involvement],
    'MonthlyElectricityConsumption': [monthly_electricity_consumption],
    'MonthlyWaterConsumption': [monthly_water_consumption],
    'Gender': [gender],
    'UsingPlasticProducts': [using_plastic_products],
    'DisposalMethods': [disposal_methods],
    'PhysicalActivities': [physical_activities]
})

# Prediction button
if st.button("Predict"):
    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display the prediction
    st.subheader("Predicted Sustainability Rating")
    st.write(f"Your predicted sustainability rating is: **{prediction}**")

    # Display the corresponding rating definition
    st.subheader("Sustainability Rating Definitions")
    if prediction == 5:
        st.markdown(
            """
            **Rating 5: Exceptionally Sustainable**
            - **Description**: Practices exceptional sustainability, deeply committed to environmental preservation.
            - **Examples**: Uses 100% renewable energy, avoids plastic products, participates in community sustainability initiatives, has a low carbon footprint.
            """
        )
    elif prediction == 4:
        st.markdown(
            """
            **Rating 4: Highly Sustainable**
            - **Description**: Strong focus on eco-friendly practices with concerted efforts to reduce environmental impact.
            - **Examples**: Uses a mix of renewable and non-renewable energy, engages in recycling and composting, chooses sustainable brands, has high environmental awareness.
            """
        )
    elif prediction == 3:
        st.markdown(
            """
            **Rating 3: Moderately Sustainable**
            - **Description**: Makes some efforts to live sustainably, with room for improvement.
            - **Examples**: Uses mixed energy sources, participates in recycling, occasionally chooses sustainable options, has moderate environmental awareness.
            """
        )
    elif prediction == 2:
        st.markdown(
            """
            **Rating 2: Low Sustainability**
            - **Description**: Practices low levels of sustainability with minimal focus on environmental considerations.
            - **Examples**: Relies on non-renewable energy, rarely recycles, low participation in community initiatives, minimal environmental awareness.
            """
        )
    elif prediction == 1:
        st.markdown(
            """
            **Rating 1: Unsustainable**
            - **Description**: Engages in unsustainable practices with significant negative environmental impact.
            - **Examples**: Uses non-renewable energy, consistently uses plastic, irresponsible waste disposal, high resource consumption, minimal environmental awareness.
            """
        )
st.markdown("---")
st.markdown("© 2024 Shravan Kumar Polu")
