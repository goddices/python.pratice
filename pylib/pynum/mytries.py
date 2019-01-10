import numpy

#解释 numpy array
#原文链接：https://docs.scipy.org/doc/numpy-1.13.0/user/quickstart.html

ar1=numpy.array([[1,2,3],[5,7,100]])
print(ar1.ndim)     #ndim = numpy dimensions 维度
print(ar1.shape)    #形状,(m,n) m行n列, 此例是2维的 
print(ar1.size)     #数组中有多少元素
print(ar1.dtype)    #元素的数据类型 int32 int64 complex

ar2=numpy.zeros((3,4),dtype=int)
#zeros((3,4),dtype=int)创建一个3行4列的int类型的2维数组
#类似的还有ones
print(ar2)

ar3=numpy.arange(0,24,dtype=int).reshape(2,3,4)
#arange(a,b)生成a到b的1维数组
#reshape(x,y,z) 转换成x行y列z高的N维数组
print(ar3)

ar4=numpy.array([[2,3,4],[5,6,7]]) *  numpy.array([[10,20,30],[40,50,100]])
#元素乘法 *
print(ar4)

ar5=numpy.array([[2,3],[5,6]]).dot(numpy.array([[10,20],[40,50]]))
#矩阵乘法 dot
print(ar5)

ar6=numpy.random.random((4,5))
print(ar6,ar6.sum(),ar6.max() )
#random.random随机生产一个数组,sum()求和,max()求最大值

ar7=numpy.arange(10)**3
print("array 7 = ",ar7," its index [2] element = ",ar7[2])
print("ar7[2:5] = ",ar7[2:5])#arr[2:5]访问 [2],[3],[4],数学上是[m,n)
ar7[:6:2]=-100;print(ar7)#等同于[0:6:2],意为下标范围[0,6)隔2个元素,赋值为-100
print(ar7[::-1])#数组倒过来

def f(x,y):
    return 10*x+y
ar8 = numpy.fromfunction(f,(5,4),dtype=int)
print(ar8)
print(ar8[2,3]) #第2行第3列元素
print(ar8[0:4,1])#第[0,4)行,第1列元素 ,生成1维数组
print(ar8[1:3,:])#第[1,3)行,所有列元素 ,生成2维数组


ar9= numpy.array([1,2,3,4,5,6]).transpose()
print(ar9)

weights=numpy.array([[2],[3],[4]])
dataSets=numpy.array([[2,3,4],[5,6,7],[10,3,42]])
print(weights)
print(dataSets)
print(weights*dataSets)
              
ar10 = numpy.array([[0.5,11], [1,10], [1.2,9.5],[1.5,8.6],[2,12]])
print("ar10  x is \n",ar10[:,0])
print("ar10  y is \n",ar10[:,1])