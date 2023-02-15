import streamlit as st
import httpie
import yfinance

data1 = yf.download('EURUSD=X', interval="1m",period="7D")
