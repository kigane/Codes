import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/lena512color.tiff')
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE,
                                      cv.CHAIN_APPROX_SIMPLE)
print(contours)
print('#######################')
print(hierarchy)
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
img = img[:, :, ::-1]
plt.imshow(img)
plt.show()

