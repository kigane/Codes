import cv2 as cv
import numpy as np

if __name__ == '__main__':
    # 查找指定颜色的HSV值
    color = np.array([[[0, 0, 255]]], dtype=np.uint8)
    color_hsv = cv.cvtColor(color, cv.COLOR_BGR2HSV)
    print(color_hsv)

    img = cv.imread('images/wbb.png')

    lowerb = np.array([0, 0, 0])
    upperb = np.array([120, 120, 120])
    mask = cv.inRange(img, lowerb, upperb)

    cv.imshow('mask', mask)
    cv.waitKey(0)

    cv.destroyAllWindows()
