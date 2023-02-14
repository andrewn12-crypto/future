import streamlit as st
import yfinance as yf

# Install yfinance from Github
!pip install git+https://github.com/ranaroussi/yfinance.git

# Define the stock ticker symbol
ticker_symbol = "AAPL"

# Download the stock data
data = yf.download(ticker_symbol, start="2020-01-01", end="2022-02-14")

# Display the data
st.line_chart(data["Adj Close"])
