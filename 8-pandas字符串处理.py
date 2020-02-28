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


# 0 读取数据：北京2018年天气数据
fpath = "./datas/beijing_tianqi/beijing_tianqi_2018.csv"
df = pd.read_csv(fpath)


# In[3]:


df.head()


# In[6]:


df.dtypes


# In[7]:


# 1、获取Series的str属性，使用各种字符串处理函数
df['bWendu'].str


# In[8]:


# 字符串替换函数
df['bWendu'].str.isnumeric()


# In[9]:


df['aqi'].str.len() # 会报错只能在，string下运行str


# In[10]:


# 2、使用str的startswith，contains等得到bool的Series可以做条件查询
condition = df['ymd'].str.startswith('2018-03')


# In[11]:


condition


# In[13]:


df[condition].head() # 只输出三月份的数据


# In[14]:


# 3、需要多次str处理的链式操作
# 怎样获取201803这样的数字月份
# 1、先将日期2018-03-31替换成20180331的形式
# 2、提取月份字符串201803
df['ymd'].str.replace('-','')


# In[15]:


# 每次调用函数，都返回一个新Series
df['ymd'].str.replace('-','').splice(0,6)


# In[17]:


df['ymd'].str.replace('-','').str.slice(0,6)


# In[18]:


# slice就是切片语法，可以直接用
df['ymd'].str.replace('-','').str[0:6]


# In[19]:


# 4、使用正则表达式的处理
# 添加新列
def get_nianyueri(x):
    year,month,day = x['ymd'].split('-')
    return f'{year}年{month}月{day}日'
df['中文日期'] = df.apply(get_nianyueri,axis=1)


# In[20]:


df['中文日期']


# In[21]:


# 问题：怎样将“2018年12月31日”中的年，月，日三个中文字符去掉？
# 方法1：链式replace
df["中文日期"].str.replace('年','').str.replace('月','').str.replace('日','')


# In[22]:


# 方法2:正贼表达式替换
# Series.str默认就开启了正则表达式模式
df['中文日期'].str.replace('[年月日]','')


# In[ ]:




