from matplotlib import pyplot as plt
import numpy as np
import cv2

'''

figure = plt.figure()
ax = figure.add_subplot(111)
ax.set_title("Grayscale Histogram")
ax.set_ylabel("# of Bins")
ax.set_xlabel("Bins")
ax.plot(hist)
ax.set_xlim([0, 256])

'''


def colored_1D(image, title="Color Histogram", mask=None):

    chans = cv2.split(image)
    
    if len(chans) == 3:
        colors = ('b', 'g', 'r')
    if len(chans) == 1:
        colors = ('black',)

    figure = plt.figure()
    ax = figure.add_subplot()
    ax.set_title(title)
    ax.set_xlabel("Bins")
    ax.set_ylabel("# of bins")

    for chan, color in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

def colored_2D(image, mask=None):
    figure = plt.figure()
    num = 131
    chans = cv2.split(image)
    name = [' G and B',' G and R', ' B and R']
    arr = [[1, 0], [1, 2], [0, 2]]
    for i, each in enumerate(arr):
        ax = figure.add_subplot(num)
        num += 1
        hist = cv2.calcHist([chans[each[0]], chans[each[1]]], [0, 1], mask, [32, 32], [0, 256, 0, 256])

        p = ax.imshow(hist, interpolation='nearest')
        ax.set_title(f'2D Color Histogram for{name[i]}')
        plt.colorbar(p)
    
    print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))


def mask(image, center=None, width=50, rectangle=True):

    mask = np.zeros(image.shape[:2], dtype="uint8")
    center = np.array(center)
    if type(center) == np.array: 
        center = [image.shape[1]//2, image.shape[0]//2]
        start = center - width
        end = center + width
    else:
        start = center[0]
        end = center[1]   

    if rectangle:
        mask = cv2.rectangle(mask, start, end, 255, -1)
    else:
        mask = cv2.circle(mask, center, width, 255, -1)

    masked = cv2.bitwise_and(image, image, mask=mask)


    return mask, masked
