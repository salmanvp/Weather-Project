import streamlit as st
import requests
API_KEY="bda51fe47d881a95297f4abe1c86ee94"


def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin-273.15


def find_current_weather(city):
    base_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    weather_data=requests.get(base_url).json()
    # st.json(weather_data)
    try:
        genaral=weather_data['weather'][0]['main']
        icon_id=weather_data['weather'][0]['icon']
        icon=f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        temperature=round(convert_to_celcius(weather_data['main']['temp']))
        descriptions=weather_data['weather'][0]['description']
        name=weather_data['name']
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return genaral,temperature,icon,descriptions,name



def main():
    st.header("Find the Weather")
    city=st.text_input("Enter The City")
    if st.button("Find"):
        general,Temperature,icon,descriptions,name=find_current_weather(city)
        col_1,col_2=st.columns(2)
        with col_1:
            st.write(name)
            st.metric(label="Temperature", value=f"{Temperature}°C")
            st.write(descriptions)
        with col_2:
            st.write(general)
            st.image(icon)


    
if __name__=="__main__":
    main()