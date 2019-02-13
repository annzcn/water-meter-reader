# -*- coding:utf-8 -*-
import cv2
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt


# 全局阈值方法效果不佳，数字与背景产生黏连
def ostu(img):
    ret, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return dst

def AdaptiveThreshold(img):
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 99, 5)
    return thresh

# 开运算
def OpenOperation(img):
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(img, kernel, iterations=1)
    erosion = cv2.erode(dilation, kernel, iterations=3)
    return erosion

if __name__ == '__main__':
    img = cv2.imread('../water_meter_images/IMG_1359.jpg')
    dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = AdaptiveThreshold(dst)
    dst = OpenOperation(img)

    plt.subplot(121)
    plt.imshow(img, cmap='gray')
    plt.subplot(122)
    plt.imshow(dst, cmap='gray')
    plt.show()

