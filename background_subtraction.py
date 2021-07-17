import numpy as np
import cv2

cap = cv2.VideoCapture('data/vtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2()
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=0)
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

while 1:
    ret, frame = cap.read()
    if not ret:
        cap = cv2.VideoCapture('data/vtest.avi')
        continue

    fgmask = fgbg.apply(frame)
    #fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    objects = cv2.bitwise_and(frame, frame, mask=fgmask)
    cv2.imshow('frame', frame)
    cv2.imshow('FG mask frame', fgmask)
    cv2.imshow('objects', objects)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()