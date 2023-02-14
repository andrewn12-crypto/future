
import streamlit as st
from git import Repo
Repo.clone_from("https://github.com/ranaroussi/yfinance.git")
st.title("Stock Price App")
st.write("hello")
st.write("testing")
