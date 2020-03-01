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


'''
1.经过统计得到多维度指标数据
  非常场景的统计场景，指定多个维度，计算聚合后的指标
  实例：统计得到电影评分数据集”，每个月份的每个分数被评分多少次：（月份、分数1~5、次数）

'''


# In[5]:


df = pd.read_csv(
    './datas/movielens-1m/ratings.dat',
    sep ='::', # 分隔符
    engine = 'python',
    header = None,
    names = 'UserID::MovieID::Rating::Timestamp'.split('::')
)
df.head()


# In[6]:


df['pdata'] = pd.to_datetime(df['Timestamp'],unit='s') # 秒，日期处理
df.head() # pdata这一列已经格式化成日期的格式


# In[7]:


df.dtypes


# In[8]:


# 实现数据统计
# 两个列：df['pdata'].dt.month和'Rating'
# 挑选出['UserID']这一列进行聚合方法：.agg(pv=np.sum)，pv：为一个新的列
df_group = df.groupby([df['pdata'].dt.month,'Rating'])['UserID'].agg(pv=np.sum)
df_group.head(20) # pdata：月份，每个月份中：5个评分的数据，对于的评分的次数


# In[9]:


# 对这样格式的数据，我想查看按月份，不同评分的次数趋势，是没法实现的
# 需要将数据变换成每个评分是一列才可以实现


# In[10]:


# 2、使用unstack实现数据二维透视
# 目的：想要画图对比按照月份的不同评分的数据趋势
df_stack = df_group.unstack()
df_stack


# In[11]:


df_stack.plot()


# In[12]:


# unstack和stack是互逆操作
df_stack.stack().head(20)


# In[13]:


# 3. 使用pivot简化透视
df_group.head(20)


# In[14]:


df_reset = df_group.reset_index() # 重置索引，默认的数字索引，月份，评分，次数
df_reset.head()


# In[18]:


df_pivot = df_reset.pivot('pdata','Rating','pv')
df_pivot.head()


# In[19]:


df_pivot.plot()


# In[20]:


# pivot方法相当于对df使用set_index创建分层索引，然后调用unstack


# In[ ]:


# 4. stack、unstack、pivot的语法
# stack:DataFrame.stack(level=-1,dropna=True),将column变成index，类似把横放的书籍变成竖放
# level=-1代表多层索引的最内层，可以通过==0,1,2指定多层索引的对应层
# unstack:DataFrame.unstack(level=-1,fill_value=None),将index变成column，类似把竖放的书籍变成横放
# pivot：DataFrame.pivot(index=None,columns=None,value=None),指定index，columns，values实现二维透视

