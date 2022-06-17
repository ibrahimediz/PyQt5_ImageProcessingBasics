import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 is the webcam

while True:
    ret, frame = cap.read() # ret is a boolean, frame is the image
    frame = cv2.resize(frame, (300, 200))
    # opencv de RGB değerleri 0-255 arasında değerler alıyor.
    # BGR olarak ele alınır
    cv2.line(frame, (0, 0), (300, 200), (255, 0, 0), 5)
    cv2.rectangle(frame,(100,100),(200,200),(255,0,0),-2)
    cv2.circle(frame,(150,150),50,(0,255,0),-1)
    cv2.putText(frame,"Python",(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()