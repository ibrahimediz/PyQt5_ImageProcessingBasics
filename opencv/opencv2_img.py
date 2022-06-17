import cv2
import numpy as np

img = cv2.imread("opencv/pictures/resimler.jpeg")
cv2.imshow("pencere",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
