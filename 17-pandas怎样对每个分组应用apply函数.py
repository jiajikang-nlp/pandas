#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


ratings = pd.read_csv(
    './datas/movielens-1m/ratings.dat',
    sep='::',
    engine = 'python',
    names = 'UserID::MovieID::Rating::Timestamp'.split('::')
)
ratings.head()


# In[8]:


# 实现按照用户ID分组，然后对其中一列归一化
def ratings_norm(df):
    '''
    @param df:每个用户分组的dataframe
    '''
    min_value = df['Rating'].min()
    max_value = df['Rating'].max()
    df['Rating_norm'] = df['Rating'].apply(lambda x : (x-min_value)/(max_value-min_value)) # 新增一个列：Rating_norm，做归一化
    return df
# 按照UserID进行分组，然后对这个分组对象进行一个apply函数， 传给这个函数的参数是每个用户分组的df
ratings = ratings.groupby('UserID').apply(ratings_norm)


# In[9]:


ratings[ratings['UserID']==1].head()


# In[13]:


# 可以看到UserID==1这个用户，Rating==3是她的最低分，是个乐观派，我们归一化0分;5->1.0
# 实例2：怎样取每个分组的TOPN数据
# 获取2018年每个月温度最高的2天数据
fpath = './datas/beijing_tianqi/beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)
# 替换掉温度后缀
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
# 新增一列为月份
df['month'] = df['ymd'].str[:7]
df.head()


# In[15]:


def getWenduTopn(df,topn):
    '''
    这里的df是每个月分组group的df
    '''
    # df.sort_values(by='bWendu'): 排序
    # ['ymd','bWendu']：取两列，日期和最高温度
    # sort_values在默认情况下是升序排序的，-topn
    return df.sort_values(by='bWendu')[['ymd','bWendu']][-topn:] 

df.groupby('month').apply(getWenduTopn,topn=2).head()


# In[ ]:


# 我们可以看到，grouby的apply函数返回的dataframe，其实和原来的dataframe其实可以完全不一样

