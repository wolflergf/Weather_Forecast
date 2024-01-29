""" This is the main file for the Streamlit application """
# Importing the required module
import streamlit as st
import plotly.express as px

# Setting the title of the application
st.title("Weather Forecast for the next days")

# Taking input from the user for the city name and country code
# The input should be in the format 'City, Country Code'
place = st.text_input(
    "Enter the city name and country code separated by comma (e.g. London, GB)"
)

# Taking input from the user for the number of days for the forecast
# The user can select a number between 1 and 5 using a slider
days = st.slider(
    "Forecast for the next how many days?",
    min_value=1,
    max_value=5,
    help="Select the number of days for which you want to see the forecast",
)

# Providing options to the user for the type of data they want to view
# The user can select between 'Temperature' and 'Sky'
option = st.selectbox("Select data view", ("Temperature", "Sky"))

# Displaying the selected options to the user
st.subheader("{} for the next {} days in {}".format(option, days, place))


def get_data(days):
    dates = ["2021-01-01", "2021-01-02", "2021-01-03"]
    temperatures = [10, 12, 17]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)


fig = px.line(
    x=d,
    y=t,
    labels={"x": "Date", "y": "Temperature (C°)"},
)
st.plotly_chart(fig)
