
import pandas as pd
import yfinance as yf
import numpy as np
from pmdarima import auto_arima

# Download data asli 2010-2023 EURUSD
data1 = yf.download('EURUSD=X', interval="1m",period="7D")
data2 = yf.download('EURUSD=X', interval="2m",period="60D")
data3 = yf.download('EURUSD=X', interval="5m",period="60D")
data4 = yf.download('EURUSD=X', interval="15m",period="60D")
data5 = yf.download('EURUSD=X', interval="30m",period="60D")
data6 = yf.download('EURUSD=X', interval="1H",period="2Y")
data7 = yf.download('EURUSD=X', interval="1D",period="max")

#Preprocessing data
data1.reset_index(inplace=True)
data2.reset_index(inplace=True)
data3.reset_index(inplace=True)
data4.reset_index(inplace=True)
data5.reset_index(inplace=True)
data6.reset_index(inplace=True)
data7.reset_index(inplace=True)
data1=data1['Close']
data2=data2['Close']
data3=data3['Close']
data4=data4['Close']
data5=data5['Close']
data6=data6['Close']
data7=data7['Close']

#Prediction
data_to_predict1=data1[:(np.shape(data1)[0]-1)]
data_to_predict2=data2[:(np.shape(data2)[0]-1)]
data_to_predict3=data3[:(np.shape(data3)[0]-1)]
data_to_predict4=data4[:(np.shape(data4)[0]-1)]
data_to_predict5=data5[:(np.shape(data5)[0]-1)]
data_to_predict6=data6[:(np.shape(data6)[0]-1)]
data_to_predict7=data7[:(np.shape(data7)[0]-1)]


model1 = auto_arima(data_to_predict1, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
model2 = auto_arima(data_to_predict2, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
model3 = auto_arima(data_to_predict3, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
model4 = auto_arima(data_to_predict4, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
model5 = auto_arima(data_to_predict5, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
model6 = auto_arima(data_to_predict6, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)
model7 = auto_arima(data_to_predict7, seasonal=False, error_action='ignore', suppress_warnings=True, stepwise=True, trace=False)

forecast1 = model1.predict(n_periods=1)
forecast2 = model2.predict(n_periods=1)
forecast3 = model3.predict(n_periods=1)
forecast4 = model4.predict(n_periods=1)
forecast5 = model5.predict(n_periods=1)
forecast6 = model6.predict(n_periods=1)
forecast7 = model7.predict(n_periods=1)

print("1Minute",forecast1)
print("2Minute",forecast2)
print("5Minute",forecast3)
print("15Minute",forecast4)
print("30Minute",forecast5)
print("1H",forecast6)
print("1Day",forecast7)
