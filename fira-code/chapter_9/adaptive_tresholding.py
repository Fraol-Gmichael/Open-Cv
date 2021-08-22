import sys

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\general_chapter")

import imutils
import numpy as np
import argparse
import cv2 
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY_INV, 11, 4)

cv2.imshow("Mean", thresh)

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY_INV, 11, 3)

cv2.imshow("Gaussian Thresh", thresh)

cv2.waitKey(0)