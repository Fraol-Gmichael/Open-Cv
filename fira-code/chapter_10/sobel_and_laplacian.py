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

# Laplacian transform
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplacian", lap)

# Sobel transform
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)
print(np.max(sobelCombined))

cv2.imshow("Sobel X", sobelX)
print(np.max(sobelX))
cv2.imshow("Sobel Y", sobelY)
print(np.max(sobelY))
cv2.imshow("Sobel Combined", sobelCombined)

cv2.waitKey(0)
