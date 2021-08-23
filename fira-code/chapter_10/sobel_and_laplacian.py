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

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

cv2.imshow("Laplacian", lap)

cv2.waitKey(0)
