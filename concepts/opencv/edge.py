import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from cv_utils import showimgs

if __name__ == '__main__':
    img = cv.imread('images/sudoku.png')
    img = img[:, :, ::-1]
    # img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # _, img = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)

    # ddepth 用于设置期望的输出数据类型。通常不用管。
    sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
    sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)
    # laplacian 的 ksize=1 相当于使用 3x3 的经典 kernel
    laplacian = cv.Laplacian(img, cv.CV_64F, ksize=1)

    # 注意
    # 从黑到白的过渡被视为正斜率，而从白到黑的过渡被视为负斜率。如果使用
    # CV_8U或np.uint8类型，则从白到黑的过渡会被忽略。
    # 解决方法是先是使用有符号类型，在取绝对值，最后转回去。
    img1 = np.zeros((600, 600), np.uint8)
    img1[100:400, 100:400] = 255
    sobelx_8u = cv.Sobel(img1, cv.CV_8U, 1, 0, ksize=5)
    sobelx_f = cv.Sobel(img1, cv.CV_64F, 1, 0, ksize=5)
    sobel_abs = np.absolute(sobelx_f)
    sobel_8u = np.uint8(sobel_abs)

    images = [img, sobelx, sobely, laplacian, 
              img1, sobelx_8u, sobel_8u]
    titles = ['Origin', 'sobelx', 'sobely', 'laplacian',
              'Square', 'sobelx_8u', 'sobel_8u']

    showimgs(2, 4, images, titles, cmap='gray')
