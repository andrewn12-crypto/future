
import streamlit as st
import subprocess
repo_url = "https://github.com/ranaroussi/yfinance.git"
local_dir = "ranaroussi/yfinance"
subprocess.run(["git", "clone", repo_url, local_dir])
st.title("Stock Price App")
st.write("hello")
st.write("testing")
