import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from cv_utils import showimgs


if __name__ == '__main__':
    img = cv.imread('images/pikachu.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)

    kernel = np.ones((5, 5), dtype=np.uint8)
    # iteration 表示要使用几轮erode运算
    # anchor=point(x, y) 指定结构元素的锚点，默认是(-1,-1)，即中心点
    erode = cv.erode(img, kernel, iterations=1)
    dialate = cv.dilate(img, kernel, iterations=1)
    # open 先侵蚀再扩张
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    # close 先扩张再侵蚀
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
    # gradient 扩张-侵蚀
    gradient1 = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    # tophat input-open
    tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    # blackhat input-close
    blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


    images = [img, erode, dialate, opening, closing,
             gradient1, tophat, blackhat]
    titles = ['Origin', 'Erode', 'Dialate', 'Opening', 'Closing',
              'Gradient', 'Tophat', 'Blackhat']

    showimgs(2, 4, images, titles, cmap='gray')

    # opencv提供的获得结构元素的方法
    se_rect = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    se_ellipse = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    se_cross = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))

    print(se_rect)
    print(se_ellipse)
    print(se_cross)
