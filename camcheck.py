import streamlit as st

import cv2

def check_webcam():
    webcam_dict = dict()
    avail = 'Available'
    for i in range(0, 10):
        cap = cv2.VideoCapture(i)
        is_camera = cap.isOpened()
        if is_camera:
            webcam_dict[f"Camera [{i}]"] = avail
            cap.release()
        else:
            webcam_dict[f"Camera [{i}]"] = None
    return webcam_dict

def app():
    st.title('WebCam index validation check')
    webcam_dict = check_webcam()
    st.write(webcam_dict)