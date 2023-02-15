import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import pmdarima
from pmdarima import auto_arima

# Download data asli 2010-2023 EURUSD

data21 = yf.download('EURUSD=X', interval="90m",period="60D")
data21.reset_index(inplace=True)
data2=data21['Close']
data_to_predict2=data2[:(np.shape(data2)[0]-1)]
model2 = auto_arima(data_to_predict2, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
forecast2 = model2.predict(n_periods=1)
st.write('1,5H',forecast2)



data3=data21['Low']
data_to_predict3=data3[:(np.shape(data3)[0]-1)]
model3 = auto_arima(data_to_predict3, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
forecast3 = model3.predict(n_periods=1)
st.write('1,5H',forecast3)
