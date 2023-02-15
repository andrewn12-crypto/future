import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd

# Download data asli 2010-2023 EURUSD
data1 = yf.download('EURUSD=X', interval="1H",period="2Y")
data2 = yf.download('EURUSD=X', interval="90m",period="60D")
data3 = yf.download('EURUSD=X', interval="1D",period="max")

data1.reset_index(inplace=True)
data2.reset_index(inplace=True)
data3.reset_index(inplace=True)


data1=data1['Close']
data2=data2['Close']
data3=data3['Close']


#Prediction
data_to_predict1=data1[:(np.shape(data1)[0]-1)]
data_to_predict2=data2[:(np.shape(data2)[0]-1)]
data_to_predict3=data3[:(np.shape(data3)[0]-1)]
