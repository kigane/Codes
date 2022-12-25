import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')

blank[:] = (0, 255, 0)  # BGR

cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 0), thickness=2)
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 100, (0, 255, 255), thickness=-1)
cv.line(blank, (0, 0), (500, 500), (0, 0, 0), thickness=1)
cv.putText(blank, "Hello World", (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 255), thickness=1)
cv.imshow('Draw Shape', blank)

cv.waitKey(0)
