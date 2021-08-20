import numpy as np
from matplotlib import pyplot as plt
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to image file")

args = vars(ap.parse_args())

image = cv2.imread(args['image'])

cv2.imshow("Original", image)

imutils.colored_1D(image)

imutils.colored_2D(image)

# 3D Histogram #
hist = cv2.calcHist([image], [0, 1, 2], None, [
                    8, 8, 8], [0, 256, 0, 256, 0, 256])

# plt.colorbar(p)

plt.show()
cv2.waitKey(0)
