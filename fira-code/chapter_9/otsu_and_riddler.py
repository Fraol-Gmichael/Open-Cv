import sys

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\general_chapter")

import imutils
import numpy as np
import argparse
import cv2
import mahotas
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image_org = cv2.imread(args['image'])

image = cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(image, (5, 5), 0)


T = mahotas.thresholding.otsu(blurred)
T = mahotas.thresholding.rc(blurred)

image = imutils.simple_tresh(image_org, T)
print(T)
cv2.imshow("Image", image[1])
cv2.waitKey(0)