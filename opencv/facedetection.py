import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 is the webcam
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

i = 0
while True:
    ret, frame = cap.read() # ret is a boolean, frame is the image
    frame = cv2.resize(frame, (600, 400))
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler = face_cascade.detectMultiScale(gri,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        roi_gri = gri[y:y+h,x:x+w]
        roi_frame = frame[y:y+h,x:x+w]
        if cv2.waitKey(2) & 0xFF == ord("t"):
            cv2.imwrite(f"ornekler/resim_{i}.jpg",roi_gri)
            i +=1
        gozler = eye_cascade.detectMultiScale(roi_gri)
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()