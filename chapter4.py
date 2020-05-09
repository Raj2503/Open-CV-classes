# SHAPES AND TEXT
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

# print(img)
# img[200:300,100:300] = 255,0,0  {color the image}
# shape[0]-> width shape[1] -> height
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# img,origin,end point,color,thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)
# img,origin,end point,color,thickness
cv2.circle(img,(400,50),30,(255,255,0),5)
# img,origin,radius,color,thickness
cv2.putText(img,"Raj Aryan",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),3)
# img,text,origin,font,scale,color,thickness


cv2.imshow("Zeros",img)

cv2.waitKey(0)