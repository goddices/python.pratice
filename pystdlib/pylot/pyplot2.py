# -*- coding: UTF-8 -*-
# By Yohanna: Finished in 2017/7/22
# Have a nice weekend
import matplotlib.pyplot as plt
import numpy as np

apple = np.array([[0.5,11], [1,10], [1.2,9.5],[1.5,8.6],[2,12]])
banana = np.array([[0.5,1], [1,2], [1.2,1.5],[1.5,1.6],[2,2]])
 
plt.scatter(np.array([0.5,1,1.5,2,2.5,3,3.5]), np.array([1,2,1,1.5,0.6,1.2,1.1]), color='yellow', linewidths=0.05)
plt.scatter(np.array([0.5,1,1.5,2,2.5,3,3.5]), np.array([4.1,5.2,6.9,7.8,6.8,5.2,5.2]), color='red',linewidths=0.5)
plt.axis([0, 4, 0, 10]) #设置坐标轴的[xmin, xmax, ymin, ymax]
plt.show()