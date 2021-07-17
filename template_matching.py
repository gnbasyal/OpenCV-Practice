import cv2
import numpy as np

img = cv2.imread('messi5.jpg')
grey = cv2.imread('messi5.jpg',0)
template = cv2.imread('messi5_face.jpg',0)
w,h = template.shape[::-1]

res = cv2.matchTemplate(grey, template, cv2.TM_CCOEFF_NORMED)
cv2.imshow('result',res)
th = 0.8
loc = np.where(res >= th)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w,pt[1]+h),(0,0,255),2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()