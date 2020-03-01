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
# 加上这一句，能在jupyter notebook展示matplot图表
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.DataFrame({'A': ['foo','bar','foo','bar','foo','bar','foo','foo'],
                  'B':['one','one','two','three','two','two','one','three'],
                  'C':np.random.randn(8),
                  'D':np.random.randn(8)})
df


# In[3]:


#一、分组使用聚合函数做数据统计
# 1、单个列 groupby，查询所有数据列的统计
df.groupby('A').sum() # 对A列分组，然后做统计 


# In[4]:


# 2、多个groupby，查询所有数据列的统计
df.groupby(['A','B']).sum()


# In[5]:


# 我们看到：('A','B')成对编程了二级索引
df.groupby(['A','B'],as_index=False).mean() # c，d列平均值，A,B变成普通的列


# In[6]:


# 3、同时查看多种数据统计
df.groupby('A').agg([np.sum,np.mean,np.std])


# In[8]:


# 4、查看单列的结果数据统计
# 方法1：预过滤，性能更好
df.groupby('A')['C'].agg([np.sum,np.mean,np.std])


# In[9]:


# 方法2：
df.groupby('A').agg([np.sum,np.mean,np.std])['C']


# In[11]:


# 5、不同列使用不同的聚类函数
df.groupby('A').agg({'C':np.sum,'D':np.mean})


# In[12]:


# 二、遍历groupby的结果理解执行流程
#for循环可以直接遍历每个group
#1、遍历单个列聚合的分组
g = df.groupby('A')
g


# In[13]:


for name,group in g:
    print(name)
    print(group)
    print()


# In[18]:


# 可以获取单个分组的数据
g.get_group('bar')


# In[20]:


# 2、遍历多个列聚合的分组
g = df.groupby(['A','B'])
for name,group in g:
    print(name)
    print(group)
    print()


# In[23]:


# 可以看到，name是一个2个元组的tuple，代表不同的列
g.get_group(('foo','two')) # 获取某个具体的分组


# In[24]:


# 可以直接查询group后的某几列，生成Series或者子DataFrame
g['C']


# In[25]:


for name,group in g['C']:
    print(name)
    print(group)
    print(type(group))
    print()


# In[28]:


# 其实所有的聚合统计，都是在dataframe和Series上进行的
# 三、实例分组探索天气数据
fpath = './datas/beijing_tianqi/beijing_tianqi_2018.csv'
df = pd.read_csv(fpath)
# 替换掉温度的后缀
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32')
df.head()


# In[37]:


# 新增一列为月份
df['month'] = df['ymd'].str[:7] # 等于年月日这一列的str形式的前7位
df.head()


# In[30]:


# 1、查看每个月的最高温度
data = df.groupby('month')['bWendu'].max()
data


# In[31]:


type(data)


# In[32]:


data.plot()


# In[33]:


#2。查看每个月的最高温度，最低温度，平均空气质量指数
df.head()


# In[34]:


group_data = df.groupby('month').agg({'bWendu':np.max, 'yWendu':np.min, 'aqi':np.mean})
group_data


# In[35]:


group_data.plot()


# In[ ]:




