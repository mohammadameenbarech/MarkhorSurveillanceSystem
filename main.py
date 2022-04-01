#app.py
import camcheck
import app3
import add_pic
import Re_train as rt
import streamlit as st
import home

PAGES = {
    "Home": home,
    "Check Available Cameras": camcheck,
    "Start Detection": app3,
    "Add Face": add_pic,
    "Re-Train System": rt
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()