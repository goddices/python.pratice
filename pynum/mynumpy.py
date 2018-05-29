 
import numpy



array1 = numpy.array(  
    [[1,-1,0.11] ,
     [2,-3,0.50],
     [12,-34,0.45],
     [4,-99,0.99],
     [12,-7,0.75]]
)

# print('\rslice array1[0,:] = ', array1[0,:])
# print('\rslice array1[:,0] = ', array1[:,0])
# print('\rslice array1[:,:] = ', array1[:,:])
# print('\rslice array1[:,1:3] = ', array1[:,1:3])
# print('\rslice array1[:,0:1] = ', array1[:,0:1])
# print('\rtype of array1 = ' , type(array1))
# print('\rtype of array1[:,0] = ' , type(array1[:,0]))

# matrix1 = numpy.mat(array1)
# matrix2 = matrix1.T
# print('slice matrix1[0,:] = ', matrix1[0,:])
# print('matrix1 type ',type(matrix1),' matrix1 = ', matrix1)
# print('matrix2 type ',type(matrix2),' matrix2 = ', matrix2)

# array2 = numpy.array([1,2,3,4,5,6])
# print('array2 = ' , array2[...,None])
# print(numpy.asmatrix(array2).T)

matrix3=numpy.asmatrix([[0,1],[1,0]])
print(numpy.linalg.det(matrix3))
print(matrix3)
print(matrix3.transpose())
print(matrix3.A)
print(numpy.zeros([1,2]))
print(type(numpy.zeros([1,2])))
 