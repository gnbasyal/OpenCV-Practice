import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))        #"cv2.CAP_PROP_FRAME_WIDTH" can be replaced with its argument id: 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))       #"cv2.CAP_PROP_FRAME_HEIGHT" can be replaced with its argument id: 4

cap.set(3, 1280)        #Using argument id
cap.set(4, 720)         #Here the camera only takes resolution values available to it

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10,50), font, 1, (0, 255, 255), 2)
        frame = cv2.putText(frame, datet, (10,150), font, 1, (0, 255, 255), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



