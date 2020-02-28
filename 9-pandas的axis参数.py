#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
 author:jjk
 datetime:2020/01/31
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import numpy as np


# In[2]:


df = pd.DataFrame(
    np.arange(12).reshape(3,4),
    columns=['A','B','C','D'] # 每列的名称
)


# In[3]:


df


# In[4]:


# 1、单列drop，就是删除某一列
df.drop('A',axis=1) # 输出a这一列


# In[5]:


# 2、单行drop，就是删除某一行
df.drop(1,axis=0)


# In[6]:


# 3、按axis=0/index执行mean聚类操作
# 反直觉：输出的不是每行的结果，而是每列的结果
df


# In[7]:


# axis=0, or axis = index
df.mean(axis=0) # 按哪个axis，就是这个axis要动起来（类似被for遍历，其它的axis保持不动,所以，四列不动


# In[8]:


df


# In[9]:


df.mean(axis=1) # 三行的平均数据，跨列输出行结果


# In[10]:


# 5、再次举例，加深理解
def get_sum_value(x):
    return x['A'] + x['B'] + x['C'] + x['D']
df['sum_value'] = df.apply(get_sum_value,axis=1) # 跨列输出行结果


# In[11]:


df


# In[ ]:




