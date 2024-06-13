import streamlit as st
import yfinance as yf
import numpy as np
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

st.title('Stock Price Analysis Dashboard')

# Create a sidebar with options
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=["Home", "Page 1", "Page 2", "Page 3"],  # required
        icons=["house", "file-earmark-text", "file-earmark-text", "file-earmark-text"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

# Create pages based on the selected option
if selected == "Home":
    st.write("# Welcome to the Home Page")
    st.write("This is the home page of the app.")

    tickerSymbol = st.text_input('Ticker Symbol', 'AAPL')
    tickerData = yf.Ticker(tickerSymbol)
    startdate = st.date_input('Start Date')
    enddate = st.date_input('End Date')

    tickerDf = tickerData.history(period='1d', start=startdate, end=enddate)

    st.line_chart(tickerDf.Close)
    st.line_chart(tickerDf.Volume)

    price_stats = tickerDf.describe()
    st.write(price_stats)


    # Set the title of the app
    st.title("Analog Gauge Meter")

    # Create a slider to simulate meter value
    meter_value = st.slider("Set Meter Value", 0, 100, 50)

    # Create the gauge figure
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=meter_value,
        gauge={'axis': {'range': [0, 100]},
            'bar': {'color': "black"},
            'steps': [{'range': [0, 25], 'color': "lightgreen"},
                        {'range': [25, 75], 'color': "gold"},
                        #  {'range': [50, 75], 'color': "pink"},
                        {'range': [75, 100], 'color': "pink"}]},
        title={'text': "Meter Value"}
    ))

    fig.update_layout(width=500, height=400, margin=dict(l=50, r=20, t=50, b=50))

    # Display the radial gauge in the Streamlit app
    st.plotly_chart(fig)

elif selected == "Page 1":
    st.write("# Welcome to Page 1")
    st.write("This is Page 1 of the app.")
elif selected == "Page 2":
    st.write("# Welcome to Page 2")
    st.write("This is Page 2 of the app.")
elif selected == "Page 3":
    st.write("# Welcome to Page 3")
    st.write("This is Page 3 of the app.")