import imutils
import numpy as np
import argparse
import cv2 


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

'''
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1]//2, image.shape[0]//2)
cv2.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)

masked = cv2.bitwise_and(image, image, mask = mask)

'''

masked = imutils.mask(image, width=300, rectangle=False)

cv2.imshow("Mask Applied to Image", masked)


cv2.waitKey(0)