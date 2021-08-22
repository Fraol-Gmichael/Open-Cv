import sys

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\chapter_7")

import imutils
import numpy as np
import argparse
import cv2 
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

row1 = np.hstack([image, cv2.blur(image, (3, 3)),])

row2 = np.hstack([cv2.blur(image, (5, 5)), cv2.blur(image, (7, 7))])

blurred = np.vstack([row1, row2])

#imutils.colored_1D(image)
#imutils.colored_1D(cv2.blur(image, (5, 5)))
#plt.show()

######### Gaussian Blur ##########
row1 = np.hstack([image, cv2.GaussianBlur(image, (3, 3), 0),])

row2 = np.hstack([cv2.GaussianBlur(image, (5, 5), 0), cv2.GaussianBlur(image, (7, 7), 0)])

gaussian_blurred = np.vstack([row1, row2])


######### Gaussian Blur ##########
row1 = np.hstack([image, cv2.GaussianBlur(image, (3, 3), 0),])

row2 = np.hstack([cv2.GaussianBlur(image, (5, 5), 0), cv2.GaussianBlur(image, (7, 7), 0)])

gaussian_blurred = np.vstack([row1, row2])

######### Median Blur ##########
row1 = np.hstack([image, cv2.medianBlur(image, 3)])

row2 = np.hstack([cv2.medianBlur(image, 5), cv2.medianBlur(image, 7)])

median_blurred = np.vstack([row1, row2])


#-------------------------- Bilateral Blur --------------------------------

row1 = np.hstack([image, cv2.bilateralFilter(image, 5, 21, 21),])

row2 = np.hstack([cv2.bilateralFilter(image, 7, 31, 31),
cv2.bilateralFilter(image, 9, 41, 41)])

bilateral_blurred = np.vstack([row1, row2])



cv2.imshow("Bilateral Blurred", bilateral_blurred)
cv2.waitKey(0)