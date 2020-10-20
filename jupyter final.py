#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

def Rule1(c,errA):
    errQ = (abs(c)*errA)
    return errQ
    
c = 5
errA = .03

errQ = Rule1(c,errA)

print("errQ =", errQ)
    


# In[10]:


def Rule2(c,m,A,errA):
    errQ = abs(c*m*A**(m-1))*errA
    return errQ

c = 1
m = 2
A = 3
errA = .15

errQ = Rule2(c,m,A,errA)

print("errQ =", errQ)


# In[12]:


def Rule3(errA, errB):
    errQ = np.sqrt(errA**2+errB**2)
    return errQ

errA = .5
errB = .1

errQ = Rule3(errA, errB)

print("errQ =", errQ)


# In[13]:


def Rule4_2(Q,A,m,errA,B,n,errB):
    errQ = Q*np.sqrt((m*errA/A)**2+(n*errB/B)**2)
    return errQ

Q = 1

A = 1
m = 1
errA = 1

B = 1
n = 1
errB = 1

errQ = Rule4_2(Q,A,m,errA,B,n,errB)

print('errQ =', errQ)


# In[15]:


def Rule4_3(Q,A,m,errA,B,n,errB,C,o,errC):
    errQ = Q*np.sqrt((m*errA/A)**2+(n*errB/B)**2+(o*errC/C)**2)
    return errQ

Q = 1

A = 1
m = 1
errA = 1

B = 1
n = 1
errB = 1

C = 1
o = 1
errC = 1

errQ = Rule4_3(Q,A,m,errA,B,n,errB,C,o,errC)

print('errQ =', errQ)


# In[ ]:




