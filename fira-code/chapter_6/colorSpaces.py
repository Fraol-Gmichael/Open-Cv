import numpy as np
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                 help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("L * A * B", lab)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

for each in [("GRAY", gray) ,("LAB", lab), ("HSV", hsv)]:
    print("{} {}".format(each[0], each[1][:5, :5]))

cv2.waitKey(0)