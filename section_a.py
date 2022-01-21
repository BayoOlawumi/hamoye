#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df  = pd.read_csv('FoodBalance.CSV')


# In[4]:


df.head()


# ### Perform a groupby sum aggregation on ‘Item’

# In[15]:


df.groupby('Item').agg('sum')


# **What is the mean and standard deviation across the whole dataset for the year 2015 to 3 decimal places?**

# In[17]:


mean_2015 = df['Y2015'].mean()
mean_2015


# In[18]:


std_2015 = df['Y2015'].std()
std_2015


# **What is the total number and percentage of missing data in 2016 to 2 decimal places?**

# In[22]:


total_null = df['Y2016'].isnull().sum()
total_null


# In[23]:


perctage_missing = (total_null/df['Y2016'].count())*100 
perctage_missing


# **Which year had the highest correlation with ‘Element Code’?**

# In[24]:


df.corr().abs()


# **What year has the highest sum of Import Quantity?
# Hint- Perform a groupby operation on ‘Element’ and use the resulting Dataframe to answer the question**

# In[28]:


elem_grp = df.groupby('Element')


# In[29]:


elem_grp.first()


# **What is the total number of the sum of Production in 2014?
# Hint- Perform a groupby operation on ‘Element’ and use the resulting Dataframe to answer the question**

# In[30]:


elem_grp['Y2014'].sum()


# **Which of these elements had the highest sum in 2018?
# Hint-  Select columns ‘Y2018’ and ‘Element’, Perform a groupby operation on ‘Element’ on the selected dataframe and answer the  question.**

# **Which of these elements had the 3rd lowest sum in 2018?
# Hint-  Select columns ‘Y2018’ and ‘Element’, Perform a groupby operation on ‘Element’ on the selected dataframe and answer the  question.**

# In[33]:


elem_grp2 = df[['Y2018','Element']].groupby('Element')
elem_grp2.first()


# In[35]:


elem_grp.first()


# In[37]:


len(df['Area'].unique())


# In[ ]:




