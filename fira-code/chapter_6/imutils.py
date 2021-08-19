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
        ratio = (height / h)
        dim = (int(w*ratio), height)

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


def crop(image, start=[0, 0], end=None):
    if not end:
        end = [image.shape[1], image.shape[0]]
    cropped = image[start[0]:end[0], start[1]:end[1]]

    return cropped


def arithmetic(image, number, add=False, subtract=False):

    number = np.ones(image.shape, dtype="uint8") * number

    if add and subtract:
        return image
    elif add:
        return cv2.add(image, number)
    elif subtract:
        return cv2.subtract(image, number)
    else:
        return image


def mask(image, center=None, width=50, rectangle=True):
    mask = np.zeros(image.shape, dtype="uint8")

    if not center:
        center = [image.shape[1]//2, image.shape[0]//2]

    center = np.array(center)

    start = center - width
    end = center + width

    if rectangle:
        masked = cv2.rectangle(mask, start, end, (255, 255, 255), -1)
    else:
        masked = cv2.circle(mask, center, width, (255, 255, 255), -1)

    masked = cv2.bitwise_and(masked, image)

    return masked

    #------------OR-----------#


def mask2(image, center=None, width=50, rectangle=True):

    mask = np.zeros(image.shape[:2], dtype="uint8")

    if not center:
        center = [image.shape[1]//2, image.shape[0]//2]

    center = np.array(center)

    start = center - width
    end = center + width

    if rectangle:
        masked = cv2.rectangle(mask, start, end, 255, -1)
    else:
        masked = cv2.circle(mask, center, width, 255, -1)

    masked = cv2.bitwise_and(image, image, mask=masked)

    return masked
