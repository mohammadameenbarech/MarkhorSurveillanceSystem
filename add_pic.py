from genericpath import exists
from platform import release
import cv2
from time import sleep
import streamlit as st
from pil import Image,ImageEnhance
import time
import os

#from webcam import webcam
def app():
    st.title("Add Picture")
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    counter = 0
    name = st.text_input("Enter Name")
    
    face_dir = 'D:\DLD PROJECT\Facerecog\Faces'
    try:
        
        while True:
            _,frame = camera.read()
            f = frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)        
    except:
        print("failed to execute")   

    if st.button("Take Picture"):
        path = os.path.join(face_dir,name)
        if not os.path.exists(path):
            os.mkdir(path)
            f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
            cv2.imwrite(f'./Faces\{name}\\img{counter}.jpg',f)
            
        else:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            cv2.imwrite(f'./Faces\{name}\\img{counter}.jpg',f)
        counter+=1
        
    