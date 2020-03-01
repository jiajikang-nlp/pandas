#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
 author:jjk
 datetime:2020/02/16
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


"""
Panda怎样实现excel的vlookup并且在指定列后面输出？
背景：
   1、有两个列，它们有相同的列；
   2、按照这个列合并成一个大的excel，即vlookup功能，要求：
      只需要第二个excel的少量的列，比如从40个列中挑选2个列
      新增的来自第二个excel的列需要放到第一个excel指定的列后面
   3、将结果输出到一个新的excel

目标：怎样将第二个“学生信息表”的姓名、性别两列，添加到第一个表“学生成绩表”，并且放在第一个表的“学号”列后面？

"""


# In[9]:


# 步骤1:读取两个数据表
# 学生成绩表
df_grade = pd.read_excel('./course_datas/c23_excel_vlookup/学生成绩表.xlsx')
df_grade.head()


# In[10]:


# 学生信息表
df_info = pd.read_excel('./course_datas/c23_excel_vlookup/学生信息表.xlsx')
df_info.head()


# In[12]:


# 步骤2：实现两个表的关联
# 即excel的vlookup功能
# 掷筛学第二个表的少量的列
df_sinfo = df_info[['学号','姓名','性别']]
df_sinfo.head()


# In[13]:


df_merge = pd.merge(left=df_grade,right=df_sinfo,left_on='学号',right_on='学号')
df_merge.head()


# In[14]:


# 步骤3：调整列的顺序
df_merge.columns # index对象


# In[15]:


# 问题：怎样将“姓名”，“性别”两列，放到“学号”的后面？
# 需要用python的语法实现列表的处理
new_columns = df_merge.columns.to_list() # 将index变成列表形式
new_columns


# In[16]:


# 按照逆序insert，会将“姓名”，“性别”放到“学号”后面
for name in ['姓名','性别'][::-1]: # 先取出性别，再取出姓名
    new_columns.remove(name)
    # 位置：index('学号')后一位
    new_columns.insert(new_columns.index('学号')+1,name) # insert语法每次都在“学号”后面添加，最终顺序：学号，姓名，性别
new_columns


# In[17]:


df_merge = df_merge.reindex(columns=new_columns) # 调整我们的索引
df_merge.head()


# In[ ]:


# 步骤四：输出最终的excel文件
df_merge.to_excel('./course_datas/c23_excel_vlookup/合并后的数据表.xlsx',index=False)

