import numpy as np

print('the version of Numpy is:'+np.__version__+'\n')

print(np.array([1,2,3]))    #一维数组

print(np.zeros((3,3)))      #二维数组

print(np.ones((2,3,4)))     #3维数组

print(np.arange(5))         #等差数组

print(np.arange(6).reshape(2,3))    #二维等差数组

print(np.eye(4))        #unit matrix

print(np.linspace(1,10,num=10))      #same gap one dimmen array

print(np.random.rand(3,3))          #random array

print(np.random.randint(6, size=(3,3)))       #random int array

print(np.fromfunction(lambda i,j:i+j,(5,5)))        #based on function
