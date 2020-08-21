# -*- encoding: utf-8 -*-
"""
@File    : yuce.py
@Time    : 2020/8/19 13:33
@Author  : Morde
@Software: PyCharm
@Description: 预测验证码
"""

from sklearn.neighbors import KNeighborsClassifier as KNN
import joblib
from PIL import Image, ImageFilter
import numpy as np
MODEL_PATH = "./yzcode_model/model.pkl"


def getX(file_name):
    X = []
    img = Image.open(file_name).convert("L")
    th=np.array(img).mean()
    im_b = img.point(lambda i: i > th, mode='1')
    im_f = im_b.filter(ImageFilter.MedianFilter(size=3))
    split_lines = [7, 25, 43, 61, 79]
    y_min = 5
    y_max = 35
    for x_min, x_max in zip(split_lines[:-1], split_lines[1:]):
        ls=np.array(im_f.crop([x_min, y_min, x_max, y_max])).tolist()
        xx=[]
        for l in ls:
            for x in l:
                xx.append(x)
        X.append(xx)
    return X


def predict():
    # 预测
    file_path = './zxgk_yzm/{}.png'
    knn = joblib.load(MODEL_PATH)
    for i in range(0, 20):
        X = getX(file_path.format(i))
        Y = knn.predict(X)
        yield Y


for yzm in predict():
    print("".join(yzm))