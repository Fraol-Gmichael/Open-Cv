import sys
sys.path.append(r"C:\Users\gyon\Desktop\Open Cv\fira-code\general_chapter")

from matplotlib import pyplot as plt
import mahotas
import cv2
import argparse
import numpy as np
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Image", image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow("Blurred", image)
canny = cv2.Canny(image, 150, 255)

cv2.imshow("Canny", canny)


cv2.waitKey(0)

