#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
 author:jjk
 datetime:2020/02/06
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


# 问题：怎样统计每周，每月，每季度的最高温度？
# 1、读取天气到dataframe
fpath = './datas/beijing_tianqi/beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)
# 替换掉温度后缀
df.loc[:, 'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:, 'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
df.head()


# In[5]:


# 2、将日期列表转换成pandas的日期
# pd.to_datetime(df['ymd'])变成一个日期对象的一个序列
df.set_index(pd.to_datetime(df['ymd']),inplace=True) # 设置索引,True:表示不会生成默认索引
df.head()


# In[6]:


df.index # 日期已经成为索引


# In[7]:


# DatatimeIndex是Timestamp的列表形式
df.index[0]


# In[8]:


# 3、方便的对DatetimeIndex进行查询
# 筛选固定的某一天
df.loc['2018-01-05']


# In[10]:


# 日期区间
df.loc['2018-01-05' : '2018-01-10']


# In[11]:


# 按月份前缀筛选
df.loc['2018-03'].head()


# In[12]:


# 按照月份前缀筛选
df.loc['2018-07' : '2018-09'].index


# In[13]:


# 按照年份前缀筛选
df.loc['2018'].head()


# In[14]:


# 4、方便的获取周，月，季度
# Timestamp，DatetimeIndex支持大量的属性可以获取日期分量


# In[15]:


# 周数字列表
# 月数字列表
# 季度数字列表


# In[30]:


# 周数字列表
df.index.week


# In[17]:


# 月数字列表
df.index.month


# In[18]:


# 季度数字列表
df.index.quarter


# In[19]:


# 5、统计每周、每月、每季度的最高温度


# In[23]:


# 统计每周的数据
df.groupby(df.index.week)['bWendu'].max().head()


# In[32]:


df.groupby(df.index.week)['bWendu'].max().plot()


# In[25]:


# 统计每月的数据
df.groupby(df.index.month)['bWendu'].max().head()


# In[26]:


df.groupby(df.index.month)['bWendu'].max().plot()


# In[27]:


# 统计每个季度的数据
df.groupby(df.index.quarter)['bWendu'].max()


# In[28]:


df.groupby(df.index.quarter)['bWendu'].max().plot()


# In[ ]:


#

