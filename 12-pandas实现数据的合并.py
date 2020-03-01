#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
 author:jjk
 datetime:2020/02/04
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df1 = pd.DataFrame({
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3'],
    'C':['C0','C1','C2','C3'],
    'D':['D0','D1','D2','D3'],
    'E':['E0','E1','E2','E3'],
})

df2 = pd.DataFrame({
    'A':['A4','A5','A6','A7'],
    'B':['B4','B5','B6','B7'],
    'C':['C4','C5','C6','C7'],
    'D':['D4','D5','D6','D7'],
    'F':['F4','F5','F6','F7'],
})


# In[3]:


df1


# In[4]:


df2


# In[5]:


# 一、使用pandas.concat合并数据
# 1、默认的 concat，参数为axis=0、join=outer、 ignore_index=False
pd.concat([df1,df2])


# In[6]:


# 2、使用 ignore_index=true可以忽略原来的索引
pd.concat([df1,df2],ignore_index=True)


# In[7]:


# 3、使用join=inner过滤掉不匹配的列
pd.concat([df1,df2],ignore_index=True,join='inner')


# In[8]:


# 4、使用axis=1相当于添加新列
df1


# In[9]:


# A 添加一列Series
s1 = pd.Series(list(range(4)),name='F')
pd.concat([df1,s1],axis=1)


# In[10]:


#B 添加多列Series
s2 = df1.apply(lambda x:x['A']+'_GG',axis=1)
s2


# In[11]:


s2.name = 'G'
pd.concat([df1,s1,s2],axis=1)


# In[12]:


# 列表可以只有Series
pd.concat([s1,s2],axis=1)


# In[13]:


# 列表是可以混合顺序的
pd.concat([s1,df1,s2],axis=1)


# In[23]:


# 二、使用dataframe.append按行合并数据
df1 = pd.DataFrame([[1,2],[3,4]],columns=list('AB'))
df2 = pd.DataFrame([[5,6],[7,8]],columns=list('AB'))
df1


# In[24]:


df2


# In[16]:


# 1、给1个dataframe添加另一个dataframe
df1.append(df2)


# In[17]:


#2、忽略原来的索引 ignore_ index=true
df1.append(df2,ignore_index=True)


# In[18]:


# 3、可以一行一行的给 Data Frame添加数据
# 一个空的df
df = pd.DataFrame(columns=['A'])
df


# In[19]:


# A:低性能的版本
for i in range(5):
    # 注意这里每次都在复制
    df = df.append({'A':i},ignore_index=True)
df


# In[21]:


# B:性能好的版本
# 第一个入参是一个列表，避免了多次复制
pd.concat(
    [pd.DataFrame([i],columns=['A']) for i in range(5)],
    ignore_index=True) # 将这5个参数一起传给列表第一个参数


# In[ ]:




