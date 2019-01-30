# -*- coding:utf-8 -*-
import cv2
import seaborn as sns
from matplotlib import pyplot as plt


def draw_contour(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
    img_, cnts, hierancy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in cnts:
        if cv2.contourArea(cnt) > 10000:
            [x, y, width, height] = cv2.boundingRect(cnt)
            if (height > 400 and height < 500 and width > 800) or (width > 400 and width < 500 and height > 800):
                cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 20)
    return img


if __name__ == '__main__':
    file_dir = '../water_meter_images/IMG_.jpg'
    img = cv2.imread(file_dir)
    result = draw_contour(img)
    plt.imshow(result)
    plt.show()
    # cv2.imshow('display', img)
    # cv2.waitKey(0)
