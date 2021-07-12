from sklearn import linear_model   # 表示，可以调用sklearn中的linear_model模块进行线性回归。
from sklearn import neighbors
import numpy as np
# 颜色值参考自  http://www.wahart.com.hk/rgb.htm
# 本例用 线性回归算法 X是RGB特征空间y是大概的人类分类空间
# 回归大概的颜色值

# 定义：
# X 是训练集的特征空间 RGB space
# y 是训练集的分类结果空间
X = [
    [255, 0, 0],  # red
    [255, 48, 48],
    [255, 64, 64],
    [178, 34, 34],
    [255, 106, 106],
    [238, 99, 99],
    [255, 99, 71],

    [0, 100, 0],  # green
    [85, 107, 47],
    [143, 188, 143],
    [46, 139, 87],
    [60, 179, 113],
    [32, 178, 170],
    [152, 251, 152],
    [34, 139, 34],
    [173, 255, 47],
    [0, 255, 0],

    [255, 255, 0],  # yellow
    [238, 201, 0],
    [255, 215, 0],
    [205, 173, 0],
    [255, 193, 37],
    [238, 173, 14],
    [255, 215, 0],
    [218, 165, 32],


    [25, 25, 112],  # blue
    [0, 0, 128],
    [255, 215, 0],
    [0, 191, 255],
    [100, 149, 237],
    [0, 0, 205],
    [65, 105, 225],
    [0, 0, 255],
]
y = [[1],
     [1],
     [1],
     [1],
     [1],
     [1],
     [1],

     [2],
     [2],
     [2],
     [2],
     [2],
     [2],
     [2],
     [2],
     [2],
     [2],


     [3],
     [3],
     [3],
     [3],
     [3],
     [3],
     [3],
     [3],



     [4],
     [4],
     [4],
     [4],
     [4],
     [4],
     [4],
     [4],
     ]
label = {1: '红色', 2: '绿色', 3: '黄色', 4: '蓝色'}
model = linear_model.LinearRegression()
model.fit(X, y)

a = model.predict([[235, 197, 16]])
# a[0][0]实际上这个值是浮点数
print('线性回归的预测颜色是：', label[int(a[0][0])])

model2 = neighbors.KNeighborsClassifier()
model2.fit(X, y)
b = model.predict([[235, 197, 16]])
print('KNN分类的预测颜色是：', label[int(b[0][0])])