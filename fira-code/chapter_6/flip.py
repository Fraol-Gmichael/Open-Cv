import numpy as np
import argparse
import cv2 
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

flipped = cv2.flip(flipped, 0)
cv2.imshow("Flipped Horizontally and Vertically", flipped)

flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)


cv2.waitKey(0)