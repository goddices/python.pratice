import numpy as np
import matplotlib.pyplot as plt

def putVector(v,color):
    plt.arrow(0,0,v[0],v[1],color=color,
            length_includes_head=True,# 增加的长度包含箭头部分
            head_width=0.4, head_length=0.4)

c = 1+1j 
a=np.array([1,1])
M=np.array([[1,1],[0,1]])
b=np.dot(a,M)

M1 = np.array([[4,3],[6,1]])
M2 = np.array([[2,5],[1,3]])
print(np.dot(M1,M2))
print(np.dot(M2,M1))

# print(a)
# print(b)
 
# plt.xlim(-5,5)
# plt.ylim(-5,5) 
# putVector(a,'r')
# putVector(b,'b')



# plt.show()



