import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Einstein-S&P.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
g_blur = cv2.GaussianBlur(img, (5,5), 0)
median = cv2.medianBlur(img, 5)
bil_filter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image','2D conv','blur','GaussianBlur','median blur','bilateralFilter']
images = [img, dst, blur, g_blur, median, bil_filter]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()