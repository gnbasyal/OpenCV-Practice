import numpy as np
import cv2 as cv

def change(x):
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s:
        img[:] = [b, g, r]
    else:
        img[:] = 0

    cv.imshow('image', img)


img = np.zeros((300,512,3), np.uint8)
cv.imshow('image',img)

switch = '0 : OFF\n1 : ON'
cv.createTrackbar('B','image',0,255,change)
cv.createTrackbar('G','image',0,255,change)
cv.createTrackbar('R','image',0,255,change)
cv.createTrackbar(switch,'image',0,1,change)

cv.waitKey(0)
cv.destroyAllWindows()

