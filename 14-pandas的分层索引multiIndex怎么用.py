#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
 author:jjk
 datetime:2020/02/05
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


stocks = pd.read_excel('./datas/stocks/互联网公司股票.xlsx')
stocks.shape


# In[3]:


stocks.head()


# In[4]:


stocks['公司'].unique() # 统计多少个公司数据


# In[5]:


stocks.index


# In[6]:


stocks.groupby('公司')['收盘'].mean()


# In[7]:


# 一、Series的分层索引Multilndex
ser = stocks.groupby(['公司','日期'])['收盘'].mean()
ser


# In[8]:


# 多维索引，空白的意思是：使用上面的值
ser.index


# In[9]:


# unstack把二级索引变成列
ser.unstack()


# In[10]:


ser


# In[11]:


ser.reset_index() # 将多级索引，变成普通的列


# In[12]:


# 二、 Series有多层索引Multilndex怎样筛选数据？
ser


# In[13]:


ser.loc['BIDU'] # 直接写第一级索引


# In[14]:


# 多层索引，可以用元组的形式筛选
ser.loc[('BIDU','2019-10-02')]


# In[15]:


ser.loc[:,'2019-10-02'] # 第一级：冒号，


# In[20]:


# 三、DataFrame的多层索引Multilndex
stocks.head()


# In[22]:


stocks.set_index(['公司','日期'], inplace=True) # 设置索引


# In[23]:


stocks.index


# In[24]:


stocks.sort_index(inplace=True) # 一级，二级排序,按照字母的顺序
stocks


# In[25]:


# 四、 DataFrameMultiIndex有多层索引怎样筛选数据？
#【重要知识】在选择数据时：
#元组（key1.key2）代表筛选多层索引，其中key1是索引第一级，key2是第二级，比如key1=JD,key2=2019-10-02
#列表[Key1,key2]代表同一层的多个KEY，其中key1和key2是并列的同级索引，比如key=JD,key2=BIDU
stocks.loc['BIDU']
stocks.loc[('BIDU','2019-10-02'),:]


# In[ ]:





# In[26]:


stocks.loc[('BIDU','2019-10-02'),'开盘']


# In[27]:


stocks.loc[['BIDU','JD'],:] # 并列筛选


# In[28]:


stocks.loc[(['BIDU','JD'],'2019-10-03'),:]


# In[29]:


stocks.loc[(['BIDU','JD'],'2019-10-03'),'收盘']


# In[30]:


stocks.loc[('BIDU', ['2019-10-02','2019-10-03']),'收盘']


# In[31]:


# slice(None)代表这一索引的所有内容
stocks.loc[(slice(None),['2019-10-02','2019-10-03']),:] # 筛选出所有公司的两天的数据


# In[32]:


stocks.reset_index()# 将多级索引，变成普通的列


# In[ ]:




