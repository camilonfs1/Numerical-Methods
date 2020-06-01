#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy


# In[4]:


def gaussJordan(matriz, vector):

    matrix = numpy.array(matriz, dtype=numpy.float64)
    vector = numpy.array(vector, dtype=numpy.float64)

    m = len(vector)
    x = numpy.zeros(m)    

    for k in range(0, m):
        for r in range(k+1, m):
            factor=(matrix[r,k]/matrix[k,k])
            vector[r]=vector[r]-(factor*vector[k])
            for c in range(0,m):
                matrix[r,c]=matrix[r,c]-(factor*matrix[k,c])

    x[m-1]=vector[m-1]/matrix[m-1, m-1]

    for r in range(m-2, -1, -1):
        suma = 0
        for c in range(0,m):
            suma=suma+matrix[r,c]*x[c]
        x[r]=(vector[r]-suma)/matrix[r, r]  
    return x


# In[20]:


print(gaussJordan([[1,2],[10**-20,1]],[12,1]))

