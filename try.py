import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

# Download data asli 2010-2023 EURUSD
data1 = yf.download('EURUSD=X', interval="1m",period="7D")
