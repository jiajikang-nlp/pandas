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
df =pd.read_csv('./datas/ml-latest-small/ratings.csv')
df.head() # 会自动生成索引


# In[3]:


df.count()# 统计每列的个数


# In[4]:


# 1、使用index查询数据
# drop=False，让索引列还保持在column
df.set_index('userId',inplace=True,drop=False)
df.head()


# In[5]:


df.index


# In[6]:


# 使用index的查询方法
df.loc[500].head(5)


# In[7]:


# 使用column的condition查询方法
df.loc[df['userId']==500].head()


# In[9]:


# 2. 使用index会提升查询性能
"""
·如果 index是唯一的， Pandas会使用哈希表优化，查询性能为O(1)
·如果 index不是唯一的，但是有序， Pandas会使用二分查找算法，查询性能为O(logN)
·如果 index是完全随机的，那么每次查询都要扫描全表，查询性能为O(N)

"""
# 实验1：
# 将数据随机打散
from sklearn.utils import shuffle
df_shffle = shuffle(df) # 将df随机打散
df_shffle.head()


# In[10]:


# 索引是否是递增
df_shffle.index.is_monotonic_increasing # 是否单调递增


# In[11]:


df_shffle.index.is_unique # 如果是的话，会哈希查询


# In[12]:


# 计时，查询id=500数据性能
get_ipython().run_line_magic('timeit', 'df_shffle.loc[500]')


# In[13]:


# 实验2：将index排序后的查询
df_sorted = df_shffle.sort_index() # 排序
df_sorted.head()


# In[14]:


# 索引是否递增的
df_sorted.index.is_monotonic_increasing


# In[15]:


df_sorted.index.is_unique


# In[16]:


get_ipython().run_line_magic('timeit', 'df_sorted.loc[500]')


# In[17]:


# 3 使用index能自动对齐数据
s1 = pd.Series([1,2,3],index=list('abc'))
s1


# In[18]:


s2 = pd.Series([2,3,4],index=list('bcd'))
s2


# In[19]:


s1+s2


# In[ ]:


'''
4.使用index更多更强大的数据结构支持
很多强大的索引数据结构
Categoricallndex，基于分类数据的Index，提升性能；
Multilndex，多维索引，用于groupby多维聚合后结果等；
Datetimelndex，时间类型索引，强大的日期和时间的方法支持；

'''

