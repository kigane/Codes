import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from cv_utils import showimgs


if __name__ == '__main__':
    img = cv.imread('images/monkey.tiff')
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # 均值滤波
    blur = cv.blur(img, (5, 5))
    # 第二个参数是深度ddepth 用于设置期望的输出数据类型。通常设为-1就行。
    # normalize=True则相当于blur，否则kernel前系数为1.
    box_filter = cv.boxFilter(img, -1, (5, 5), normalize=True)
    # 高斯滤波 第三个参数是sigmaX,为0则表示从核的宽高自动计算
    gaussian_blur = cv.GaussianBlur(img, (5, 5), 0)
    # 中位滤波
    median_blur = cv.medianBlur(img, 5)
    # 双边滤波
    bilateral_filter = cv.bilateralFilter(img, 9, 75, 75)
    
    images = [img, blur, box_filter, gaussian_blur,
              median_blur, bilateral_filter]
    titles = ['Origin', 'Mean Blur', 'box_filter',
              'gaussian_blur', 'median_blur', 'bilateral_filter']
    showimgs(2, 3, images, titles)
    print(blur == box_filter)
