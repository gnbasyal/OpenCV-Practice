import cv2

img = cv2.imread('baboon.jpg')
layer = img.copy()
gaus_pyr = [layer]

#Gaussian Pyramid
for i in range(3):
    layer = cv2.pyrDown(layer)
    gaus_pyr.append(layer)
    #cv2.imshow('L'+str(i),layer)

layer = gaus_pyr[2]
cv2.imshow('upper level gaussian', layer)
lap_pyr = [layer]

#Laplacian Pyramid
for i in range(3,0,-1):
    gaus_ext = cv2.pyrUp(gaus_pyr[i])
    laplacian = cv2.subtract(gaus_pyr[i-1], gaus_ext)
    cv2.imshow(str(i), laplacian)

'''for i in range(3):
    layer = cv2.pyrUp(layer)
    gaus_pyr.append(layer)
    cv2.imshow('U'+str(i),layer)'''

cv2.imshow("orig",img)
cv2.waitKey(0)
cv2.destroyAllWindows()