#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
 author:jjk
 datetime:2020/01/31
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import numpy as np


# In[6]:


# 一、Series
# 仅有数据列表即可产生最简单的Series
s1 = pd.Series([1,'a',5.2,7])
# 左侧为索引，右侧为数据
print(s1)
# 获取索引
print(s1.index)
# 获取数据
print(s1.values)


# In[8]:


# 3.1.2 创建一个具有标签索引的Series
s2 = pd.Series([1,'a',3.4,6,],index=['a','b','c','d'])
print(s2)
print(s2.index)


# In[9]:


# 3.1.3 使用python字典创建Series
sdata = {'o1':3434, '02':3434,'03':'5656'}
s3 = pd.Series(sdata)
print(s3)


# In[14]:


# 3.2.1 根据多个字典序列创建dataframe
data = {
    'state': ['1','2','3','4','5'],
    'year':[232,343,343,343,545],
    'pop':[1,2,3,4,5]
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print(df.columns) # 行
print(df.index) # 列


# In[15]:


df


# In[16]:


df['year']


# In[17]:


type(df['year']) # 查询一列


# In[23]:


df.loc[3] # 查询一行


# In[24]:


type(df.loc[3])


# In[18]:


df[['year','pop']]


# In[19]:


type(df[['year','pop']]) # 查询多行


# In[25]:


df.loc[1:3]


# In[26]:


type(df.loc[1:3]) # 查询多行


# In[ ]:




