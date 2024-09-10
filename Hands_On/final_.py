import streamlit as st
import yfinance as yf
import pandas as pd

# Initial boilerplate code to set up a Streamlit app
st.title("Interactive Stock Price Dashboard")

# Function to fetch historical stock price data
@st.cache
def fetch_stock_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data

# Sidebar widget to select stock ticker
ticker = st.sidebar.text_input("Enter Stock Ticker", value="AAPL")

# Sidebar widget to select date range
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("today"))

# Fetch data and display
if ticker:
    data = fetch_stock_data(ticker, start_date, end_date)
    if not data.empty:
        st.subheader(f"Stock Price Data for {ticker}")
        st.line_chart(data['Close'])
    else:
        st.write("No data found for the selected ticker and date range.")
else:
    st.write("Please enter a stock ticker.")
    
