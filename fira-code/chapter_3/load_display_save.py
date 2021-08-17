import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])

#print(f"width: {image.shape[1]}")
#print(f"height: {image.shape[0]}")
#print(f"channels: {image.shape[2]}")

#print(image)
print(image.shape)
#cv2.imshow("image", image)
#cv2.waitKey(0)
