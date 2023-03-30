import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('images/lena512color.tiff')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Lena', gray)
print(gray.shape)
gray_level = np.array(cv.split(gray)).flatten()

num_bins = 255

n, bins, patches = plt.hist(gray_level, bins=num_bins, facecolor='blue', alpha=0.3)
plt.show()
