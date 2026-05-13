import cv2
import numpy as np
from utilities.StackImages import stackImages

url = "C:\\Users\\hamza\\OneDrive\\Computer Vision\\images\\rhombus.jpg"
cap = cv2.VideoCapture(0)

def empty(a):
    pass

cv2.namedWindow("Threshold Detector")
cv2.resizeWindow("Threshold Detector", 900, 300)
cv2.createTrackbar("Threshold 1", "Threshold Detector", 170, 255, empty)
cv2.createTrackbar("Threshold 2", "Threshold Detector", 180, 255, empty)
cv2.createTrackbar("Area", "Threshold Detector", 10, 5000, empty)

def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        c_area = cv2.getTrackbarPos("Area", "Threshold Detector")
        if area > c_area:
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 8)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)

            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 5)
            cv2.putText(imgContour, "Point: " + str(len(approx)), (x + 20, y + h + 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 4)
            cv2.putText(imgContour, "Area: " + str(area), (x + 20, y + h + 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 4)
        
while True:
    # img = cv2.imread(url)
    _, img = cap.read()
    img = cv2.flip(img, 1)
    imgContour = img.copy()
    ths1 = cv2.getTrackbarPos("Threshold 1", "Threshold Detector")
    ths2 = cv2.getTrackbarPos("Threshold 2", "Threshold Detector")
    imgCanny = cv2.Canny(img, ths1, ths2)
    
    getContours(imgCanny, imgContour)
    
    stackImg = stackImages(0.5, [[img, imgCanny], [imgContour, imgContour]])
    cv2.imshow("Web Cam", stackImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break