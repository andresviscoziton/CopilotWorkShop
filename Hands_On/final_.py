# import streamlit as st
# import yfinance as yf
# import pandas as pd


# # Set up the Streamlit app
# st.title("Interactive Stock Price Dashboard")

# # Sidebar for user input
# st.sidebar.header("User Input")
# selected_stock = st.sidebar.text_input("Enter stock ticker", "AAPL")
# start_date = st.sidebar.date_input("Start date", pd.to_datetime("2020-01-01"))
# end_date = st.sidebar.date_input("End date", pd.to_datetime("today"))

# # Fetch historical stock price data
# @st.cache
# def fetch_data(ticker, start, end):
#     stock_data = yf.download(ticker, start=start, end=end)
#     return stock_data

# # Fetch data
# data = fetch_data(selected_stock, start_date, end_date)

# # Display stock data
# st.subheader(f"Stock Data for {selected_stock}")
# st.write(data)

# # Create interactive line chart
# st.subheader("Stock Price Over Time")
# st.line_chart(data['Close'])

# # Display additional information
# st.sidebar.subheader("Additional Information")
# st.sidebar.write(f"Data range: {start_date} to {end_date}")
# st.sidebar.write(f"Selected stock: {selected_stock}")

# # Run the app
# if __name__ == "__main__":
#     st.run()