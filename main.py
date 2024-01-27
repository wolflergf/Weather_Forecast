import streamlit as st

st.title("Weater Forecast for the next days")
st.markdown("### Enter the city name and country code to get the weather forecast")
place = st.text_input(
    "Enter the city name and country code separated by comma (e.g. London, GB)"
)
days = st.slider(
    "Forecast for the next how many days?",
    min_value=1,
    max_value=5,
    help="Select the number of days for which you want to see the forecast",
)
option = st.selectbox("Select data view", ("Temperature", "Sky"))
st.subheader("{} for the next {} days in {}".format(option, days, place))
