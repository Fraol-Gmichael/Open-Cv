import numpy as np
import cv2 
import argparse
import imutils
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to image file")

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

equalized = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, equalized]))


imutils.colored_1D(equalized)
imutils.colored_1D(image)

plt.show()

cv2.waitKey(0)
