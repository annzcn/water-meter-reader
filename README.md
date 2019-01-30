### 项目内容：
&emsp;读取数字式水表表头；目前思路分为两种：一采用OpenCV先对数字进行分割，再进入训练模块；二是直接对数字区域进行打标，以识别区域重合度和数字识别准确率同时作为模型训练优化指标；

### 更新日志：
- **2019年1月30日**：采用OpenCV读取水表图像中的轮廓，以轮廓包围面积先做一轮筛选；又因水表读数区域轮廓近似矩形，以轮廓矩形长宽做二轮筛选；对于角度正确的图片适用，对于读数区域倾斜的情况仍然存在问题；

### 当前效果：
- 对于读数区域垂直或水平的情况，OpenCV目前能够较好地识别读数区域，如图所示：
![Image text](https://github.com/LaterBetterThanNever/water-meter-reader/blob/master/display/1-30-1.png)
- 对于读数区域倾斜的情况，无法通过边缘矩阵的长宽识别，如图所示：
![Image text](https://github.com/LaterBetterThanNever/water-meter-reader/blob/master/display/1-30-2.png)

### 遗留问题：
- [ ] 可通过仿射变换先将图片的读数区域转正再通过OpenCV识别读数区域；
