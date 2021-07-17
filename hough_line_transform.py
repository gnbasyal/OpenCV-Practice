import cv2
import numpy as np

img = cv2.imread('sudoku.png')
gray = cv2.imread('sudoku.png',0)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
print(img.shape)
#print(lines)

for line in lines:
    r,theta = line[0]

    '''a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * r
    y0 = b * r'''

    #this is a method to calculate 2 extreme points given r and theta
    x1 = int(r * np.cos(theta) - 1000 * np.sin(theta))
    y1 = int(r * np.sin(theta) + 1000 * np.cos(theta))
    x2 = int(r * np.cos(theta) + 1000 * np.sin(theta))
    y2 = int(r * np.sin(theta) - 1000 * np.cos(theta))

    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()