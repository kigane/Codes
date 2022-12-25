import cv2 as cv

def slide(img1, img2):
    img1 = cv.resize(img1, (800, 600), interpolation=cv.INTER_AREA)
    img2 = cv.resize(img2, (800, 600), interpolation=cv.INTER_AREA)
    cv.imshow('image', img1)
    for i in range(100):
        alpha = i / 100.
        beta = 1. - i / 100.
        img = cv.addWeighted(img1, alpha, img2, beta, gamma=0)
        cv.imshow('image', img)
        if cv.waitKey(20) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    img1 = cv.imread('images/cat.jpg')
    img2 = cv.imread('images/cat2.jpg')
    slide(img1, img2)
    cv.waitKey(0)
    cv.destroyAllWindows()

