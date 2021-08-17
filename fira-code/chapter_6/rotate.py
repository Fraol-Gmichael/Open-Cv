import numpy as np
import argparse
import cv2 
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)


shifted = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", shifted)

cv2.waitKey(0)
