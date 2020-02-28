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

"""
pandas数据统计函数

1、汇总类统计

2、唯一去重和按值计数

3、相关系数和协方差

"""
# 0 读取数据
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)


# In[2]:


df.head()


# In[3]:


# 先简单的一个处理
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')


# In[4]:


df.head()


# In[6]:


# 1 汇总类统计
# 一下子提取所有的数字列统计结果
df.describe()


# In[7]:


# 查看单个Series的数据
df['bWendu'].mean()


# In[8]:


# 最高温
df['bWendu'].max()


# In[9]:


# 最低温
df['bWendu'].min()


# In[12]:


# 6.2 唯一去重和按值计数
# 唯一性去重
# 一般不用于数值列，而是枚举，分类列
df.head()


# In[13]:


df['fengxiang'].unique()


# In[14]:


df['tianqi'].unique()


# In[15]:


df['fengli'].unique()


# In[16]:


# 按值计数
df['fengxiang'].value_counts()


# In[17]:


df['tianqi'].value_counts()


# In[18]:


df['fengli'].value_counts()


# In[19]:


# 6.3 相关系数和协方差
# 协方差矩阵：
df.cov()


# In[20]:


# 相关系数矩阵
df.corr()


# In[22]:


# 单独查看空气质量和最高温度的相关系数
df['aqi'].corr(df['bWendu']) # 二者关系不大


# In[23]:


# 空气质量和温差的相关系数
df['aqi'].corr(df['bWendu']-df['yWendu'])


# In[ ]:


# 

