import cv2
import numpy as np

path = "C:\\Users\\hamza\\OneDrive\\Pictures\\Screenshots\\new.png"
width, height = 500, 500

img = np.zeros((width, height, 3), np.uint8)
# img = np.random.randint(0, 200, (width, height, 3), dtype="uint8")

## shapes
cv2.putText(img, "Drawing Shapes", (img.shape[0]//4, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0), 2)
cv2.line(img, (width//2, 100), (width//2, height), (255, 255, 255), 2)
cv2.circle(img, ((width//2)//2, height//2), 50, (0, 255, 255), 2)
cv2.rectangle(img, (width-(width//3), 100), (width-((width//2)//2), height-50), (255, 255, 0), cv2.FILLED)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()