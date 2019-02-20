# -*- coding:utf-8 -*-
import cv2
import seaborn as sns
from matplotlib import pyplot as plt


def img_processing(img):
    dst = cv2.GaussianBlur(img, (9, 9), 0)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    return dst

def draw_contour(img):
    ret, thresh = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    img_, cnts, hierancy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        if cv2.contourArea(cnt) > 10000:
            print('此轮廓的面积 = ', cv2.contourArea(cnt))
            [x, y, width, height] = cv2.minAreaRect(cnt)
            if (height > 400 and height < 500 and width > 800) or (width > 400 and width < 500 and height > 800):
                cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 20)
    return thresh, img

if __name__ == '__main__':
    img = cv2.imread('../water_meter_images/IMG_0544.jpg')
    dst = img_processing(img)
    thresh, result = draw_contour(dst)
    plt.subplot(121)
    plt.imshow(thresh, cmap='gray')
    plt.subplot(122)
    plt.imshow(result)
    plt.show()
