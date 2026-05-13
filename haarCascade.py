import cv2
import numpy as np
from utilities.StackImages import stackImages

windowName = "Faces Detector"
frameWidth = 700
frameHeight = 600
file = "haarcascade_frontalface_default.xml"
path = f"C:\\Users\\hamza\\OneDrive\\Computer Vision\\haarcascades\\{file}"
url = "C:\\Users\\hamza\\OneDrive\\Computer Vision\\images\\faces.jpg"
objectName = "Face"
color = (255, 0, 255)
def empty(a):
    pass

cv2.namedWindow(windowName)
cv2.resizeWindow(windowName, frameWidth, 400)
cv2.createTrackbar("Scale", windowName, 100, 1000, empty)
cv2.createTrackbar("Neig", windowName, 2, 20, empty)
cv2.createTrackbar("Area", windowName, 0, 10000, empty)
cv2.createTrackbar("Brightness", windowName, 180, 255, empty)

cascade = cv2.CascadeClassifier(path)

cap = cv2.VideoCapture(0)
while True:
    brightness = cv2.getTrackbarPos("Brightness", windowName)
    # img = cv2.imread(url)
    cap.set(10, brightness)
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img = cv2.resize(img, (frameWidth, frameHeight))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    scale = 1+(cv2.getTrackbarPos("Scale", windowName)/1000)
    neig = cv2.getTrackbarPos("Neig", windowName)
    
    objects = cascade.detectMultiScale(gray, scale, neig)
    
    if len(objects) == 0:
        cv2.putText(img, "No DetectionS", (20,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    
    for (x, y, w, h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Area", windowName)
        if area>minArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 5)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
    
    # stack = stackImages(0.5, [[img, gray]])
    cv2.imshow(windowName, img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break