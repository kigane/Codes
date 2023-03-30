import cv2 as cv
import numpy as np

if __name__ == '__main__':
    img1 = cv.imread('images/wbb.png')
    # 缩放
    img1 = cv.resize(img1, (600, 600), interpolation=cv.INTER_AREA)
    # 平移
    h, w = img1.shape[:2]
    M = np.float32([
        [1, 0, 100],
        [0, 1, 100],
    ])
    dst = cv.warpAffine(img1, M, (w, h))
    cv.imshow('translate', dst)
    # 旋转
    M = cv.getRotationMatrix2D((h / 2, w / 2), 45, 1)
    dst = cv.warpAffine(img1, M, (w, h))
    cv.imshow('translate', dst)
    # 仿射变换 - 变换后平行的线仍然保持平行
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(img1, M, (w, h))
    cv.imshow('translate', dst)
    # 透视变换
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(img1, M, (w, h))
    cv.imshow('translate', dst)

    cv.waitKey(0)
    cv.destroyAllWindows()
