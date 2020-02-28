#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
 author:jjk
 datetime:2020/01/31
 coding:utf-8
 project name:test/pandas
 Program function: Pandas的SettingWithCopyWarning
"""
import pandas as pd


# In[2]:


# 0 读取数据
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)
df.head()


# In[3]:


# 替换掉温度的后缀℃
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')


# In[4]:


df.head()


# In[10]:


# 1、复现
# 只选出3月份的数据用于分析
condition = df['ymd'].str.startswith('2018-03')


# In[6]:


# 设置温度差
df[condition]['wen_cha'] = df['bWendu']-df['yWendu']
"""
发出警告的代码：df[condition]['wen_cha'] = df['bWendu']-df['yWendu'] 相当于：df.get(condition).set(wen_cha),第一步的get发出的警告
链式操作其实是两个步骤，先get后set，get得到的dataframe可能是view也可能是copy，pandas发出警告
核心要诀：pandas的dataframe的修改写操作，只允许在源dataframe上进行，一步到位。

"""


# In[7]:


# 查看是否修改成功
df[condition].head()


# In[8]:


# 3、 解决方法1
# 将get+Set的两步操作，改成set的一步操作
df.loc[condition,'wen_cha'] = df['bWendu'] - df['yWendu']
df[condition].head()


# In[11]:


# 4、 解决方法2
# 如果需要预筛选做后续的处理分析，使用copy复制dataframe
df_moth3 = df[condition].head()


# In[12]:


df_moth3.head()


# In[13]:


df_moth3['wen_cha'] = df['bWendu'] - df['yWendu']
df_moth3.head()


# In[ ]:


# 总之，padas不允许先筛选字dataframe，再进行修改写入
# 要么使用.loc实现一个步骤直接修改源dataframe
# 要么先复制一个子dataframe再进行一个步骤执行修改

