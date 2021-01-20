#algebra with arrays: 
import numpy as np
a =np.array([1,2,3.0,4,5,6,7,8,9])
b = np.array([69,420,333,111,2,96,66,99,6969])
print(a)
print(b)
c = a+b
print(c)

d = b-a
print(d)

e = b*a
f = b/a
print(e)
print(f)

#sum of all elements in an array:

sum1 = sum(a)
print(sum1)
sum2 = sum(b)
print(sum2)

max_a = max(a)
max_b = max(b)
print(max_a , max_b)

avg = np.average(a)
avg1 = np.average(b)
print(avg , avg1)

g = np.full(6,5)
print(g)

#g1 = np.fill(1)
#print(g1)

#logspace()
h = np.logspace(1,5,23)    #numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)
print(h)

#fill()
i2 = np.array([1,2,3,4,5,69,96,66])
print(i2)
i2.fill(2)   #fills the array with scalar value
print(i2) 

#astype
ma = a.astype(int)
print(ma)

print(h[0:3])  #indexing
print(h[3:])   #slicing

v = np.array([1,2,3,4,5,69,96,66])
print(v.reshape(4,2))
x = np.array([[1,2,3,3],[1,5,6,7]])

print(np.ravel(x))
                                                #see the basic difference between ravel and flatten
print(x.flatten())

#vstack : stacks elements of two arrays in vertically order thst is along row
v1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
v2 = np.array([[12,23,45],[45,56,78],[89,100,210]])
print(v1)
print(v2)
print(np.vstack((v1,v2)))
#hstack : stacks element in horizontally order that is along coloumn
print(np.hstack((v1,v2)))

fg = np.arange(6)
print(fg)














