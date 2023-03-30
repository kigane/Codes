import cv2 as cv

if __name__ == '__main__':
    flags = [i for i in dir(cv) if i.startswith('COLOR_')]
    print(flags)
    img = cv.imread('./images/lena512.bmp')
    # cv.imshow("Lena", img) # 窗口名称，ndarray类型图像
    # cv.waitKey(0)

    cv.namedWindow('image', cv.WINDOW_NORMAL)  # cv.WINDOW_NORMAL 可以调整窗口大小
    cv.imshow('image', img)
    
    key = cv.waitKey(0) & 0xFF

    if key == ord('s'):
        cv.imwrite('./images/lena.png', img)  # 文件名，ndarray类型图像
        cv.destroyAllWindows()
    else:
        cv.destroyAllWindows()

