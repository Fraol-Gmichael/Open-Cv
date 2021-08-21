import imutils
import numpy as np
import argparse
import cv2 
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

imutils.colored_1D(image, "Original Histogram Image")

mask , masked= imutils.mask(image, [(15, 15), (130, 100)])
cv2.imshow("Mask", masked)

imutils.colored_1D(masked, mask=mask)

plt.show()
cv2.waitKey(0)