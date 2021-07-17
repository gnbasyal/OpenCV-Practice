###DOESN'T WORK USING MATPLOTLIB

import cv2

def change(x):
    pass

img = cv2.imread('messi5.jpg',0)

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar',512,100)
cv2.createTrackbar('th1','Trackbar',0,255,change)
cv2.createTrackbar('th2','Trackbar',0,255,change)

while 1:
    th1 = cv2.getTrackbarPos('th1', 'Trackbar')
    th2 = cv2.getTrackbarPos('th2', 'Trackbar')
    canny = cv2.Canny(img, th1, th2)

    cv2.imshow('image',img)
    cv2.imshow('Canny',canny)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()























