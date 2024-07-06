import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from kiss import main
# from predict import pred

def get_stock_data(ticker, start_date, end_date):
    try:
        stock = yf.Ticker(ticker)
        
        data = stock.history(start=start_date, end=end_date)
    
    except Exception as e:
        stock, data = None
        print(f"An unexpected error occurred: {e}")

    finally:
        return stock, data
    
def get_moving_averages(data):
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA100'] = data['Close'].rolling(window=100).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Price', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA50'], name='50-day Moving Avg', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA100'], name='100-day Moving Avg', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA200'], name='200-day Moving Avg', line=dict(color='yellow')))

    fig.update_layout(
        title='',
        xaxis_title='Date',
        yaxis_title='Price',
        legend_title='Indicators',
        hovermode='x unified'
    )
    
    return fig



def ratio_metrics(ticker):
    info = ticker.info
    pe_ratio = info['trailingPE']
    return pe_ratio



def main():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "Compare", "Predict", "KISS"],
            icons=["house", "bar-chart-steps", "graph-up-arrow", "book-half"],
            default_index=0,
        )

    if selected == "Home":
        st.title('Stock Price Analysis Dashboard')
        st.divider()

        tickerSymbol = st.text_input('Ticker Symbol', 'AAPL')
        startdate = st.date_input('Start Date')
        enddate = st.date_input('End Date')
        if startdate==enddate or startdate>enddate:
            st.write("Please change start date to get appropriate results.")
        else:
            ticker, tickerDf = get_stock_data(tickerSymbol, startdate, enddate)
            st.divider()

            st.subheader("Stock Price")
            if tickerDf['Close'].iloc[-1] > tickerDf['Close'].iloc[0]:
                linecolor = 'green'
            else:
                linecolor = 'red'
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=tickerDf.index, y=tickerDf['Close'], name=ticker.info['longName'], line=dict(color=linecolor, width=2)))
            fig.update_layout(title="", xaxis_rangeslider_visible=True)
            st.plotly_chart(fig)
            st.bar_chart(tickerDf.Volume)
            st.divider()

            st.subheader("Moving Averages")
            minDate, maxDate = pd.to_datetime(startdate), pd.to_datetime(enddate)
            if (maxDate - minDate).days > 200:
                fig = get_moving_averages(tickerDf)
                st.plotly_chart(fig)
            else:
                st.write("Not enough data to calculate moving averages.")
            st.divider()

            pe = ratio_metrics(ticker)
            st.subheader("Ratio Metrics")
            # Create the gauge figure
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=pe,
                gauge={'axis': {'range': [0, 40]},
                    'bar': {'color': "blue"},
                    'steps': [{'range': [0, 13], 'color': "green"},
                                {'range': [13, 27], 'color': "gold"},
                                {'range': [27, 40], 'color': "red"}]},
                title={'text': "Price-to-Earning Ratio"}
            ))
            fig.update_layout(width=500, height=400, margin=dict(l=20, r=20, t=50, b=50))
            st.plotly_chart(fig)
            st.divider()

            st.subheader("Financial Performance")
            df = ticker.incomestmt
            trace1 = go.Bar(
                x=df.columns,
                y=df.loc['Total Revenue'],
                name='Total Revenue',
                marker=dict(color='blue')
            )
            trace2 = go.Bar(
                x=df.columns,
                y=df.loc['Total Expenses'],
                name='Total Expenses',
                marker=dict(color='red')
            )
            trace3 = go.Bar(
                x=df.columns,
                y=df.loc['Net Income'],
                name='Net Income',
                marker=dict(color='green'),
            )
            data = [trace1, trace2, trace3]
            layout = go.Layout(
                title='',
                yaxis=dict(title='Amount'),
                barmode='group'
            )
            fig = go.Figure(data=data, layout=layout)
            st.plotly_chart(fig)
            st.divider()

            st.subheader("Income statement")
            st.write(ticker.incomestmt)
            st.divider()

            st.subheader("Financials")
            st.write(ticker.financials)
            st.divider()

            st.subheader("Balance Sheet")
            st.write(ticker.balance_sheet)
            st.divider()

            st.subheader("Cash Flow")
            st.write(ticker.cashflow)
            st.divider()
            
            st.subheader("Stock Info")
            st.write(ticker.info)
            st.divider()
        
            st.subheader("About Dataset")
            st.write(tickerDf.describe())




    elif selected == "Compare":
        st.title("Comparision")
        st.divider()
        startdate = st.date_input('Start Date')
        enddate = st.date_input('End Date')
        st.write("")

        if startdate==enddate or startdate>enddate:
            st.write("Please change start date to get appropriate results.")
        else:
            col1, col2= st.columns(2)
            with col1:
                st.write("Enter 1st stock")
                ticker1 = st.text_input('Ticker Symbol', 'AAPL')
                stock1, tickerDf1 = get_stock_data(ticker1, startdate, enddate)
                st.subheader('Stock Price')
                if tickerDf1['Close'].iloc[-1] > tickerDf1['Close'].iloc[0]:
                    linecolor = 'green'
                else:
                    linecolor = 'red'
                fig1 = go.Figure()
                fig1.add_trace(go.Scatter(x=tickerDf1.index, y=tickerDf1['Close'], name=stock1.info['longName'], line=dict(color=linecolor)))
                fig1.update_layout(title=stock1.info['longName'], xaxis_rangeslider_visible=True)
                st.plotly_chart(fig1)

                st.subheader("Financial Performance")
                df = stock1.incomestmt
                trace1 = go.Bar(
                    x=df.columns,
                    y=df.loc['Total Revenue'],
                    name='Total Revenue',
                    marker=dict(color='blue')
                )
                trace2 = go.Bar(
                    x=df.columns,
                    y=df.loc['Total Expenses'],
                    name='Total Expenses',
                    marker=dict(color='red')
                )
                trace3 = go.Bar(
                    x=df.columns,
                    y=df.loc['Net Income'],
                    name='Net Income',
                    marker=dict(color='green'),
                )
                data = [trace1, trace2, trace3]
                layout = go.Layout(
                    title=stock1.info['longName'],
                    yaxis=dict(title='Amount'),
                    barmode='group',
                    legend=dict(
                        orientation='h',
                        y=-0.1,
                    )
                )
                fig = go.Figure(data=data, layout=layout)
                st.plotly_chart(fig)

            with col2:
                st.write("Enter 2nd stock")
                ticker2 = st.text_input('Ticker Symbol', 'GOOG')
                stock2, tickerDf2 = get_stock_data(ticker2, startdate, enddate)
                st.subheader("")
                if tickerDf2['Close'].iloc[-1] > tickerDf2['Close'].iloc[0]:
                    linecolor = 'green'
                else:
                    linecolor = 'red'
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(x=tickerDf2.index, y=tickerDf2['Close'], name=stock2.info['longName'], line=dict(color=linecolor)))
                fig2.update_layout(title=stock2.info['longName'], xaxis_title='Date', yaxis_title='Price', xaxis_rangeslider_visible=True)
                st.plotly_chart(fig2)

                st.subheader('')
                df = stock2.incomestmt
                trace1 = go.Bar(
                    x=df.columns,
                    y=df.loc['Total Revenue'],
                    name='Total Revenue',
                    marker=dict(color='blue')
                )
                trace2 = go.Bar(
                    x=df.columns,
                    y=df.loc['Total Expenses'],
                    name='Total Expenses',
                    marker=dict(color='red')
                )
                trace3 = go.Bar(
                    x=df.columns,
                    y=df.loc['Net Income'],
                    name='Net Income',
                    marker=dict(color='green'),
                )
                data = [trace1, trace2, trace3]
                layout = go.Layout(
                    title=stock2.info['longName'],
                    yaxis=dict(title='Amount'),
                    barmode='group',
                    legend=dict(
                        orientation='h',
                        y=-0.1,
                    )
                )
                fig = go.Figure(data=data, layout=layout)
                st.plotly_chart(fig)

            st.divider()

            stock1Returns = tickerDf1['Close'].pct_change().fillna(0).cumsum() * 100
            stock2Returns = tickerDf2['Close'].pct_change().fillna(0).cumsum() * 100
            st.subheader("Stock returns in percentage")
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=tickerDf1.index, y=stock1Returns, mode='lines', name=stock1.info['longName']))
            fig.add_trace(go.Scatter(x=tickerDf2.index, y=stock2Returns, mode='lines', name=stock2.info['longName']))
            fig.update_layout(xaxis_title='Date', yaxis_title='Returns in (%)')
            st.plotly_chart(fig)
            st.divider()
        

    elif selected == "Predict":
        st.title("Predicting Stock Prices")
        st.divider()

        tickerSymbol = st.text_input('Ticker Symbol', 'AAPL')
        startdate = st.date_input('Start Date')
        enddate = st.date_input('End Date')
        stock, tickerDf = get_stock_data(tickerSymbol, startdate, enddate)

        fig, ax = plt.subplots(figsize=(16, 6))
        ax.set_title('Price History')
        ax.plot(tickerDf['Close'])
        ax.set_xlabel('Date', fontsize=18)
        ax.set_ylabel('Price', fontsize=18)
        st.pyplot(fig)

        st.write("")
        st.subheader("Stock price prediction is only available on local machine...")
        # pred(tickerDf)


    elif selected == "KISS":
        st.title("Keep It Simple Strategy")
        st.divider()
        st.write(main.check())
        




if __name__ == '__main__':
    main()