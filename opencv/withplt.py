import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def showimg(ax, img, title=None):
    ax.imshow(img)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])

if __name__ == '__main__':
    img = cv.imread('./images/lena512color.tiff')
    img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    # b, g, r = cv.split(img) # 比较耗时
    # img3 = cv.merge([r, g, b])
    img3 = img[:, :, ::-1] # h, w, c | row, col, ch 
    _, axes = plt.subplots(1, 3, figsize=(4 * 3, 4))
    showimg(axes[0], img, 'cv raw BGR')
    showimg(axes[1], img2, 'cvtColor')
    showimg(axes[2], img3, 'split&merge')
    plt.show()
