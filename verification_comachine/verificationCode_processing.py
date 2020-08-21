# -*- encoding: utf-8 -*-
"""
@File    : verificationCode_processing.py
@Time    : 2020/8/19 9:53
@Author  : Morde
@Software: PyCharm
@Description:验证码处理
"""
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm
from sklearn.neighbors import KNeighborsClassifier as KNN
# from sklearn.externals import joblib
import joblib


class VerificationCode:
    # @staticmethod
    # def get_img():
    #     page_snap_obj = Image.open('../imgs/1.jpg')
    #     image_obj = page_snap_obj.crop()
    #     # image_obj.show()
    #     return image_obj

    @staticmethod
    def delete_line(images):
        im = images.convert("L")
        # plt.imshow(img)
        im_z = np.array(im)  # im转化为im_z矩阵
        print(im_z.mean())  # im_z的平均值
        print(np.median(im_z))  # im_z的中位数
        plt.subplot(4, 2, 1)
        plt.imshow(np.array(im), cmap=cm.gray)
        im_b = im.point(lambda i: i > 199, mode='1')  # 用im_z的平均值199转化为黑白图像im_b
        plt.subplot(4, 2, 2)
        plt.imshow(im_b)  # 显示im_b
        im_a = im.point(lambda i: i > 220, mode='1')  # 用im_z的中位数220转化为黑白图像im_a
        plt.subplot(4, 2, 3)
        plt.imshow(im_a)
        im_f = im_b.filter(ImageFilter.MedianFilter(size=3))
        plt.subplot(4, 2, 4)
        plt.imshow(im_f)
        # plt.show()
        im = im_f
        print(im.size)
        a = np.array(im)  # im转化为a矩阵
        pd.DataFrame(a.sum(axis=0)).plot.line()  # 画出每列的像素累计值
        plt.imshow(a, cmap='gray')  # 画出图像
        split_lines = [7, 24, 38, 57, 73]  # 经过调整过的分割线的合理间距
        vlines = [plt.axvline(i, color='r') for i in split_lines]  # 画出分割线
        plt.show()
        '''
        y_min = 5
        y_max = 35
        # 设置获取图像的高和宽
        ims = []
        c = 1
        for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
            im.crop([x_min, y_min, x_max, y_max]).save('./p_pics/'+str(c) + '.png')
            # crop()函数是截取指定图像！
            # save保存图像！
            c = c + 1
        for i in range(1, 5):
            file_name = "./zxgk_yzm_split/{}.png".format(i)
            plt.subplot(4, 2, i)
            im = Image.open(file_name).convert("1")
            # im=img.filter(ImageFilter.MedianFilter(size=3))
            plt.imshow(im)
            # 显示截取的图像！
        plt.show()
        '''

    @staticmethod
    def img_process(name):
        path = "./zxgk_yzm/{}.png".format(str(name))
        img = Image.open(path).convert("L")
        th = np.array(img).mean()
        im_b = img.point(lambda i: i > th, mode='1')
        im_f = im_b.filter(ImageFilter.MedianFilter(size=3))
        split_lines = [7, 25, 43, 61, 79]
        y_min = 5
        y_max = 35
        ims = []
        c = 1
        for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
            im_f.crop([x_min, y_min, x_max, y_max]).save('./p_pics/{}-{}.png'.format(str(name), str(c))) # 切割图片
            c = c + 1
        # for i in range(0, 101):
        #     print("process {} pic".format(i))
        #     img_process(i)

    @staticmethod
    def Y():
        # 获取字符的值！这些验证码是我一个一个肉眼写出来的！
        with open("./pic_result/result.txt") as f:
            Y = list(f.read().replace("\n", ""))
        return Y

    @staticmethod
    def getX():
        # 获取X的值！
        path = "./p_pics/{}-{}.png"
        X = []
        for i in range(0, 101):
            for c in range(1, 5):
                img = Image.open(path.format(str(i), str(c)))
                ls = np.array(img).tolist()
                xx = []
                for l in ls:
                    for x in l:
                        xx.append(x)
                X.append(xx)
        return X

    # @staticmethod
    def train(self):
        # 用knn模型进行训练
        knn = KNN()
        knn.fit(self.getX(), self.Y())
        joblib.dump(knn, "./yzcode_model/model.pkl")
        # 保存结果！


if __name__ == '__main__':
    v = VerificationCode()
    v.train()


