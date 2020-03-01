#!/usr/bin/env python
# coding: utf-8

# In[15]:


"""
 author:jjk
 datetime:2020/02/04
 coding:utf-8
 project name:test/pandas
 Program function: 

"""
import pandas as pd
# 1、电影数据集的join实例
# 电影评分数据集说明
'''
包含三个文件
1.用户对电影的评分数据 ratings.dat
2.用户本身的信息数据 usersdat
3.电影本身的数据 movies.dat
可以关联三个表，得到一个完整的大表
'''
df_ratings = pd.read_csv(
    './datas/movielens-1m/ratings.dat',
    sep='::', # 分隔符
    engine='python',# 需要指明python来确保分隔符
    names='UserID::MovieID::Rating::Timestamp'.split('::'))


# In[16]:


df_ratings.head()


# In[17]:


df_users = pd.read_csv(
    './datas/movielens-1m/users.dat',
    sep='::', # 分隔符
    engine='python',# 需要指明python来确保分隔符
    names='UserID::Gender::Age::Occupation::Zip-code'.split('::'))


# In[18]:


df_users.head()


# In[19]:


df_movies = pd.read_csv(
    './datas/movielens-1m/movies.dat',
    sep='::', # 分隔符
    engine='python',# 需要指明python来确保分隔符
    names='MovieID::Title::Genres'.split('::'))


# In[20]:


df_movies.head()


# In[22]:


# 评分数据中的moveID进行join
df_ratings_users = pd.merge(df_ratings,df_users,left_on='UserID',right_on='UserID',how='inner')
df_ratings_users.head()


# In[23]:


df_ratings_users_moveis = pd.merge(
    df_ratings_users,
    df_movies,
    left_on='MovieID',
    right_on='MovieID',
    how='inner')
df_ratings_users_moveis.head()


# In[24]:


'''
2、理解merge时数量的对齐关系
以下关系要正确理解：
one-to-one：一对一关系，关联的key都是唯一的
    比如（学号，姓名） merge（学号，年龄）
    结果条数为：1*1
one-to-many：一对多关系，左边唯key，右边不唯key
    比如（学号，姓名） merge（学号，【语文成绩、数学成绩、英语成绩）
    结果条数为：1N
many-to-many：多对多关系，左边右边都不是唯一的
    比如（学号，【语文成绩、数学成绩、英语成绩）erge（学号【篮球足球、乒乓球）
    结果条数为：MN
'''
left = pd.DataFrame({
    'sno':[11,12,13,14],
    'name':['name_a','name_b','name_c','name_d']}) # 创建一个矩阵
left


# In[26]:


right = pd.DataFrame({
    'sno' : [11,12,13,14],
    'age' : ['21','22','23','24']})
right


# In[27]:


# 一对一关系，结果中有四条
pd.merge(left,right,on='sno')


# In[28]:


# 2.2  一对多关系的merge
# 注意：数据会被复制
left = pd.DataFrame({
    'sno':[11,12,13,14],
    'name':['name_a','name_b','name_c','name_d']}) # 创建一个矩阵
left


# In[29]:


right = pd.DataFrame({
    'sno':[11,11,11,12,12,13],
    'grade':['语文88','数学90','英语75','语文66','数学55','英语23']}) # 创建一个矩阵
right


# In[30]:


# 数目以多的一边为准
pd.merge(left,right,on='sno')


# In[32]:


#2.3 多对多
# 注意：结果数量会出现乘法
left = pd.DataFrame({
    'sno':[11,11,12,12,12],
    '爱好':['篮球','羽毛球','乒乓球','篮球','足球']}) # 创建一个矩阵
left


# In[33]:


right = pd.DataFrame({
    'sno':[11,11,11,12,12,13],
    'grade':['语文88','数学90','英语75','语文66','数学55','英语23']}) # 创建一个矩阵
right


# In[34]:


pd.merge(left,right,on='sno')


# In[53]:


# 3、理解left join，right join，inner join,outer join的区别
left = pd.DataFrame({
    'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})
right = pd.DataFrame({
    'key':['k0','k1','k4','k5'],
    'C':['C0','C1','C4','C5'],
    'D':['D0','D1','D4','D5']})


# In[54]:


left


# In[55]:


right


# In[56]:


# 3.1 Inner join 默认
# 左边和右边的key都有，才会出现现在的结果里
pd.merge(left,right,how='inner')


# In[57]:


# 3.2 left join
# 左边的都会出现在结果中，右边的如果无法匹配则为Null
pd.merge(left,right,how='left')


# In[58]:


# 3.3 right join
# 右边的都会出现在结果中，左边的如果无法匹配则为Null
pd.merge(left,right,how='right')


# In[59]:


#3.4 outer join
# 右边和左边都会出现在结果中，如果无法匹配则为null
pd.merge(left,right,how='outer')


# In[63]:


# 4 如果出现非key的字段重名怎么办？
# 3、理解left join，right join，inner join,outer join的区别
left = pd.DataFrame({
    'key':['k0','k1','k2','k3'],
    'A':['A0','A1','A2','A3'],
    'B':['B0','B1','B2','B3']})
right = pd.DataFrame({
    'key':['k0','k1','k4','k5'],
    'A':['C0','C1','C4','C5'],
    'D':['D0','D1','D4','D5']})


# In[64]:


left


# In[65]:


right


# In[66]:


pd.merge(left,right,on='key') # 默认处理


# In[68]:


pd.merge(left,right,on='key',suffixes=('_left','_right'))


# In[ ]:




