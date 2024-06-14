import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
# from predict import pred

def ratio_metrics(tickerData):
    info = tickerData.info
    pe_ratio = info['trailingPE']
    return pe_ratio


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Compare", "Predict"],
        icons=["house", "bar-chart-steps", "graph-up-arrow"],
        default_index=0,
    )

if selected == "Home":
    st.title('Stock Price Analysis Dashboard')
    st.write("")
    tickerSymbol = st.text_input('Ticker Symbol', 'AAPL')
    tickerData = yf.Ticker(tickerSymbol)
    startdate = st.date_input('Start Date')
    enddate = st.date_input('End Date')

    tickerDf = tickerData.history(period='1d', start=startdate, end=enddate)

    st.write("")
    st.write("")
    st.line_chart(tickerDf.Close)
    st.bar_chart(tickerDf.Volume)
    st.write("")
    st.write("")

    pe = ratio_metrics(tickerData)
    st.write("Income statement")
    st.write(tickerData.incomestmt)
    st.write("")
    st.write("Balance Sheet")
    st.write(tickerData.balance_sheet)
    st.write("")
    st.write("Cash Flow")
    st.write(tickerData.cashflow)
    st.write("")    
    st.write("Stock Info")
    st.write(tickerData.info)
    st.write("")
    st.write("Financials")
    st.write(tickerData.financials)
    st.write("")
    st.write("Dataframe")
    st.write(tickerDf.describe())


    st.title("Ratio Metrics")
    # Create the gauge figure
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=pe,
        gauge={'axis': {'range': [0, 40]},
            'bar': {'color': "black"},
            'steps': [{'range': [0, 15], 'color': "green"},
                        {'range': [16, 25], 'color': "gold"},
                        {'range': [26, 40], 'color': "red"}]},
        title={'text': "Price-to-Earning Ratio"}
    ))
    fig.update_layout(width=500, height=400, margin=dict(l=20, r=20, t=50, b=50))
    st.plotly_chart(fig)

elif selected == "Compare":
    st.title("Comparision")
    startdate = st.date_input('Start Date')
    enddate = st.date_input('End Date')
    st.write("")
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Enter 1st stock")
        tickerSymbol1 = st.text_input('Ticker Symbol', 'AAPL')
        tickerData1 = yf.Ticker(tickerSymbol1)
        tickerDf1 = tickerData1.history(period='1d', start=startdate, end=enddate)
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(x=tickerDf1.index, y=tickerDf1['Close'], mode='lines', name='Stock 1'))
        fig1.update_layout(title='Stock 1 Close Price', xaxis_title='Date', yaxis_title='Price')
        st.plotly_chart(fig1)

    with col2:
        st.write("Enter 2nd stock")
        tickerSymbol2 = st.text_input('Ticker Symbol', 'GOOG')
        tickerData2 = yf.Ticker(tickerSymbol2)
        tickerDf2 = tickerData2.history(period='1d', start=startdate, end=enddate)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=tickerDf2.index, y=tickerDf2['Close'], mode='lines', name='Stock 2'))
        fig2.update_layout(title='Stock 2 Close Price', xaxis_title='Date', yaxis_title='Price')
        st.plotly_chart(fig2)
    

elif selected == "Predict":
    st.write("Predicting Stock Prices")
    st.write("")

    tickerSymbol = st.text_input('Ticker Symbol', 'AAPL')
    tickerData = yf.Ticker(tickerSymbol)
    startdate = st.date_input('Start Date')
    enddate = st.date_input('End Date')

    tickerDf = tickerData.history(period='1d', start=startdate, end=enddate)

    fig, ax = plt.subplots(figsize=(16, 6))
    ax.set_title('Close Price History')
    ax.plot(tickerDf['Close'])
    ax.set_xlabel('Date', fontsize=18)
    ax.set_ylabel('Price', fontsize=18)
    st.pyplot(fig)

    st.write("")
    st.subheader("Stock price prediction is only available on local machine...")
    # pred(tickerDf)
