#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
 author:jjk
 datetime:2020/01/31
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
fpath = pd.read_excel('./datas/student_excel/student_excel.xlsx',skiprows=2) # 忽略前2行


# In[3]:


fpath


# In[4]:


# 步骤2：检测空值
fpath.isnull()


# In[5]:


fpath['分数'].isnull()


# In[6]:


fpath['分数'].notnull()


# In[7]:


# 筛选没有空分数的所有行
fpath.loc[fpath['分数'].notnull(),:]


# In[8]:


# 步骤3：删除掉全是空值的列
fpath.dropna(axis="columns",how='all',inplace=True) # 或者axis=1


# In[9]:


fpath


# In[10]:


# 步骤4：删除掉全是空值的行
fpath.dropna(axis=0,how='all',inplace=True)


# In[11]:


fpath


# In[12]:


# 步骤5：将分数为空的列填充为0分
fpath.fillna({'分数':0}) # 等价于：fpath.loc[:,'分数'] = fpath['分数'].fillna(0)


# In[13]:


# 步骤6：将姓名为空的填充
# 使用有限制填充，用ffill：forward fill
fpath.loc[:,'姓名'] = fpath['姓名'].fillna(method='ffill')


# In[14]:


fpath


# In[ ]:


# 步骤7：将清洗好的excel保存
fpath.to_excel('./datas/student_excel/student_excel_clean.xlsx',index=False) # index=False，是将索引不写入，这样就只保存：姓名，科目，分数

