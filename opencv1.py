import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 is the webcam

while True:
    ret, frame = cap.read() # ret is a boolean, frame is the image
    frame = cv2.resize(frame, (640, 480))
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, "FPS: " + str(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()