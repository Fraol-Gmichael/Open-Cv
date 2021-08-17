import numpy as np
import cv2

# translate means to shft the image to the left, right, top and bottom
def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    
    return shifted


def rotate(image, angle, center=None, scale=1.0):
    height, width = image.shape[:2]
    if not center:
        center = (width//2, height//2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (width, height))

    return rotated

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    h, w = image.shape[:2]
    if not(width or height):
        return image
    elif width:
        ratio = (width / w)
        dim = (width, int(h*ratio))
    else:
        ratio = (height/ h)
        dim = (int(w*ratio), height)

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized




