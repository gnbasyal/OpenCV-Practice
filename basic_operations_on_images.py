import numpy as np
import cv2

img = cv2.imread('messi5.jpg')
img2= cv2.imread('baboon.jpg')
print(img.shape)
print(img.size)

#splitting into b, g, r channels
'''b,g,r = cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)'''

#merging the b, g, r channels
'''img = cv2.merge((b,g,r))
cv2.imshow('image',img)'''

#copying one Region Of Interest (ROI) on another
'''ball = img[280:340, 330:390]
img[273:333, 100:160] = ball
cv2.imshow('image',img)'''

#adding two images
#note that the images should be of the same size
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
#img3 = cv2.add(img, img2)
img3 = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
cv2.imshow('image', img)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
























