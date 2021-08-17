import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Add the path of the image here")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])


height, width, channels = image.shape
print('height', height)
print('width', width)
print('channels', channels)

cv2.imshow("Image", image)
cv2.waitKey(0)

for each in range(int(height)):
	image[each] = np.array(list(reversed(image[each])))


cv2.imshow("Image", image)
cv2.waitKey(0)