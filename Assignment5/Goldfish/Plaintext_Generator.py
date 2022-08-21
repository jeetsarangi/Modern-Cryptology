#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


mapping = {
 '0000': 'f',
 '0001': 'g',
 '0010': 'h',
 '0011': 'i',
 '0100': 'j',
 '0101': 'k',
 '0110': 'l',
 '0111': 'm',
 '1000': 'n',
 '1001': 'o',
 '1010': 'p',
 '1011': 'q',
 '1100': 'r',
 '1101': 's',
 '1110': 't',
 '1111': 'u'}


# In[3]:


def create_input(name,mapping):
    output = open(name+".txt","w+")
    
    
    for i in range(8):
        
        for j in range(128):
            
            number_string = bin(j)[2:].zfill(8)
            
            temp_plain = 'ff'*i + mapping[number_string[:4]] + mapping[number_string[4:]] + 'ff'*(7-i)
            
            output.write(temp_plain + " ")
        output.write("\n")
        
        
    output.close()


# In[4]:


create_input("plaintexts",mapping)

