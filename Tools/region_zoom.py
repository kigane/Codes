from math import sqrt
import cv2
import glob
import os
import numpy as np
from icecream import ic

def draw_dotted_line2(img, p1, p2, color, thickness, n):
    # n 线段数
    w = p2[0] - p1[0]
    h = p2[1] - p1[1]
    l = sqrt(w * w + h * h)
    # 矫正线长度，使线个数为奇数
    m = l / n
    m = m + 1 if m % 2 == 0 else m
    n = l / m
    n = int(n)

    cv2.circle(img, p1, 1, color, thickness) # 画起点
    cv2.circle(img, p2, 1, color, thickness) # 画终点
    # 画中间点
    if (p1[1] == p2[1]): #水平线：y = m
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        for x in np.linspace(x1, x2, n)[:-1]: 
            cv2.line(img, (x, p1[1]), (x + n, p1[1]), color, thickness)
    elif (p1[0] == p2[0]): #垂直线, x = m
        y1 = min(p1[1], p2[1])
        y2 = max(p1[1], p2[1])
        for y in np.linspace(y1, y2, n)[:-1]:
            cv2.line(img, (p1[0], y), (p1[0], y + n), color, thickness)
    else: # 倾斜线，与x轴、y轴都不垂直或平行
        # 直线方程的两点式：(y-y1)/(y2-y1)=(x-x1)/(x2-x1) -> y = (y2-y1)*(x-x1)/(x2-x1)+y1
        n1 = n * abs(w) / l
        k = h / w
        x1 = min(p1[0], p2[0])
        x2 = max(p1[0], p2[0])
        for x in np.linspace(x1, x2, n)[:-1]:
            p3 = (int(x), int(k * (x - p1[0]) + p1[1]))
            p4 = (int(x + n1), int(k * (x + n1 - p1[0]) + p1[1]))
            ic(p3)
            ic(p4)
            cv2.line(img, p3, p4, color, thickness, lineType=cv2.LINE_AA)


if __name__ == '__main__':
    # 获取所有要处理的图片的文件路径
    image_files = glob.glob("assets/quality/*.png")

    show_one = False

    for image_file in image_files:
        img = cv2.imread(image_file)
        # 定位矩形 下方叶片
        x1, y1, w1, h1 = 420, 528, 45, 70
        # 放大后的矩形
        x2, y2, w2, h2 = 550, 400, 2*w1, 2*h1
        # 裁剪出局部图像
        roi = img[y1:y1+h1, x1:x1+w1]
        # 缩放局部图像 2x
        zoom_roi = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        # 创建一个和原图像大小相同的掩码
        result = img.copy()
        result[y2:y2+h2, x2:x2+w2] = zoom_roi
        # 定位矩形框
        cv2.rectangle(result, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2) # (0, 255, 0)表示矩形框颜色，2表示线条宽度
        # 放大结果框
        cv2.rectangle(result, (x2, y2), (x2+w2, y2+h2), (0, 0, 255), 2) # (0, 255, 0)表示矩形框颜色，2表示线条宽度
        # 虚线
        draw_dotted_line2(result, (x1+w1, y1), (x2, y2), (0, 0, 255), 2, 10)
        draw_dotted_line2(result, (x1+w1, y1+h1), (x2, y2+h2), (0, 0, 255), 2, 8)

        # 显示结果
        if not show_one:
            cv2.imshow('result', result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            show_one = True
        cv2.imwrite(f"assets/results/{os.path.basename(image_file)}", result)
