import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('j.png', 0)

#if image is not already a binary image
#img = cv2.imread('smarties.png', 0)
#_, mask = cv2.threashold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(img, kernel, iterations=2)
erosion = cv2.erode(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
morph_grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

titles = ['image', 'dilation', 'erosion', 'opening', 'closing', 'morph gradient', 'top hat', 'black hat']
images = [img, dilation, erosion, opening, closing, morph_grad, top_hat, black_hat]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()




























