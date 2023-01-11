import streamlit as st
import plotly.express as px
import backend

st.title("Weather Forcast for next Few Days")

cityName = st.text_input(label="Enter City Name :",key="CityName")

slidVal = st.slider(label="Number Days Forcast",
                    min_value=1,max_value=5,
                    key="SilderValue",
                    help="Select the number of forecasted days")
option = st.selectbox(label="Select Data to view",
                      options=["Temperature","Sky"],
                      key="NevMenu")

if cityName:
    st.subheader(f"{option} for next {slidVal} days in {cityName} :")

    data = backend.get_data(cityName,slidVal)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in data]
        dates = [dict["dt_txt"] for dict in data]
        figure = px.line(x = dates,y=temperatures,labels={"x":"Dates","y":"Temperatures in (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {'Clear':"images/clear.png",'Clouds':"images/cloud.png",'Rain':"images/rain.png",'Snow':"images/snow.png"}
        skies = [dict["weather"][0]["main"] for dict in data]
        image_path = [images[condition] for condition in skies]
        st.image(image_path,width=115)
        