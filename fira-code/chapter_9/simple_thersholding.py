import sys

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\chapter_7")

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

(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Threshold Binary Inv", threshInv)
cv2.imshow("Image", image)

coins = cv2.bitwise_and(image, image, mask=threshInv)
cv2.imshow("Coins", coins)

cv2.waitKey(0)
