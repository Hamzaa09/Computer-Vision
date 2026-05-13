import cv2

frameWidth = 680
frameHeight = 420

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow("WebCam", img)
    img = cv2.resize(img, (frameWidth, frameHeight))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break