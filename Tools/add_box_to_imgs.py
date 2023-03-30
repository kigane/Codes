import cv2
import glob
import os

from region_zoom import draw_dotted_line2

# 获取所有要处理的图片的文件路径
# image_files = glob.glob("assets/tmp/*.png")
image_files = glob.glob(f"assets/quality/Pama*")

border_color = (0, 255, 0)
adain_top_14 = (360, 2, 200, 100)
adain_top_19 = (365, 2, 200, 100)
adain_leave_14 = (420, 528, 45, 70)
adain_leave_19 = (420, 513, 45, 70)
leave_zoomed_pos = (550, 400)

pama_raw_14 = (630, 120, 60, 90)
pama_raw_19 = (620, 80, 60, 90)

# 循环遍历每张图片，并添加矩形框
for image_file in image_files:
    # 读取图片
    img = cv2.imread(image_file)

    if '14' in image_file:
        # 定义矩形框的位置和大小 14
        x, y, w, h = pama_raw_14 
        cv2.rectangle(img, (x, y), (x+w, y+h), border_color, 2)

        # 第二个
        # 定位矩形 下方叶片
        x1, y1, w1, h1 = adain_leave_14
        # 放大后的矩形
        x2, y2, w2, h2 = *leave_zoomed_pos, 2*w1, 2*h1
        # 裁剪出局部图像
        roi = img[y1:y1+h1, x1:x1+w1]
        # 缩放局部图像 2x
        zoom_roi = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        # 嵌入
        img[y2:y2+h2, x2:x2+w2] = zoom_roi
        # 定位矩形框
        cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), border_color, 2) # 2表示线条宽度
        # 放大结果框
        cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), border_color, 2) # 2表示线条宽度
        # 虚线
        draw_dotted_line2(img, (x1+w1, y1), (x2, y2), border_color, 2, 10)
        draw_dotted_line2(img, (x1+w1, y1+h1), (x2, y2+h2), border_color, 2, 8)
    elif "19" in image_file:
        # 定义矩形框的位置和大小 19
        x, y, w, h = pama_raw_19 
        cv2.rectangle(img, (x, y), (x+w, y+h), border_color, 2)

        # 第二个
        # 定位矩形 下方叶片
        x1, y1, w1, h1 = adain_leave_19
        # 放大后的矩形
        x2, y2, w2, h2 = *leave_zoomed_pos, 2*w1, 2*h1
        # 裁剪出局部图像
        roi = img[y1:y1+h1, x1:x1+w1]
        # 缩放局部图像 2x
        zoom_roi = cv2.resize(roi, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        # 嵌入
        img[y2:y2+h2, x2:x2+w2] = zoom_roi
        # 定位矩形框
        cv2.rectangle(img, (x1, y1), (x1+w1, y1+h1), border_color, 2) # 2表示线条宽度
        # 放大结果框
        cv2.rectangle(img, (x2, y2), (x2+w2, y2+h2), border_color, 2) # 2表示线条宽度
        # 虚线
        draw_dotted_line2(img, (x1+w1, y1), (x2, y2), border_color, 2, 10)
        draw_dotted_line2(img, (x1+w1, y1+h1), (x2, y2+h2), border_color, 2, 8)
        
    # # Depth loss 
    # x, y, w, h = 5, 5, 160, 160 
    # # 绘制矩形框
    # cv2.rectangle(img, (x, y), (x+w, y+h), border_color, 2) # (0, 255, 0)表示矩形框颜色，2表示线条宽度
    # # 第二个
    # x, y, w, h = 495, 10, 180, 100 
    # cv2.rectangle(img, (x, y), (x+w, y+h), border_color, 2) # (0, 255, 0)表示矩形框颜色，2表示线条宽度
    # # 第三个
    # x, y, w, h = 70, 465, 85, 120 
    # cv2.rectangle(img, (x, y), (x+w, y+h), border_color, 2) # (0, 255, 0)表示矩形框颜色，2表示线条宽度
    # # 第四个
    # x, y, w, h = 306, 160, 115, 80 
    # cv2.rectangle(img, (x, y), (x+w, y+h), border_color, 2) # (0, 255, 0)表示矩形框颜色，2表示线条宽度

    # 显示或保存结果
    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    cv2.imwrite(f"assets/results/{os.path.basename(image_file)}", img)
