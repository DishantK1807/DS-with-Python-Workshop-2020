# -*- coding: utf-8 -*-
"""NumPy_Practice.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ja6URvZGEV6zCH464ukQahsY17N3WvMn
"""

import numpy as np

a = np.array([1,2,3], dtype = 'int64')

print(a)

a

type(a)

a.ndim

b = np.array([[1,2,3],[1,2,3]])

print(b)

b.ndim

type(b[0])

type(a[0])

a.itemsize

b.itemsize

b.nbytes

b.size

a.size

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])

print(a)

a[1,5]

a[:, : ]

a[1, 3 : -1 : 3]

a[1,5] = 31

a

a[0, :] = a[1,2]

a

c = np.array([[[1,2],[4,4],[3,4],[5,5]],[[1,2],[4,4],[3,4],[5,5]],[[1,2],[4,4],[3,4],[5,5]]])

print

c.ndim

c.shape

b

c = np.array([[[1, 2],[3,4]],[[2, 3],[7,8]]])

print(c)

c.shape

c[0][1] = [9,9]

c

c[1][1] = [8,8]

c

c.shape

#initializing different types of arrays

zero = np.zeros((3,3,3), dtype = 'int16')

zero.shape

zero

np.ones((3,3))

type(zero[0][0][1])

np.full((3,3), 100, dtype='int32')

np.full_like(zero, 8)

np.random.rand(4,2)

np.random.randint(1,6, size =(1,1))

np.identity(5)

arr = np.array([[1,2,3]])
r1 = np.repeat(arr, 3 , axis = 0)

r1.shape

##manipulating arrays , copyuing and stuff like that

output = np.ones((5,5))
print(output)

z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:-1,1:-1] = z

output

