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
# 数据为北京2018年全年天气预报
df = pd.read_csv("./datas/beijing_tianqi/beijing_tianqi_2018.csv")
print(df.head())


# In[3]:


# 设置索引为日期，方便按日期筛选
df.set_index('ymd',inplace=True)


# In[4]:


# 按字符串处理
df.index


# In[5]:


df.head() # 再次查看，数据格式，就会以日期为索引奥


# In[6]:


# 替换掉温度后面的后缀℃
df.loc[:,'bWendu'] = df["bWendu"].str.replace("℃","").astype("int32") # 所有的行对应的‘bWendu’列，等于一个新的数据列：进行一个替换，然后设置一个数据类型
df.loc[:,'yWendu'] = df['yWendu'].str.replace("℃","").astype("int32")


# In[7]:


df.dtypes #查看一下数据类型


# In[8]:


df.head()


# In[11]:


# 4.1 使用单个label查询数据
# 得到单个值
df.loc['2018-01-03','bWendu']


# In[13]:


# 得到一个Series
df.loc['2018-01-04',['bWendu','yWendu']]


# In[14]:


df.head()


# In[16]:


#4.2 使用值列表批量查询
# 得到Series
df.loc[['2018-01-03','2018-01-04','2018-01-05'],'bWendu']


# In[17]:


# 得到DataFrame
df.loc[['2018-01-03','2018-01-04','2018-01-05'],['bWendu','yWendu']]


# In[19]:


# 行index按区间
df.loc['2018-01-03' : '2018-01-05', 'bWendu'] # 按照区间奥


# In[20]:


# 列index按区间
df.loc['2018-01-03','bWendu':'fengxiang']


# In[21]:


# 行和列按区间查询
df.loc['2018-01-03' : '2018-01-05','bWendu':'fengxiang']


# In[22]:


# 使用条件表达式查询
# bool列表的长度得等于行数或者列数
# 简单条件查询，最低温度低于-10度的列表
df.loc[df['yWendu']<-10,:] # 所有的列


# In[23]:


df['yWendu']<-10


# In[27]:


# 复杂条件查询，查一下我心中的完美天气
# 注意：组合条件用&符号合并，每个条件判断都的带括号
df.loc[(df['bWendu']<=30) & (df['yWendu']>=15) & (df['tianqi']=='晴') & (df["aqiLevel"]==1),:]


# In[28]:


#再次观察这里的boolean条件
(df['bWendu']<=30) & (df['yWendu']>=15) & (df['tianqi']=='晴') & (df['aqiLevel']==1)


# In[29]:


# 4.5 调用函数查询
# 直接用lambda表达式
df.loc[lambda df : (df['bWendu']<=30) & (df['yWendu']>=15), :]


# In[30]:


# 编写自己的函数，查询9月份，空气质量好的数据
def query_my_data(df):
    # 每一行：df.index,
    # 转换成字符串形式：df.index.str
    # 查询九月份数据：df.index.str.startswith('2018-09')
    # 空气质量等于优秀：& df['aqiLevel']==1
    return df.index.str.startswith('2018-09') & df['aqiLevel'] ==1 
df.loc[query_my_data,:] # 调用函数


# In[ ]:




