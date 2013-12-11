import numpy
import time

begin = time.time()

f = open('pb_81_path_sum.txt', 'r')
l=[]
for line in f:
    l.append(line)
for i in range(0,len(l)):
    l[i]=l[i][:-1]
    l[i]=l[i].split(',')
    for j in range(len(l[i])):
        l[i][j]=int(l[i][j])

A=numpy.matrix(l)
# A = numpy.matrix([[4,3,5],[6,1,2],[9,7,8]])

submat_min_path={}

def min_path_sum(A,submat_min_path):
    if A.shape[0]==1 or A.shape[1]==1:
        submat_min_path[A.shape]=A.sum()
        return A.sum()
    else:
        higherMat=A[:-1,:]
        leftMat=A[:,:-1]
        if higherMat.shape not in submat_min_path:
            submat_min_path[higherMat.shape]=min_path_sum(higherMat,submat_min_path)
        if leftMat.shape not in submat_min_path:
            submat_min_path[leftMat.shape]=min_path_sum(leftMat,submat_min_path)
        return min(submat_min_path[higherMat.shape],submat_min_path[leftMat.shape]) + A[-1,-1]

print "Min path sum is", min_path_sum(A,submat_min_path)

end = time.time()
print end-begin
