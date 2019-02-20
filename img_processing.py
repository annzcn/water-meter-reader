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

# 照片大小均为3024*4032
def findContours(original, img):
    minmumOfPictureArea = 3024*4032*0.02
    maxOfPictureArea = 3024*4032*0.06
    _, contours, hierachy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    contoursToFind = []
    angleToRotate = 0.0
    rotateFlag = False
    for contour in contours:
        contourArea = cv2.contourArea(contour)
        if (contourArea>=minmumOfPictureArea) and (contourArea<=maxOfPictureArea):
            ret = cv2.minAreaRect(contour)
            weight = ret[1][0]
            height = ret[1][1]
            rateOfWeightToHeight = 0.0
            rateOfHeightToWeight = 0.0
            if (weight > 0.0 and height > 0.0):
                rateOfWeightToHeight = weight / height
                rateOfHeightToWeight = height / weight
            if (rateOfHeightToWeight> 3.5 and rateOfHeightToWeight<3.8) or (rateOfWeightToHeight>3.5 and rateOfWeightToHeight<3.8):
                if(weight > height):
                    rotateFlag = True
                print(ret)
                contoursToFind.append(contour)
                cv2.drawContours(original, contour, -1, (255, 0, 0), 10)
                angleToRotate = ret[2]
                center = ret[0]
    # if(len(contoursToFind)!=1): 若识别到的轮廓数不等于1，记得改写！
    return img, angleToRotate, center, rotateFlag


# 旋转图像
def rotate(img, angle, center=None, scale=1.0):
    height, weight = img.shape[:2]
    if center is None:
        center = (weight/2, height/2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotatedImg = cv2.warpAffine(img, M, (weight, height))
    return rotatedImg

if __name__ == '__main__':
    img = cv2.imread('../water_meter_images/IMG_0546.jpg')
    angleToratate = 0.0
    dst = bilateralFilter(img)
    dst = greyWorld(dst)
    dst = contrastEnhancement(dst)
    dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    dst = AdaptiveThreshold(dst)
    dst = OpenOperation(dst)
    dst, angleToratate, center, rotateFlag = findContours(img, dst)
    if rotateFlag :
        dst = rotate(img, 180 + angleToratate)
    else:
        dst = rotate(img, 90 + angleToratate)

    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(dst, cmap='gray')
    plt.show()

