#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
 author:jjk
 datetime:2020/02/05
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd


# In[4]:


# 定义两个目录
work_dir = './course_datas/c15_excel_split_merge' # 数据目录
splits_dir = f'{work_dir}/splits'
import os
if not os.path.exists(splits_dir):
    os.mkdir(splits_dir)# 如果目录不存在，则创建此目录


# In[5]:


# 0、读取源Excel到pandas
df_source = pd.read_excel(f'{work_dir}/crazyant_blog_articles_source.xlsx')
df_source.head()


# In[6]:


df_source.index


# In[7]:


df_source.shape


# In[8]:


total_row_count = df_source.shape[0]
total_row_count # 一共多少行


# In[9]:


'''
一、将一个大 ExcelExcel等份拆成多个
1.使用df.iloc方法，将一个大的dataframe拆分成多个小dataframe
2.将使用dataframe.to_excel保存每个小Excel

'''
# 1、计算拆分后的每个excel的行数
# 这个大的excel，会拆分给这个几个人
user_names = ['xiao_shuai','xiao_wang','xiao_ming','xiao_lei','xiao_bo','xiao_hong']


# In[10]:


# 每个人的任务数目
split_size = total_row_count // len(user_names) # 258%6
if total_row_count % len(user_names) != 0:
    split_size +=1 # 如果不能整除，就让每个人的数目+1，让前面的人多处理一行，后面的人少处理一行
    
split_size # 每个人处理的行数


# In[11]:


# 2、拆分成多个dataframe
df_subs = []
for idx,user_name in enumerate(user_names):# 索引和名称
    #计算每个人的开始和结束索引
    #iloc的开始索引
    begin = idx%split_size
    #iloc的结束索引
    end = begin+split_size
    # 实现df按照iloc拆分
    df_sub = df_source.iloc[begin:end]
    # 将每个字df存入列表
    df_subs.append((idx,user_name,df_sub)) # 传入三个元素


# In[12]:


#3、将每个dataframe存入excel
for idx,user_name,df_sub in df_subs:
    file_name = f'{splits_dir}/crazyant_blog_articles_{idx}_{user_name}.xlsx'
    df_sub.to_excel(file_name,index=False)


# In[13]:


# 二、合并多个小excel到一个大excel
'''
1.遍历文件夹，得到要合并的Exce文件列表
2.分别读取到dataframe，给每个df添加一列用于标记来源
3.使用pd.concat进行df批量合并
4.将合并后的dataframe输出到excel

'''
# 1.遍历文件夹，得到要合并的Exce文件列表
import os
excel_names = [] # 存储excel文件名字
for excel_name in os.listdir(splits_dir):
    excel_names.append(excel_name)
excel_names


# In[14]:


# 2.分别读取到dataframe，给每个df添加一列用于标记来源
df_list = [] 
for excel_name in excel_names:
    # 读取每个excel到df
    excel_path = f'{splits_dir}/{excel_name}'
    df_split = pd.read_excel(excel_path)
    # 得到username
    # 替换换后剩下：数字_名字，只需要名字，则，进行一个切片操作：[2:]
    username = excel_name.replace('crazyant_blog_articles_','').replace('.xlsx','')[2:]
    print(excel_name,username)
    # 给每个df添加一列，即用户名字
    df_split['username'] = username
    
    df_list.append(df_split)


# In[15]:


# 3.使用pd.concat进行df批量合并
df_merged = pd.concat(df_list)
df_merged.shape


# In[16]:


df_merged.head()


# In[17]:


df_merged['username'].value_counts() # 统计df_merged['username']列每个变量取值的次数


# In[18]:


# 4.将合并后的dataframe输出到excel
df_merged.to_excel(f'{work_dir}/crazyant_blog_articles_merged.xlsx',index=False)


# In[ ]:




