import numpy as np
import argparse
import cv2 
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

shifted = imutils.translate(image, 25, 50)
cv2.imshow("Shifted down and Right", shifted)

shifted = imutils.translate(image, -50, -90)
cv2.imshow("Shifted UP and Left", shifted)

cv2.waitKey(0)
