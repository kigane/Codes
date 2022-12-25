import cv2 as cv

if __name__ == '__main__':
    capture = cv.VideoCapture('./Cameras.mp4')

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    writer = cv.VideoWriter('test.avi', fourcc, 20, (800, 600))


    for i in range(18):
        print(capture.get(i)) # 视频的基本信息
        # 可以使用capture.set(propid, val)修改?
        # 3 宽
        # 4 高
        # 5 帧率

    while capture.isOpened():
        isTrue, frame = capture.read()

        if isTrue:
            # frame = cv.resize(frame, (800, 600), interpolation=cv.INTER_AREA)
            
            cv.imshow('GMTK Video', frame)
            writer.write(frame)

            # 用cv.waitKey(20)控制播放速度
            if cv.waitKey(20) & 0xFF == ord('q'):
                break
        else:
            break
    
    capture.release()
    writer.release()
    cv.destroyAllWindows()
