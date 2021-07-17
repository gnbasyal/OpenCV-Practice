import numpy as np
import cv2
#img=cv2.imread('board.jpg',1)
img=np.ones([512,512,3],np.uint8)*255
#img=cv2.lineine(img,(0,0),(255,255),(255,0,0),2)
img=cv2.arrowedLine(img,(0,0),(255,255),(255,0,0),2)
img=cv2.rectangle(img,(384,0),(510,128),(0,0,255),-1)
img=cv2.circle(img,(50,50),50,(0,255,0),2)
img=cv2.putText(img,'OpenCV',(10,350),cv2.FONT_HERSHEY_COMPLEX,4,(255,255,255),5,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()