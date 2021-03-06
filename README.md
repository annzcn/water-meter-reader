### 项目内容：
&emsp;读取数字式水表表头；目前思路分为两种：一采用OpenCV先对数字进行分割，再进入训练模块；二是直接对数字区域进行打标，以识别区域重合度和数字识别准确率同时作为模型训练优化指标；

### 更新日志：
- **2019年1月30日**：采用OpenCV读取水表图像中的轮廓，以轮廓包围面积先做一轮筛选；又因水表读数区域轮廓近似矩形，以轮廓矩形长宽做二轮筛选；对于角度正确的图片适用，对于读数区域倾斜的情况仍然存在问题；
- **2019年2月13日**：以自适应阈值算法代替原本的Otsu阈值算法进行二值化，保证了数字与背景不会因图像灰度不一致而产生粘连；通过腐蚀和膨胀去除了图像中的噪声点；
- **2019年2月20日**：先用Canny边缘检测，用面积和最小包围矩形长宽比做限定，找到读数区域，并用最小包围矩形返回的倾斜度数对图像进行仿射变换，校正图像的倾斜；
- **2019年2月23日**：分割出数字区域

### 当前效果：
- 采用自适应阈值算法，窗口大小设置为99，以每一个窗口计算一个阈值进行二值化，得到的图片如图所示：
![Image text](https://github.com/LaterBetterThanNever/water-meter-reader/blob/master/display/2-13-3.png)
- 通过腐蚀与膨胀操作，去除噪点，增强读书区域的清晰度，效果如图所示：
![Image text](https://github.com/LaterBetterThanNever/water-meter-reader/blob/master/display/2-13-4.png)
- 已能清晰识别读数区域，并完成倾斜图像的校正工作；
![Image text](https://github.com/LaterBetterThanNever/water-meter-reader/blob/master/display/2-20-1.png)
![Image text](https://github.com/LaterBetterThanNever/water-meter-reader/blob/master/display/2-23-1.png)

### 遗留问题：
- [x] 可通过仿射变换先将图片的读数区域转正再通过OpenCV识别读数区域；
- [x] 描绘图像的水平与垂直投影图，分割出读数区域；
- [x] 分割每一位数字，并扔进模型训练；
- [x] 通过模型训练，准确率为98.1%
- [ ] 需要更多的数据集（视频采样）
