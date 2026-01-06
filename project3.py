#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit requests


# In[5]:


import streamlit as st
import requests

st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️")
st.title("🌤️ Weather Forecast Dashboard")

# Input for city
city = st.text_input("Enter City Name")

if city:
    api_key = "8b3739342f069d68252827534d1d9917"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"Weather in {city}")
        st.write(f"🌡️ Temperature: {data['main']['temp']} °C")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
        st.write(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"🌥️ Condition: {data['weather'][0]['description'].title()}")
    else:
        st.error("City not found or API error.")



# In[ ]:





# In[ ]:




