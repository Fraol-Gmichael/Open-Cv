import sys

sys.path.append( r"C:\Users\gyon\Desktop\Open Cv\fira-code\chapter_7")

import imutils
import numpy as np
import argparse
import cv2 
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, 
                help="Path to image file")

args = vars(ap.parse_args())
image = cv2.imread(args['image'])

kernel = np.ones((5, 5), np.float32)/25

dst = cv2.filter2D(image,-1,kernel)

#plt.subplot(121), plt.imshow(image), plt.title('Original')
#plt.xticks([]), plt.yticks([])
#plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
#plt.xticks([]), plt.yticks([])
#plt.show()

cv2.imshow("Image", image)
cv2.imshow("Blurred", dst)

cv2.waitKey(0)

