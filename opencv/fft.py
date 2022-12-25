import sys
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from PIL import Image, ImageOps
from cv_utils import *

if __name__ == '__main__':
    img = cv.imread('images/link.png', 0)
    # img = cv.imread('images/001.jpg', 0)
    # f = np.fft.fft2(img) # 快速傅里叶变换
    # fshift = np.fft.fftshift(f) # 将零频率分量移到图像中间
    # magnitude_spectrum = 20*np.log(np.abs(fshift))
    # plt.subplot(121), plt.imshow(img, cmap='gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    # plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    # plt.show()

    # rows, cols = img.shape
    # crow, ccol = rows//2, cols//2
    # # 高通滤波(把FFT变换，平移后的图像的中心的低频部分去除)
    # fshift[crow-30:crow+31, ccol-30:ccol+31] = 0  # 矩形掩码会导致振铃效应
    # f_ishift = np.fft.ifftshift(fshift) # 把DC分量移回左上角
    # img_back = np.fft.ifft2(f_ishift) # 逆傅里叶变换，复原图像
    # img_back = np.real(img_back)
    # plt.subplot(131), plt.imshow(img, cmap='gray')
    # plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(132), plt.imshow(img_back, cmap='gray')
    # plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
    # plt.subplot(133), plt.imshow(img_back)
    # plt.title('Result in JET'), plt.xticks([]), plt.yticks([])
    # plt.show()


    # CV
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * \
        np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dft_shift[..., 0], cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    sys.exit()

    rows, cols = img.shape
    crow, ccol = rows//2, cols//2
    # 首先创建一个掩码，中心正方形为1，其余全为零
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow-30:crow+30, ccol-30:ccol+30] = 1
    # 应用掩码和逆DFT
    fshift = dft_shift*mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img_back, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
