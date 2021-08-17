import cv2 
import imutils
import argparse
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

print(f"Max of 255: {cv2.add(np.uint8([200]), np.uint8([100]))}")
print(f"Max of 255: {cv2.subtract(np.uint8([50]), np.uint8([100]))}")

print(f"Wrap Arround: {np.uint8([200]) + np.uint8([116])}")
print(f"Wrap Arround: {np.uint8([50]) - np.uint8([100])}")

added = imutils.arithmetic(image, 50, True)
cv2.imshow("added", added)

subtracted = imutils.arithmetic(image, 50, subtract=True)

cv2.imshow("subtracted", subtracted)

cv2.waitKey(0)