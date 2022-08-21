#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle


# In[2]:


# l = [[84, 115, 15, 96, 96, 19, 10, 64], [0, 70, 28, 26, 42, 39, 120, 12], [0, 0, 43, 0, 6, 31, 21, 94], [0, 0, 0, 12, 118, 51, 101, 28], [0, 0, 0, 0, 112, 111, 31, 20], [0, 0, 0, 0, 0, 11, 82, 72], [0, 0, 0, 0, 0, 0, 27, 11], [0, 0, 0, 0, 0, 0, 0, 38]]
# r = [19, 117, 40, 75, 86, 44, 21, 14]
with open('At_matrix.pkl','rb') as file:
    l = pickle.load(file)
    file.close()
with open('Exp_vector.pkl','rb') as file:
    r = pickle.load(file)
    file.close()
A_t=[]
m = len(l) 
n = len(l[0])
 
for i in range(n):
    temp = []
    for j in range(m):
        temp.append(l[j][i])
    A_t.append(temp)


# In[3]:


A_t


# In[4]:



from pyfinite import ffield
b_size = 8
ff = ffield.FField(7, gen=0x83, useLUT=-1)
A_t = np.array(A_t)
exp = []
for i in range(0,128):
    lis = [1]
    exp.append(lis)
for i in range(0,128):
    for j in range(0,126):
        t = exp[i][j]
        result = ff.Multiply(t,i)
        exp[i].append(result)
inv = []
for i in range(128):
    lis = []
    for j in range(128):
        lis.append(0)
    inv.append(lis)
inv = np.array(inv) 
for i in range(0,128):
    for j in range(1,127):
        k = exp[i][j]
        inv[j][k] = i
        
inverse = []
inverse.append(1)
for i in range(1, 128):
    inverse.append([ff.Inverse(i)])
aug = []
for i in range(8):
    lis = []
    for j in range(16):
        lis.append(0)
    aug.append(lis)
aug = np.array(aug) 
   

for i in range(0,8):
    for j in range(0,8):
        aug[i][j] = A_t[i][j]
    aug[i][i+8] = 1


for j in range(0,8):
    for i in range(j,8):
        if(aug[i,j] != 0):
            p = i
            break
    aug[[j, p]] = aug[[p, j]]

    fac = inverse[aug[j][j]]
    fac = fac[0]
    for m in range(16):
        
        aug[j][m] = ff.Multiply(aug[j][m],fac)
    for i in range(0,8):
        if i!=j and aug[i][j] != 0:
            fac = aug[i][j]
          
            for k in range(16):
                temp = ff.Multiply(aug[j][k], fac)
                aug[i][k] = ff.Add(temp, aug[i][k])
inv_a = []
for i in range(8):
    lis = []
    for j in range(8):
        lis.append(0)
    inv_a.append(lis)
inv_a = np.array(inv_a) 

for i in range(0,8):
    for j in range(0,8):
        inv_a[i][j] = aug[i][8+j]
print("A inverse matrix: \n{}".format(inv_a))


# In[5]:


password = "gsiiiplhgsjpltljiujnkglrkilqguig" 
decrypted_password = ''
b_size = 16
for i in range(2): 
    elements = ''
    for j in range(16*i,16*(i+1)):
         elements = elements +  password[j]
    block = []
    for j in range(0,8):
        block.append([(ord(elements[2*j]) - ord('f'))*16 + (ord(elements[2*j+1]) - ord('f'))])
        
   
    
    lis = []
    for k in range(8):
        
        lis.append(inv[r[k]][block[k]][0])
    liss = []
    
    for m in range(8):
        summ =0
        for n in range(8):
            s = ff.Multiply(inv_a[m][n], lis[n])
            summ = ff.Add(s,summ)
        liss.append(summ)
    lis = []
    for k in range(8):
        lis.append(inv[r[k]][liss[k]])
    
    liss = []
    for m in range(8):
        summ =0
        for n in range(8):
            s = ff.Multiply(inv_a[m][n], lis[n])
            summ = ff.Add(s,summ)
        liss.append(summ)
    lis = []
    for k in range(8):
        lis.append(inv[r[k]][liss[k]])
    
    for c in lis:
        decrypted_password =   decrypted_password + chr(c)
print("The password is",decrypted_password)
    


# In[6]:


print("After removing zeros :",end = "")
print(decrypted_password[:10])


# In[ ]:




