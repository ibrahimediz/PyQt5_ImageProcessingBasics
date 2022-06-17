import cv2
from cv2 import threshold
import numpy as np

img = cv2.imread("opencv/pictures/ornekler1.jpeg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #  [0-255,0-255,0-255] => [0-255]
retval,th1 = cv2.threshold(gri,100,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
retval,th3 = cv2.threshold(gri,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("pencere",th1)
cv2.imshow("pencere1",gri)
cv2.imshow("pencere2",th2)
cv2.imshow("pencere3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()
