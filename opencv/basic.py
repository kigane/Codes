import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from cv_utils import showimgs


if __name__ == '__main__':
    img1 = cv.imread('images/blue-ball.jpg')
    img1 = cv.resize(img1, (800, 600), interpolation=cv.INTER_AREA)

    img1gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
    # 灰度在 100 到 255 之间的像素灰度值设为 255， 其他设为 0
    ret, mask = cv.threshold(img1gray, 180, 255, cv.THRESH_BINARY)
    mask_inv = cv.bitwise_not(mask)
    # src1[i] & src2[i] if mask[i] != 0
    img1_font = cv.bitwise_and(img1, img1, mask=mask)

    img2 = cv.imread('images/wbb.png')
    img2 = cv.resize(img2, (800, 600), interpolation=cv.INTER_AREA)

    rows, cols, chs = img1.shape
    roi = img2[0:rows, 0:cols]
    img2_bg = cv.bitwise_and(roi, roi, mask=mask_inv)

    img4 = cv.add(img1_font, img2_bg)

    img3 = cv.addWeighted(img1, 0.3, img2, 0.7, gamma=0) # 图片融合

    imgs = np.array([img1, img2, img3, img1_font, img2_bg, img4])
    imgs = imgs[:, :, :, ::-1]
    titles = ['cat', 'wbb', 'addWeight', 'font', 'bg', 'bitwise op']
    fig, axes = plt.subplots(2, 3)
    showimgs(axes, imgs, titles)
    
