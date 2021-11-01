import streamlit as st
import numpy as np
import pandas as pd

st.title("This is my first app from Galileo master")

x=4
st.write(x, "^2 = ", x*x)

st.write("This is a Data frame")
st.write(pd.DataFrame({"Column A": ["A", "B", "C", "D", "E"],  "Column B": [1,2,3,4,5]}))

"""
# Title: This is a title tag
This is other example for data frames
"""
df = pd.DataFrame({"Column A": ["A", "B", "C", "D", "E"],  "Column B": [1,2,3,4,5]})
df

"""
## Show me some graphs
"""
df_to_plot= pd.DataFrame(np.random.randn(20,3), columns=["Column A", "Column B", "Column C"])
st.line_chart(df_to_plot)

"""
## Let's plot a map!
### a continuacion las columnas SE DEBEN LLAMAR ASI lat y lon
"""
df_lat_lon = pd.DataFrame(np.random.randn(1000, 2)/[50,50] + [37.76, -122.4], columns=["lat", "lon"]) 
st.map(df_lat_lon)

if st.checkbox("show dataframe"):
    df_lat_lon

"""
## Let's try some widgets

### 1. Slider
"""
x = st.slider("Select a value for X", min_value=1, max_value=100)
y = st.slider("Select a power for Y", min_value=0, max_value=5)
st.write(x, "power", y, "is:", x**y)

"""
### What about options
"""
def test():
    st.write("Funcion ejecutada :)")
option_list=range(1,11)
option = st.selectbox("Which number do you like best?", option_list)
st.write("Your favorite number is:", option)

"""
### How about a progress bar
"""
import time
label = st.empty()
progress_bar = st.progress(0)
for i in range(0, 101):
    label.text(f"The proccess is: {i}%")
    progress_bar.progress(i)
    time.sleep(0.01)
"The wait is done!"


st.sidebar.write("This is a sidebar")
option_side = st.sidebar.selectbox("Select a slide number", option_list)
st.sidebar.write("The selection is ", option_side)

st.sidebar.write("Another slider")
another_slider = st.sidebar.slider("Select Range", 0.0, 100.0, (25.0,75.0))
st.sidebar.write("El nuevo valor del rango:", another_slider)










#streamlit run first_app.py