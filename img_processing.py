# -*- coding:utf-8 -*-
import cv2
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt


# 双边滤波
def bilateralFilter(img):
    dst = cv2.bilateralFilter(img, 5, 21, 21)
    return dst


# 灰度世界调整光线平衡
def greyWorld(img):
    img = img.transpose(2, 0 ,1).astype(np.uint8)
    averageOfB = np.average(img[0])
    averageOfG = np.average(img[1])
    averageOfR = np.average(img[2])
    average = (averageOfB + averageOfG +averageOfR) / 3
    img[0] = np.minimum(img[0] * (average/averageOfB), 255)
    img[1] = np.minimum(img[1] * (average/averageOfG), 255)
    img[2] = np.minimum(img[2] * (average/averageOfR), 255)
    img = img.transpose(1, 2, 0).astype(np.uint8)
    return img


# 对比度增强
def contrastEnhancement(img):
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    channels = cv2.split(ycrcb)
    cv2.equalizeHist(channels[0], channels[0])
    cv2.merge(channels, ycrcb)
    dst = cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR)
    return dst


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
    img = cv2.imread('../water_meter_images/IMG_0597.jpg')
    dst = bilateralFilter(img)
    dst = greyWorld(dst)
    dst = contrastEnhancement(dst)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    dst = AdaptiveThreshold(dst)
    dst = OpenOperation(dst)

    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(dst, cmap='gray')
    plt.show()

