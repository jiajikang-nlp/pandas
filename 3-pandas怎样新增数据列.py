#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
 author:jjk
 datetime:2020/01/31
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
"""
1 直接赋值
2 df.apply方法
3 df.assign方法
4 按条件选择分组分别赋值
"""
# 0 读取csv数据到dataframe
fpath1 = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath1)
print(df.head())


# In[8]:


# 1 直接赋值的方法
# 实例：清理到温度列，变成数字列
df.loc[:,'bWendu'] = df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu'] = df['yWendu'].str.replace('℃','').astype('int32') 


# In[11]:


df.head()


# In[10]:


# 实例：计算温差
# 注意：df['bWendu']其实一个Series，后面的减法返回的是Series
df.loc[:,'wencha'] = df['bWendu'] - df['yWendu']
print(df.head())


# In[12]:


df.head()


# In[16]:


#5.2 df.apply方法
def get_wendu_type(x):
    if x['bWendu'] >33:
        return '高温'
    if x['yWendu'] <-10:
        return '低温'
    return '常温'
# 注意需要设置axis==1,这个series的index是columns
df.loc[:,'wendu_type'] = df.apply(get_wendu_type,axis=1)


# In[18]:


# 查看温度类型的计数
df['wendu_type'].value_counts() 


# In[19]:


# 5.3 df.assign方法
# 实例，将温度从摄氏度变为华氏度
# 可以同时添加多个新的列
df.assign(
    yWendu_huashi = lambda x : x['yWendu'] * 9 /5 +32, # yWendu_huashi:新增加的列
    # 摄氏度转华氏度
    bWendu_huashi = lambda x : x['bWendu'] * 9 /5 +32
)


# In[20]:


# 5.4 按条件选择分组分别赋值
# 先创建实例（这是第一种创建新列的方法）
df['wencha_type'] = ''
df.loc[df['bWendu'] - df['yWendu']>10, 'wencha_type'] = '温差大'
df.loc[df['bWendu'] - df['yWendu']<=10, 'wencha_type'] = '温差正常'


# In[21]:


df['wencha_type'].value_counts()


# In[ ]:




