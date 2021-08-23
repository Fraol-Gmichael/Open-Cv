import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

resized = imutils.resize(image, 564)

cv2.imshow("Original", resized)
cv2.waitKey(0)
