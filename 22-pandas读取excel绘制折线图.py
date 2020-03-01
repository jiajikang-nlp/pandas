#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
 author:jjk
 datetime:2020/02/16
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
import numpy as np
#%matplotlib inline


# In[2]:


"""
PandasPyecharts怎样结合绘制交互性折线图？
背景：
   PandasPython是用于数据分析领域的超级牛的库
   Echarts是百度开源的非常好用强大的可视化图表库， PyechartsPython是它的库版本

"""


# In[3]:


xlsx_path = './datas/stocks/baidu_stocks.xlsx'
df = pd.read_excel(xlsx_path,index_col='datetime',parse_dates=True)
df.head()


# In[4]:


df.index # 索引


# In[5]:


df.sort_index(inplace=True) # 索引排序，inplace=True表示修改这个索引
df.head()


# In[12]:


# 2、使用pyecharts绘制折线图
from pyecharts.charts import Line
from pyecharts import options as opts
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


# 折线图
line = Line() # 折线图对象

# x轴
line.add_xaxis(df.index.to_list()) # x轴数据：列表——日期

# 每个y轴
line.add_yaxis("开盘价",df['open'].round(2).to_list())
line.add_yaxis("收盘价",df['close'].round(2).to_list())

# 图标配置
line.set_global_opts(
    title_opts=opts.TitleOpts(title='百度股票2019年'), 
    tooltip_opts=opts.TooltipOpts(trigger='axix',axis_pointer_type='cross'))


# In[15]:


# 渲染数据
line.render_notebook()
line.render()


# In[ ]:





# In[ ]:




