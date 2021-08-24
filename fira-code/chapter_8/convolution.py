import sys

from numpy.core.fromnumeric import shape

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\chapter_7")

import imutils
import numpy as np
import argparse
import cv2 
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
                help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = image.astype(np.float32)/255.0
kernel = np.float32([[1, 0, -1], [1, 0, -1], [1, 0, -1]])

#kernel2 = np.ones([5, 5], dtype="float32")/25
#image = cv2.filter2D(image,-1,kernel2)
#image = cv2.GaussianBlur(image, (5, 5), 0)

dst2 = cv2.filter2D(image,-1,kernel)
dst2 = np.absolute(dst2)
kernel = kernel.transpose()

dst = cv2.filter2D(image,-1,kernel)
dst = np.absolute(dst)

dst4 = (dst*dst) + (dst2*dst2)
magnitude = np.sqrt(dst4).astype(np.float32)

cv2.imshow("Image", image)
cv2.imshow("Blurred", dst)

cv2.imshow("Blurred2", dst2)
cv2.imshow("Blurred4", magnitude)

cv2.waitKey(0)

