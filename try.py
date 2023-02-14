import streamlit as st
import subprocess

# Specify the repository URL and the absolute path to the local directory where you want to clone it
repo_url = "https://github.com/ranaroussi/yfinance.git"
local_dir = "/path/to/local/directory"

# Clone the repository using Git
subprocess.run(["git", "clone", repo_url, local_dir])

# Add the local directory to the Python path and import the yfinance module
import sys
sys.path.insert(0, local_dir + "/yfinance")
import yfinance

# Use the yfinance module in your Streamlit app
st.title("Stock Price App")
st.write("hello")
st.write("testing")
