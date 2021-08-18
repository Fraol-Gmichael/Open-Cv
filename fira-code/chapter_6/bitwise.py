import cv2 
import argparse
import numpy as np
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

negattedImage = np.bitwise_not(image)
cv2.imshow("Negated", negattedImage)


rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

cv2.imshow("Circle", circle)

bitwiseAnd = np.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)

bitwiseOr = np.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)

bitwiseXor = np.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor)

bitwiseNot = np.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)

cv2.waitKey(0)