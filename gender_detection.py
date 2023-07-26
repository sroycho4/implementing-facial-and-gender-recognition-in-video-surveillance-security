import cv2
import cvlib as cv
import numpy as np

webcam = cv2.VideoCapture(0)
    
padding = 20
while webcam.isOpened():
    status, frame = webcam.read()
    face, confidence = cv.detect_face(frame)
    #write your code here



    
    cv2.imshow("Real-time gender detection", frame)
    # press "s" to stop
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
webcam.release()
cv2.destroyAllWindows()        