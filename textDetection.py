import cv2
import pytesseract

width, height = 700, 500
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
path = "C:\\Users\\hamza\\OneDrive\\Computer Vision\\images\\text_image.png"
config = r'--oem 3 --psm 6'

img = cv2.imread(path)
img = cv2.resize(img, (width, height))

# Preprocessing for better detection
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(gray, (3,3), 0)
# thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Character Reading
# boxes = pytesseract.image_to_boxes(img, config=config)
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
#     cv2.rectangle(img, (x, height-y), (w, height-h), (0, 0, 255), 2)
#     cv2.putText(img, f'{b[0]}', (x, (height-y)+20), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

# Words Reading
boxes = pytesseract.image_to_data(img, config=config)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if (len(b) == 12) and float(b[10])>60:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(img, f'{b[11]}', (x, (y+h)+20), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()