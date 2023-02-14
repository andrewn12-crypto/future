
import streamlit as st
import subprocess

url = "https://github.com/ranaroussi/yfinance.git"
target_dir = "/path/to/destination/directory"

subprocess.run(["git", "clone", url, target_dir], check=True)
st.title("Stock Price App")
st.write("hello")
st.write("testing")
