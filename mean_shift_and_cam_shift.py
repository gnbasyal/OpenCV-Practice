import numpy as np
import cv2

cap = cv2.VideoCapture('slow_traffic_small.mp4')

#take first frame
ret, frame = cap.read()

#define initial location of car window
x,y,w,h = 300,200,100,50
track_window = (x,y,w,h)

#define region of interest
roi = frame[y:y+h, x:x+w]
#cv2.imshow('roi',roi)
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0, 60, 32)), np.array((180, 255, 255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
#print(roi_hist)
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
#print(roi_hist)

#define term criteria, either 10 iterations or move by atleast 1 point
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while 1:
    ret, frame = cap.read()
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180], 1)

        #apply meanshift/camshift to get new location
        #ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)
        print(ret)

        #draw on image for meanShift
        #x,y,w,h = track_window
        #final_img = cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 3)

        #draw on image for CamShift
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        print(pts)
        final_img = cv2.polylines(frame, [pts], 1, (0,255,0), 2)

        cv2.imshow('dst',dst)
        cv2.imshow('frame', final_img)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()