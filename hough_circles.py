import numpy as np
import cv2
img = cv2.imread('smarties.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=40 )
#print(circles)

circles = circles[0]
#print(circles)
for circle in circles:
    x, y, r = circle
    #print (x,y,r)
    cv2.circle(img, (x,y), r, (0,0,0), 2)
    cv2.circle(img, (x, y), 2, (0, 255, 255), 2)

cv2.imshow('output',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
