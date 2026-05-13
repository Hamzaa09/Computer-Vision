import cv2

path = "C:\\Users\\hamza\\OneDrive\\Pictures\\Screenshots\\new.png"
width, height = 500, 500

img = cv2.imread(path)
resizedImg = cv2.resize(img, (width, height))
croppedImg = img[:450, :]

print(img.shape)
print(resizedImg.shape)
print(croppedImg.shape)


cv2.imshow("Image", img)
cv2.imshow("Resized Image", resizedImg)
cv2.imshow("Cropped Image", croppedImg)
cv2.waitKey(0)