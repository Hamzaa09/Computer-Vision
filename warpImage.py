import cv2
import numpy as np
import requests

circles = np.zeros((4,2), np.int64)
counter = 0

def mousePoints(event, x, y, flags, params):
    global counter
    
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)
        
width, height = 500, 500
url = "https://picsum.photos/200"
response = requests.get(url)
image_array = np.frombuffer(response.content, dtype=np.uint8)
img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
img = cv2.resize(img, (width, height))

while True:
    if counter == 4:
        pt1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        output = cv2.warpPerspective(img, matrix, (width, height))

        cv2.imshow("Output", output)

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoints)
    cv2.waitKey(1)