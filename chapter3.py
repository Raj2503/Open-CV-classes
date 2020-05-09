# RESIZING AND CROPPING
import cv2
import numpy as np

img = cv2.imread("Resources/raj.jpg")
print(img.shape)

imgResize = cv2.resize(img,(300,200))
print(imgResize.shape)

imgCropped = img[0:200,200:500]

cv2.imshow("Image",img)
cv2.imshow("Reszied Image",imgResize)
cv2.imshow("Cropped Imaged",imgCropped)
cv2.waitKey(0)