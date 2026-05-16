import imutils, numpy as np, cv2
from utilities import StackImages

url = "C:\\Users\\hamza\\OneDrive\\Computer Vision\\images\\faces.jpg"
img = cv2.imread(url)
img = cv2.resize(img, (400, 400))

# ----------- Image Rotation -----------

# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# center = (img.shape[1] // 2, img.shape[0] // 2)
# rotation_matrix = cv2.getRotationMatrix2D(center, 310, 1)
# img = cv2.warpAffine(img, rotation_matrix, (img.shape[1], img.shape[0]))

# img = imutils.rotate(img, 90)


# ----------- Image Translation -----------
# tx, ty = 50, 50
# translation_matrix = np.array([[1, 0, tx], [0, 1, ty]], dtype=np.float32)
# img = cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))


# ----------- Image Normalization -----------
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# r, g, b = cv2.split(img_rgb)

# b_normalized = cv2.normalize(b.astype(float), None, 0, 1, cv2.NORM_MINMAX)
# g_normalized = cv2.normalize(g.astype(float), None, 0, 1, cv2.NORM_MINMAX)
# r_normalized = cv2.normalize(r.astype(float), None, 0, 1, cv2.NORM_MINMAX)

# img_p = cv2.merge((b_normalized, g_normalized, r_normalized))
# stack_img = StackImages.stackImages(1, [[img_p, img]])


# ----------- Image Equalization -----------
# equalized_img = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
# stack_img = StackImages.stackImages(1, [[equalized_img, img]])

# ----------- Image Bordering -----------
# img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 0, 255])
# print(img.shape) 

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()