import cv2
import matplotlib.pyplot as plt

opencv_color = ('b','g','r')

def draw_rgb_lines(img, title=["Blue", "Green", "Red"]):
    """画出三通道图像的直方图
    Parameters
    ----------
    img: 原始图像
    titles: 三通道标题
    """
    for i,col in enumerate(opencv_color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr, color=col, label=title[i])
        plt.xlim([0,256])
    plt.legend(title, loc="upper right")
    plt.show()

def subplot(rows, columns, images, titles):
    """画出多张图像的函数
    Parameters
    ----------
    rows, columns: 画框的行和列
    images: 图像数组
        图像总数不要超过 rows * columns
    titles: 图像标题数组
    Returns
    -------
    """
    N = 2
    # create figure size: width * height
    fig = plt.figure(figsize=(columns * N, rows * N))
    for i, img in enumerate(images):
        # Adds a subplot at i+1 position
        fig.add_subplot(rows, columns, i+1)
        # showing image
        plt.imshow(img)
        plt.axis("off")
        plt.title(titles[i])
