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

f = image.astype(np.float32)/255.0

image = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
cv2.imshow("fira", image)
print(np.max(image))

cv2.waitKey(0)