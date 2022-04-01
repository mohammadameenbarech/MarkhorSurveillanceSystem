import streamlit as st
import os

st.title("Re-Train system")
if st.button('Click to Train'):
    os.system('python train_v2.py')