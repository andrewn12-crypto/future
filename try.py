import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import pmdarima
from pmdarima import auto_arima

# Download data asli 2010-2023 EURUSD

data2 = yf.download('EURUSD=X', interval="90m",period="60D")
data2.reset_index(inplace=True)
data2=data2['Close']
data_to_predict2=data2[:(np.shape(data2)[0]-1)]
model2 = auto_arima(data_to_predict2, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
forecast2 = model2.predict(n_periods=1)
st.write("1,5H",forecast2)

