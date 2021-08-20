import numpy as np
from matplotlib import pyplot as plt
import cv2 
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to image file")

args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

"""

figure = plt.figure()
ax = figure.add_subplot(111)
ax.set_title("Grayscale Histogram")
ax.set_ylabel("# of Bins")
ax.set_xlabel("Bins")
ax.plot(hist)
ax.set_xlim([0, 256])

"""

cv2.waitKey(0)