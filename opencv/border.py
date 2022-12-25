import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from functools import partial


def showimg(ax, img, title=None):
    ax.imshow(img)
    ax.set_title(title)
    ax.set_xticks([])
    ax.set_yticks([])


if __name__ == '__main__':
    BLUE = [255, 0, 0]
    img = cv.imread('./images/lena512color.tiff')
    img = img[:, :, ::-1]
    makeBorder = partial(cv.copyMakeBorder, img, 80, 80, 80, 80)
    borders = [cv.BORDER_REPLICATE, cv.BORDER_REFLECT,
               cv.BORDER_REFLECT101, cv.BORDER_WRAP]
    constant = makeBorder(cv.BORDER_CONSTANT, value=BLUE)
    _, axes = plt.subplots(2, 3)
    axes = axes.reshape(-1)
    imgs = [img]+[makeBorder(x) for x in borders]+[constant]
    titles = ['img', 'replicate', 'reflect', 'reflect101', 'warp', 'constant']

    for i, image, title in zip(range(6), imgs, titles):
        print(image.shape)
        showimg(axes[i], image, title)
    plt.show()
