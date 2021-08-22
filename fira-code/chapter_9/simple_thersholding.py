import sys

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\general_chapter")

import imutils
import numpy as np
import argparse
import cv2 
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])


def simple_tresh(image_org, t_value):
    image = cv2.cvtColor(image_org, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    (T, thresh) = cv2.threshold(blurred, t_value, 255, cv2.THRESH_BINARY)
    (T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
    coins = cv2.bitwise_and(image_org, image_org, mask=threshInv)
    print(coins.shape)

    return np.hstack([image_org, coins]), np.hstack([thresh, threshInv])

cv2.imshow("Coins", simple_tresh(image, 155)[0])
cv2.imshow("Thresholds", simple_tresh(image, 155)[1])

cv2.waitKey(0)
