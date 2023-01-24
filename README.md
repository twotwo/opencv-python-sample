# opencv-python-sample

OpenCV(v4.7) for Python(v3.7)

## Create Project

```bash
poetry new opencv-python-sample
cd opencv-python-sample
poetry add opencv-python>=4.7.0 jupyter>=1.0.0
```

## Run Jupyter Notebook

```bash
poetry shell
poetry install
jupyter notebook --no-browser &
```

## Image Processing Tutorials

OpenCV Tutorials/ [Image Processing (imgproc module)](https://docs.opencv.org/4.7.0/d7/da8/tutorial_table_of_content_imgproc.html)

|  Category  | Topic  | Code |
| ----- | ----- | ----- |
|  Basic  | OpenCV 简介 | [01_start.ipynb](./01_start.ipynb)  |
|  Basic  | 图像平滑处理 | [05_smoothing.ipynb](./05_smoothing.ipynb)  |
|  Basic  | 形态学操作 | [01_morphology.ipynb](./06_morphology.ipynb)  |
|  Basic  | 阈值处理 | [04_threshold.ipynb](./04_threshold.ipynb)  |
|  Transformations  | 边缘检测 | [08_canny-edge-detection.ipynb](./08_canny-edge-detection.ipynb)  |
|  Transformations  | 仿射变换| |
|  Transformations  | | |
|  Transformations  | | |
|  Histograms  | 直方图处理 | [10_histograms.ipynb](./10_histograms.ipynb)  |
|  Contours  | 图像轮廓 | [09_contours.ipynb](./09_contours.ipynb)  |

OpenCV-Python Tutorials / [Image Processing in OpenCV](https://docs.opencv.org/4.7.0/d2/d96/tutorial_py_table_of_contents_imgproc.html)

| Topic  | Code |
| ----- | ----- |
| OpenCV 简介 | [01_start.ipynb](./01_start.ipynb)  |
| 色彩空间类型转换 | [02_colorspace.ipynb](./02_colorspace.ipynb)  |
| 几何变换 | [03_geometry.ipynb](./03_geometry.ipynb)  |
| 阈值处理 | [04_threshold.ipynb](./04_threshold.ipynb)  |
| 图像平滑处理 | [05_smoothing.ipynb](./05_smoothing.ipynb)  |
| 形态学操作 | [06_morphology.ipynb](./06_morphology.ipynb)  |
| 图像梯度 | [07_gradients.ipynb](./07_gradients.ipynb)  |
| 边缘检测 | [08_canny-edge-detection.ipynb](./08_canny-edge-detection.ipynb)  |
| 图像轮廓 | [09_contours.ipynb](./09_contours.ipynb)  |
| 直方图处理 | [10_histograms.ipynb](./10_histograms.ipynb)  |
