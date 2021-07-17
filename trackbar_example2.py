import cv2 as cv

def update(x):
    img = cv.imread('messi5.jpg')
    cp = cv.getTrackbarPos('CP','image')
    font = cv.FONT_HERSHEY_SIMPLEX
    img = cv.putText(img, str(cp), (10,100), font, 2, (0,0,255), 2)
    switchval = cv.getTrackbarPos('color/gray','image')
    if switchval:
        img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imshow('image',img2)
    else:
        cv.imshow('image',img)


img = cv.imread('messi5.jpg')
cv.imshow('image',img)
cv.createTrackbar('CP','image',10,400,update)
cv.createTrackbar('color/gray','image',0,1,update)
cv.waitKey(0)
cv.destroyAllWindows()

