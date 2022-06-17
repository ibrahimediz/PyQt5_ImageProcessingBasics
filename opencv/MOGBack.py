import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 is the webcam
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read() # ret is a boolean, frame is the image
    frame = cv2.resize(frame, (300, 200))
    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', frame)
    cv2.imshow("Maske",fgmask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()