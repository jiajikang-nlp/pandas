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


# In[2]:


# 0 读取数据
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
# 替换掉温度的后缀℃
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')


# In[3]:


df.head()


# In[4]:


# 1、Series的排序
# 对aqi排序
df['aqi'].sort_values()


# In[5]:


df['aqi'].sort_values(ascending=False) # 降序


# In[6]:


df['tianqi'].sort_values() # 对中文的排序


# In[7]:


# 2、dataframe的排序
# 2.1 单列排序
df.sort_values(by='aqi')


# In[8]:


df.sort_values(by='aqi',ascending=False) # 降序


# In[9]:


# 2.2 多列排序
# 按照空气质量等级，最高温度排序，默认升序
df.sort_values(by=['aqiLevel','bWendu'])


# In[10]:


# 两个字段都是降序
df.sort_values(by=['aqiLevel','bWendu'],ascending=False)


# In[11]:


# 分别指定升序和降序
df.sort_values(by=['aqiLevel','bWendu'],ascending=[True,False])


# In[ ]:




