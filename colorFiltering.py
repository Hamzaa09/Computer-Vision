import cv2
import numpy as np

frameWidth = 500
frameHeight = 400
cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 900, 300)
cv2.createTrackbar("Hue MIN", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue MAX", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat MIN", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat MAX", "HSV", 255, 255, empty)
cv2.createTrackbar("Val MIN", "HSV", 0, 255, empty)
cv2.createTrackbar("Val MAX", "HSV", 255, 255, empty)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    img = cv2.flip(img, 1)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hue_min = cv2.getTrackbarPos("Hue MIN", "HSV")
    hue_max = cv2.getTrackbarPos("Hue MAX", "HSV")
    sat_min = cv2.getTrackbarPos("Sat MIN", "HSV")
    sat_max = cv2.getTrackbarPos("Sat MAX", "HSV")
    val_min = cv2.getTrackbarPos("Val MIN", "HSV")
    val_max = cv2.getTrackbarPos("Val MAX", "HSV")
    
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    
    hStack = np.hstack([img, imgHSV, result])
    cv2.imshow("Web Cam", hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
