import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    _,frame = cap.read()

    cv2.circle(frame, (155, 120),5, (0,0,255), -1)
    cv2.circle(frame, (480, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (20, 475), 5, (0, 0, 255), -1)
    cv2.circle(frame, (620, 475), 5, (0, 0, 255), -1)

    #capture the points from the orig frame
    pts1 = np.float32([[155, 120],[480, 120],[20, 475],[620, 475]])
    #define the points in the resulting frame
    pts2 = np.float32([[0,0], [640, 0], [0,480], [640, 480]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    print(matrix)
    result = cv2.warpPerspective(frame, matrix, (640, 480))

    cv2.imshow("result", result)
    cv2.imshow("orig", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
