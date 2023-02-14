import streamlit as st
import subprocess

# Specify the repository URL and the absolute path to the local directory where you want to clone it
repo_url = "https://github.com/ranaroussi/yfinance.git"
local_dir = "/path/to/local/directory"

# Clone the repository using Git
subprocess.run(["git", "clone", repo_url, local_dir])
import subprocess
import sys

# Clone yfinance repository
repo_url = "https://github.com/ranaroussi/yfinance.git"
local_dir = "/path/to/local/directory"
subprocess.run(["git", "clone", repo_url, local_dir])
subprocess.run(["pip", "install", "-r", local_dir + "/yfinance.git])
# Add cloned directory to sys.path
sys.path.insert(0, local_dir)

# Import yfinance module
import yfinance


# Use the yfinance module in your Streamlit app
st.title("Stock Price App")
st.write("hello")
st.write("testing")
