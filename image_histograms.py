import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')
#img = np.zeros((200,200), np.uint8)
#cv2.rectangle(img,(0,100),(200,200),(255),-1)
#cv2.rectangle(img,(0,50),(100,100),(127),-1)

histB = cv2.calcHist([img],[0],None,[256],[0,256])
histG = cv2.calcHist([img],[1],None,[256],[0,256])
histR = cv2.calcHist([img],[2],None,[256],[0,256])
plt.plot(histB)
plt.plot(histG)
plt.plot(histR)
plt.show()
print(histB)

'''b,g,r = cv2.split(img)
cv2.imshow('image',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

plt.hist(b.ravel(), 256,[0,256],color='blue')
plt.hist(g.ravel(), 256,[0,256],color='green')
plt.hist(r.ravel(), 256,[0,256],color='red')
plt.show()'''

cv2.waitKey(0)
cv2.destroyAllWindows()