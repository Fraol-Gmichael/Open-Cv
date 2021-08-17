import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="Add the path of the image here")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])
height, width, channels = image.shape

#for each in range(int(height)):
	#image[each] = np.array(list(reversed(image[each])))
image[0:100, 0:100] = np.flip(image[0:100, 0:100])


b, g, r = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# affect some part from the image 
snipped = image[0:int(height/4), 0:width].copy()
image[0:int(height/4), 0:width] = [0, 255, 0]

cv2.imshow("Image", image)
#cv2.imshow("Snipped", snipped)
cv2.waitKey(0)
