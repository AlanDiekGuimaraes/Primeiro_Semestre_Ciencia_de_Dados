#!/usr/bin/env python
# coding: utf-8

# # Rascunho das atividades de aula (26/03/2024)

# In[1]:


import numpy as np


# In[2]:


def transp(mat):
    """
    mat = [[2, 3], [4, 5], [6, 7]]

    [[2, 3],
     [4, 5]
     [6, 7]]

     mat_transposta:
     [[2, 4, 6],
      [3, 5, 7]]
    """
    nl = len(mat)  # linhas na matriz mat
    nc = len(mat[0])  # colunas em mat
    tr = []
    for j in range(nc):
        linha = []
        for i in range(nl):
            linha.append(mat[i][j])
        tr.append(linha)
    return tr


# In[3]:


mat = [[2, 3], [4, 5], [6, 7]]
transp(mat)


# In[4]:


def mult_mat(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Dimensoes incompativeis")

    nl = len(A)  # linhas do resultado
    nc = len(B[0])  # colunas do resultado

    resultado = [[ 0 for _ in range(nc)]
                     for _ in range(nl)]

    for i in range(nl):
        for j in range(nc):
            for k in range(len(B)):
                resultado[i][j] += A[i][k]*B[k][j]
                
    return resultado


# In[5]:


A = [[1,2,3], [4,5,6]]  # 2x3
B = [[7,8,9], [10,11,12],[13,14,15]]  # 3x3
mult_mat(A, B)  # 2x3


# In[6]:


B = [[7,8,9], [10,11,12],[13,14,15]]  # 3x3
I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # 3x3
mult_mat(I, B)


# In[7]:


import math
PI = 3.1416  # 180 graus
math.cos(PI/4)


# In[8]:


from math import pi
pi


# In[9]:


import numpy as np
arr  = np.array([1,2.0,3])
arr.dtype


# In[10]:


arr1 = np.array([1,2])
arr2 = np.array([3,4])
arr3 = np.vstack((arr1,arr2))
print(arr3)


# In[11]:


arr3[0,0] = -1
print(arr3)
print(arr1)


# In[ ]:





# In[12]:


print(arr1)
arr4 = arr1
arr4[0] = -1
print(arr4)


# In[13]:


print(-1*arr4)


# In[ ]:




