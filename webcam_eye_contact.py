import cv2
import numpy as np

def change(x):
    pass

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv2.putText(frame, strXY, (x, y), font, 0.5, (255,255,0), 2)
        cv2.imshow("orig", frame)

cap = cv2.VideoCapture(0)
cv2.namedWindow("select corner")
cv2.createTrackbar('corner','select corner',0,3,change)
blank = np.zeros((480, 640, 3),np.uint8)
h = blank.shape[0]
w = blank.shape[1]

pts = np.array([[0,0],[w,0],[w,h],[0,h]])
frame = cv2.polylines(blank, [pts], 1, (0,255,0), 3)
#cv2.imshow('blank',blank)

while 1:
    _,frame = cap.read()

    cv2.circle(frame, (20, 0), 5, (0, 0, 255), -1)
    cv2.circle(frame, (620, 0), 5, (0, 0, 255), -1)
    cv2.circle(frame, (50, 475), 5, (0, 0, 255), -1)
    cv2.circle(frame, (590, 475), 5, (0, 0, 255), -1)

    frame = cv2.add(frame, blank)
    #capture the points from the orig frame
    pts1 = np.float32([[20, 0],[620, 0],[50, 475],[590, 475]])
    #define the points in the resulting frame
    pts2 = np.float32([[0,0], [640, 0], [0,480], [640, 480]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    #print(matrix)
    result = cv2.warpPerspective(frame, matrix, (640, 480))

    cv2.imshow("result", result)
    cv2.imshow("orig", frame)

    cv2.setMouseCallback('orig', click_event)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
