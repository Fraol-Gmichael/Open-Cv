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
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", image)

blurred = cv2.GaussianBlur(gray, (11, 11), 0)

edged = cv2.Canny(blurred, 30, 150)

"""edged2 = np.zeros(edged.shape, dtype="uint8")
edged3 = cv2.merge([edged, edged2, edged2])
cv2.imshow("Edged", edged)"""

cents, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

coins = image.copy()

cv2.drawContours(coins, cents, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)

for (i, c) in enumerate(cents):
    # We can compute the 'bounding box' for each contour, which is
    # the rectangle that encloses the contour
    (x, y, w, h) = cv2.boundingRect(c)

    # Now that we have the contour, let's extract it using array
    # slices
    print("Coin #{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    cv2.imshow("Coin", coin)

    # Just for fun, let's construct a mask for the coin by finding
    # The minumum enclosing circle of the contour
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
	
cv2.waitKey(0)