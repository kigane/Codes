# cv.calcHist（images，channels，mask，histSize，ranges[，hist[，accumulate]]）
# images：它是uint8或float32类型的源图像。它应该放在方括号中，即“ [img]”。
# channels：也以方括号给出，是计算直方图的通道的索引。例如，如果输入为灰度图
# 像，则其值为[0]。对于彩色图像，可以传递[0]，[1]或[2]分别计算蓝色，绿色或红色通道的
# 直方图。
# mask：图像掩码。为了找到完整图像的直方图，将其指定为“无”。但是，如果要查找图像特
# 定区域的直方图，则必须为此创建一个掩码图像并将其作为掩码。
# histSize：这表示我们的BIN计数。需要放在方括号中。对于全尺寸，我们通过[256]
# ranges：这是我们的RANGE。通常为[0, 256]
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    img = cv.imread('images/lena512color.tiff', cv.IMREAD_GRAYSCALE)
    hist = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.hist(img.ravel(), 256, [0, 256])
    print(img.ravel().shape)
    plt.show()

    # img = cv.imread('images/lena512color.tiff')
    # color = ('b', 'g', 'r')
    # for i, col in enumerate(color):
    #     histr = cv.calcHist([img], [i], None, [256], [0, 256])
    #     plt.plot(histr, color=col)
    #     plt.xlim([0, 256])
    # plt.show()
