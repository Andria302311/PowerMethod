import numpy as np
import scipy.sparse as sp
import time


def power_iteration(A, niter):
    tol = 10 ** (-9)
    Ashape = A.shape
    eigvec = np.random.rand(Ashape[0])
    eigval_old = np.dot(np.transpose(eigvec), A.dot(eigvec)) / np.dot(np.transpose(eigvec), eigvec)
    for i in range(niter):
        # calculate the matrix-by-vector product Ab
        eigvec1 = A.dot(eigvec)
        # calculate the norm
        eigvec1_norm = np.linalg.norm(eigvec1)
        # re normalize the vector
        eigvec = eigvec1 / eigvec1_norm
        # eigenvalue
        eigval_new = np.dot(np.transpose(eigvec), A.dot(eigvec)) / np.dot(np.transpose(eigvec), eigvec)
        if (abs(eigval_new - eigval_old) / eigval_new) < tol:
            return eigval_new
        eigval_old = eigval_new

    return eigval_new


def get_maxeigval(A):
    niter = 200000
    return power_iteration(A, niter)

import Set


x = np.array(Set.M, np.float)
print("Set of Leslie Matrix:")
print(x)
import numpy
#print(numpy.power(Matrix))
print("max eigenvalue")
print(get_maxeigval(x))

def Inverse(A):
    return np.linalg.pinv(A)

x_=Inverse(x)
print("Inverse:")
print(x_)
print("check Inverse correctness:")
print(np.allclose(x, np.dot(x, np.dot(Inverse(x), x))))


print("smallest eigenvalue (Inverse Power Method):")
print(get_maxeigval(x_))

def Compute2Norm(eigenvalue,eigenvector,matrix):
    return np.linalg.norm((matrix*eigenvector-eigenvector*eigenvalue), ord=2)

def CheckAccuracy(eigenvalues,eigenvectors,matrix):
    CheckerArray=[]
    for i in range(0,len(eigenvalues)):
        CheckerArray.append(Compute2Norm(eigenvalues[i],eigenvectors[i],matrix))
    return np.linalg.norm(CheckerArray)


def PowerShift(shift,DominantMatrix):
    shiftMatrix=np.identity(len(DominantMatrix))*shift
    print(shiftMatrix)
    return get_maxeigval(DominantMatrix-shiftMatrix)

print("PowerShift:")
print(PowerShift(0.2,x))

def FindAllEigenvalues(DominantMatrix,shift):
    eigenvalues=[]
    eigenvalues.append(get_maxeigval(DominantMatrix))
    for i in range(len(DominantMatrix)-1):
        eigenvalues.append(PowerShift(shift,DominantMatrix))
    return eigenvalues

print(FindAllEigenvalues(x,0.2))



