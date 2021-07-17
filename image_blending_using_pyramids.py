import cv2
import numpy as np

apple = cv2.imread('data/apple.jpg')
orange = cv2.imread('data/orange.jpg')
print(apple.shape)
print(orange.shape)
apple_orange = np.hstack((apple[:,:256], orange[:,256:]))

#generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

#generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

#generate Laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5,0,-1):
    gaus_ext = cv2.pyrUp(gp_apple[i])
    lap = cv2.subtract(gp_apple[i-1], gaus_ext)
    lp_apple.append(lap)

#generate Laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5,0,-1):
    gaus_ext = cv2.pyrUp(gp_orange[i])
    lap = cv2.subtract(gp_orange[i-1], gaus_ext)
    lp_orange.append(lap)

#Now add left and right halves in each level
apple_orange_pyr = []
for apple_lap, orange_lap in zip(lp_apple, lp_orange):  #This is a way to iterate in 2 lists
    cols, rows, ch = apple_lap.shape
    lap = np.hstack((apple_lap[:,:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyr.append(lap)

#now reconstruct
apple_orange_rec = apple_orange_pyr[0]
for i in range(1,6):
    apple_orange_rec = cv2.pyrUp(apple_orange_rec)
    apple_orange_rec = cv2.add(apple_orange_pyr[i], apple_orange_rec)

cv2.imshow('apple',apple)
cv2.imshow('orange',orange)
cv2.imshow('apple_orange',apple_orange)
cv2.imshow('apple_orange_rec',apple_orange_rec)
cv2.waitKey(0)
cv2.destroyAllWindows()