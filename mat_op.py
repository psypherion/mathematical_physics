#matrix addition
import numpy as np
fst_mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
snd_mat = np.array([[12,23,34],[45,56,67],[69,69,69]])
add_mat = np.add(fst_mat,snd_mat)    #matrix addition
mult_mat = np.matmul(fst_mat,snd_mat) #matrix multiplication
dot_mat = np.dot(fst_mat,snd_mat)     #dot product of matrix
print(fst_mat,snd_mat,add_mat,mult_mat,dot_mat)
