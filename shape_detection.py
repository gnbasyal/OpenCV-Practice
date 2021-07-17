##THE IMAGE USED IS NOT THE BEST FOR THIS CODE##

import cv2

img = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow('img',img)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.015*cv2.arcLength(contour, True),True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 2)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx) == 4:
        cv2.putText(img, "Quadrilateral", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    elif len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))
    else:
        cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0))

cv2.imshow('shapes',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
