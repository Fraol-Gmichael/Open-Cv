import numpy as np
import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

blue = image[ : , : , 0]
green = image[ : , : , 1]
red = image[ : , : , 2]

b, g, r =   cv2.split(image)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

zeros = np.zeros(image.shape[:2], dtype="uint8")

blueHue = cv2.merge([b, zeros, zeros])
greenHue = cv2.merge([zeros, g, zeros])
redHue = cv2.merge([zeros, zeros, r])

customeHue = imutils.hueMaker(image, (0, 0, 0), hueto='b')

cv2.imshow("Green Hue", greenHue)
cv2.imshow("Red Hue", redHue)
cv2.imshow("Blue Hue", blueHue)
cv2.imshow("Custom", customeHue)

cv2.waitKey(0)
