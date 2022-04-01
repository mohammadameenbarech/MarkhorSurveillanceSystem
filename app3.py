import streamlit as st
import cv2
import app2 as a
import time
import mediapipe as mp
import camcheck as cc
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
prevTime = 0
with mp_hands.Hands(
    min_detection_confidence=0.5,       #Detection Sensitivity
    min_tracking_confidence=0.5) as hands:

    def app():
        st.title("Webcam Live Feed")
        #run = st.checkbox('Run')
        required_shape = (160,160)
        face_encoder = a.InceptionResNetV2()
        path_m = "facenet_keras_weights.h5"
        face_encoder.load_weights(path_m)
        encodings_path = 'encodings/encodings.pkl'
        face_detector = a.mtcnn.MTCNN()
        encoding_dict = a.load_pickle(encodings_path)
        FRAME_WINDOW = st.image([])
        cam_avail = cc.check_webcam()
        cam = []
        counter = 0
        for i,j in cam_avail.items():
            if cam_avail[i] is None:
                continue 
            else:
                cam.append(counter)
            counter+=1
        while True:    
            option = st.selectbox(
                'Select Cameras Connected?',
                (cam))
            break
        cap = cv2.VideoCapture(option)
        prevTime = 0

       #while run:
            #frame = camera.read()
            #frame= a.detect(frame , face_detector , face_encoder , encoding_dict)
            #FRAME_WINDOW.image(frame)
            #cv2.imshow('camera', frame)
       # else:
           # st.write('Stopped')
        while cap.isOpened():
            ret,frame = cap.read()


            if not ret:
                print("CAM NOT OPEND") 
                break
            currTime = time.time()
            fps = 1 / (currTime - prevTime)
            prevTime = currTime
            
            frame = a.detect(frame , face_detector , face_encoder , encoding_dict)
            FRAME_WINDOW.image(frame[:, :, ::-1])

            # currTime = time.time()
            # prevTime = currTime
            # fps = 1 / (currTime - prevTime)
            
            #cv2.putText(ret, (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 196, 255), 2)
            #cv2.imshow('camera', frame)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
        