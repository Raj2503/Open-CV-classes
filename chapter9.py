# FACE DETECTION

import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/me1.jpg")
img = cv2.resize(img,(800,512))

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(w+x,y+h),(255,0,0),2)

cv2.imshow("FACEDETECTION",img)
cv2.waitKey(0)