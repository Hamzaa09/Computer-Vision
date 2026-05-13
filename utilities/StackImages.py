import cv2
import numpy as np

def stackImages(scale, imgArray):
    """
    Stack multiple images in a grid layout with auto-scaling.
    
    :param scale: float - resize factor (e.g., 0.5 = half size)
    :param imgArray: list of lists - 2D array of images to stack
                     e.g., [[img1, img2], [img3, img4]] → 2x2 grid
    """
    rows = len(imgArray)
    cols = len(imgArray[0])

    rowsAvailable = isinstance(imgArray[0], list)
    width  = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    if rowsAvailable:
        for x in range(rows):
            for y in range(cols):
                # Resize every image to match the first image's size
                imgArray[x][y] = cv2.resize(imgArray[x][y], (width, height))

                # Convert grayscale → BGR so all images can be stacked together
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows

        for x in range(rows):
            hor[x] = np.hstack(imgArray[x])   # Stack each row horizontally

        ver = np.vstack(hor)                   # Stack all rows vertically

    else:
        # Single row of images
        for x in range(rows):
            imgArray[x] = cv2.resize(imgArray[x], (width, height))
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor

    # Apply the global scale
    ver = cv2.resize(ver, (int(ver.shape[1] * scale), int(ver.shape[0] * scale)))
    return ver