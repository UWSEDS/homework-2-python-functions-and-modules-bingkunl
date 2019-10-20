#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def create_dataframe(url):
    data = pd.read_csv(url)
    return data

def test_create_dataframe(data, names):
    for name in data:
        l = len(data[name])
        if name not in names:
            return False
        if l < 10:
            return False
        for i in range(l-1):
            t1 = type(data[name][i])
            t2 = type(data[name][i+1])
            if t1 != t2:
                return False
    return True


# In[ ]:




