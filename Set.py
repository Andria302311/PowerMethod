# set randmly F(n)

import random

print(random.random())

def setF(n):
    F=[]
    for i in range(0,n):
        i=random.random()
        F.append(i)
    return F

F=setF(5)
print(setF(5))


def setS(m):
    S = []
    for i in range(0, m):
        i = random.random()
        S.append(i)
    return S
print(setS(4))
S=setS(4)


def setMatrix(F,S):
    import numpy as np
    M=[]

    for i in range(0,len(F)):
        row=[]
        for j in range(0,len(F)):
            if(j==i-1):
                row.append(S[i-1])
            else:
                row.append(0)
        if (i == 0):
            M.append(F)
        else:
            M.append(row)
    return M

M=setMatrix(F,S)
print(M)