# READ IMAGES, VIDEOS AND WEBCAMS
import cv2
print("Package Imported")

# FOR IMAGE
img = cv2.imread("Resources/raj.jpg")
img2 = cv2.resize(img,(700,512))
cv2.imshow("Output",img)
cv2.imshow("Smaller Output",img2)
cv2.waitKey((0))

# FOR WEBCAM VIDEO
cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
