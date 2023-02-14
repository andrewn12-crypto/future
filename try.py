
import streamlit as st
import subprocess
repo_url = "https://github.com/ranaroussi/yfinance.git"
local_dir = "ranaroussi/yfinance"
subprocess.run(["git", "clone", repo_url, local_dir])
import sys
sys.path.insert(0, local_dir + "/yfinance") # replace `local_dir` with the actual path to your cloned yfinance directory

st.title("Stock Price App")
st.write("hello")
st.write("testing")
