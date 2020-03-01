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
# 1. map用于Series值的转换
# 实例：将古朴代买英文转换成中文名字
# Series.map(dict) or Series.map(function)均可
stocks = pd.read_excel('./datas/stocks/互联网公司股票.xlsx')
stocks.head()


# In[2]:


stocks['公司'].unique()


# In[5]:


# 公司股票代码到中文的映射，注意这里是小写
dict_company_names = {
    'bidu':'百度',
    'baba':'阿里巴巴',
    'iq':'爱奇艺',
    'jd':'京东'
}


# In[6]:


# 方法1：Series.map(dict)
stocks['公司中文'] = stocks['公司'].str.lower().map(dict_company_names)
stocks.head()


# In[8]:


# 方法2：Series.map(function)
# function的参数是Series的每个元组的值
stocks['公司中文2'] = stocks['公司'].map(lambda x : dict_company_names[x.lower()])
stocks.head()


# In[9]:


# 2、apply用于Series和DataFrame的转换
# Series.apply(function),函数的参数为每个值
# DataFrame.apply(function),函数的参数是Series


# In[10]:


# Series.apply(function),函数的参数为每个值
stocks['公司中文3'] = stocks['公司'].apply(lambda x : dict_company_names[x.lower()])
stocks.head()


# In[14]:


# DataFrame.apply(function),函数的参数是Series
# stocks.apply的stocks是一个dataframe，
# 扫描是跨列的
stocks['公司名称4'] = stocks.apply(
    lambda x : dict_company_names[x['公司'].lower()],
    axis=1)
stocks.head()


# In[16]:


# 注意这个代码：
#1. apply是在stocks这个dataframe上调用
#2. lambda x的x是一个series，因为指定了axis=1，所以series的key是列名，可以用x['公司']获取


# In[18]:


# 3、applymap用于dataframe所有值的转换
sub_df = stocks[['收盘','开盘','高','低','交易量']]
sub_df.head()


# In[19]:


# 将整个数字取整数，应用于所有元素
sub_df.applymap(lambda x : int(x))


# In[20]:


# 直接修改原df的这几列
stocks.loc[:,['收盘','开盘','高','低','交易量']] = sub_df.applymap(lambda x : int(x))
stocks.head()


# In[ ]:




