import cv2 
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

cv2.imshow("Original", image)

cropped = imutils.crop(image, [50, 50], [300, 300])
cv2.imshow("Cropped", cropped)


cv2.waitKey(0)