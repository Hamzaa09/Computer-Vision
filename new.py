import numpy as np
import cv2

frameWidth = 680
frameHeight = 420
kernel = np.ones((5,5), np.uint8)

path = "C:\\Users\\hamza\\OneDrive\\Pictures\\Screenshots\\new.png"
img = cv2.imread(path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (11, 11), 0)
img = cv2.Canny(img, 50, 50)
imgDilation = cv2.dilate(img, kernel, iterations=2)
imgErrosion = cv2.erode(img, kernel, iterations=1)

print(kernel)
cv2.imshow("Image Dilation",imgDilation)
cv2.imshow("Image Errosion",imgErrosion)
cv2.waitKey(0)
