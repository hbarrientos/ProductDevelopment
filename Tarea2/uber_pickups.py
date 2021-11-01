import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)



"""
# Uber pickups exercise
"""
URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'
#URL = "uber-raw-data-sep14.csv"

@st.cache(suppress_st_warning=True)
def download_data():
    return pd.read_csv(URL)

nrow = st.sidebar.slider("No. rows to display:", 0, 10000, value = 1000)
hour_range = st.sidebar.slider("Select a range hour:", 0, 24, (8, 17))
st.sidebar.write("Hours selected:", hour_range[0], hour_range[1])
data = (download_data()
        #.iloc[1:nrow]
        .rename(columns={"Date/Time":"date_time", "Lat":"lat", "Lon":"lon", "Base":"base"})
        .assign(date_time= lambda df:pd.to_datetime(df.date_time))
        .loc[lambda df: (df.date_time.dt.hour >= hour_range[0]) & (df.date_time.dt.hour < hour_range[1]) ]
        .loc[1:nrow]
        .sort_values(by='date_time')
        )
data

st.map(data)

# Order el data frame por fecha/hora elegida
# Agregar Histograma de las horas, plot de grafica o histograma cuantos viajes hay a cada hora

fig = plt.figure(figsize=(10, 4))
plt.hist(pd.DataFrame({'hour': data['date_time'].dt.hour}))
st.balloons()
st.pyplot(fig)


