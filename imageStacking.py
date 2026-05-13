import numpy as np
import cv2
from utilities.StackImages import stackImages

frameWidth  = 800
frameHeight = 800
kernel = np.ones((5, 5), np.uint8)

path = "C:\\Users\\hamza\\OneDrive\\Pictures\\Screenshots\\new.png"

# Resize once at load — all derived images inherit the size
img = cv2.resize(cv2.imread(path), (frameWidth, frameHeight))

# Derived images — no need to resize again
imgGray     = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGaussian = cv2.GaussianBlur(img, (11, 11), 0)
imgCanny    = cv2.Canny(img, 50, 150)          # 50,50 is too narrow — use different thresholds
imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
imgErosion  = cv2.erode(imgCanny, kernel, iterations=1)

# Stack in a 2x3 grid
imgStack = stackImages(0.5, [[img, img, img]])

cv2.imshow("All Transformations", imgStack)
cv2.waitKey(0)