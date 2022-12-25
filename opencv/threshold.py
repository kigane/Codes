import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from cv_utils import showimgs

def thresh_changing(img_gray):
    for i in range(256):
        ret, mask = cv.threshold(img_gray, i, 255, cv.THRESH_BINARY)
        cv.imshow('threshold change', mask)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
        elif cv.waitKey(25) & 0xFF == ord('s'):
            cv.waitKey(0)


if __name__ == '__main__':
    img = np.uint8([i for i in range(256)]*256)
    img = img.reshape((256, 256))
    # 灰度在100到255之间的像素灰度值设为255， 其他设为0
    # 参数: 灰度图像， 阈值， 最大值， 二值化方法
    # 返回值：阈值， 二值化图像
    # 全局阈值
    method = 'THRESH_BINARY'
    t = getattr(cv, method)
    ret, thresh1 = cv.threshold(img, 127, 255, t) # 超过阈值的设为最大值，没超的设为0
    ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
    ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) # 超过阈值的设为最大值，没超的不变
    ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)  # 超过阈值的不变，没超的设为0
    ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # 超过阈值的设为0，没超的不变
    titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    showimgs(2, 3, images, titles, cmap='gray')
    
    # 自适应阈值
    img = cv.imread('images/3in1.jpg')
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 参数：灰度图像， 最大值， 自适应算法， 二值化方法， 区块大小， 常数
    adthresh1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 21, 4)
    adthresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 4)
    titles = ['Origin', 'mean-c', 'gaussian']
    images = [img, adthresh1, adthresh2]
    # fig, axes, = plt.subplots(1, 3, figsize=(15, 5))
    # showimgs(axes, images, titles, cmap='gray')

    # Otsu二值化算法， 阈值会自动计算，所以第二个参数没用
    # ret2, th2 = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    # print(ret2)
    # cv.imshow('Otus', th2)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

