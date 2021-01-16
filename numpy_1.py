import numpy as np 
a = np.array([1,2,3,4,5,6]) #one dimensional array
b = np.array([[1,2],[3,4],[5,6]]) #2 dimensional array
#printing the arrays
print(a)
print(b)


#MATRIX:

# BI-DIMENSIONAL 
c = np.array([[1,2,3],[4,5,6]])
print(c)

#shape of matrix
shape_matrix = c.shape
print(shape_matrix)

#dimension of matrix
dimension_mat = c.ndim
print(dimension_mat)

#re-shaping the arrays
#(we know that we have declared "a" as a linear array ,so now we'll try to reshape this array and turn it into a 2x3 matrix)

a2 = a.reshape(2,3)
print(a2)

a3 = a.reshape(3,2)
print(a3)

#3 dimensional array
e = np.array([1,2,3,4,5,6,7,8,9,0,12,69])
a4 = e.reshape(2,3,2)
print(a4)
f = a4.ndim
print(f) #printing the dimension

#everything in one line: 
g = np.array([1,2,3,4,5,6]).reshape(2,3).ndim #in this line we are declaring the array and reshaping it and checking the dimensions altogether
print(g)

#resizing the array

#(now we know that we reshaped the array a quite a few times...so lets see what happened to the array a itself)
print(a)
##as we can see in the output the array a is still a linear array ...that means while we were reshaping the array it just reshapes and used accd to that following command but the array itself doesnt change at all
##to change the shape of the array we need to use resize()

a.resize(3,2)
print(a) ## as we can see the array itself got changed

#data type of an array:
print(a.dtype) #here we get int32 it means all the elements of the array is integer

flt = np.array([1,2,3,4.5,6,7,8]).dtype
print(flt)#float64 stands for any elemnts..atleast one element in the array is a float number
 
compx = np.array([1,2,3,4+7j,5,6]).dtype
print(compx) #o/p is complex128 means atleast one value in the array is complex number

##we can also change datatype of an array 
flt2 = np.array([1,2,3,4.5,6,7,8],dtype = int)
print(flt2) #as we're changing the dat type from float to inyteger the value after point is removed automatixally
flt3 = np.array([1,2,3,4.5,6,7,8],dtype = complex)
print(flt3) #every elemnt is turned in complex manner

#special arrays
##1 : ZERO ARRAYS
zero= np.zeros(6) #the number written in the bracket is the no. of elements that is the number of zeros in the array
print(zero)

zero2= np.zeros((2,3)) #declaring the dimension of zero array
print(zero2)

##2 one array
one = np.ones(4)
print(one)

one2 = np.ones((2,3))
print(one2)

##3 CONSTANT ARRAYS
const = np.full((6,2),69)
print(const)

##4 identity matrix 
iden = np.eye(6)
print(iden)

##MATRIX WITH RANDOM NUMBERS

rndm_mat = np.random.random((3,3))
print(rndm_mat)


#printing simple series as arrays with arrange()
arrng = np.arange(1,69,2.3) #arange(starting,ending,difference)
print(arrng)

arrng2 = np.arange(1,12,3).reshape(2,2)
print(arrng2)

#to create equidistant points using linspace()
lnspce = np.linspace(0.1,0.9,4) #(starting point,ending point,number of equidistant points)
print(lnspce)
















