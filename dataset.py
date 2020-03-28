#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Create a single .xlsx file with 10 sheets inside filled with dummy data.
#Read the .xlsx file using pandas
#Export every single sheet of the .xlsx file as a .csv file. (The Output should produce 10 .csv files that contains values of each sheet of .xlsx file respectively)

import pandas as pd


# In[ ]:


#Read the .xlsx file using pandas
excel_file = 'dataset.xls'
hash = pd.read_excel(excel_file)


# In[10]:


#View Data
hash.head()


# In[18]:


# Read all sheets 
sales_data = pd.ExcelFile('dataset.xls')
Sheet1 = pd.read_excel(sales_data, 'march')
Sheet2 = pd.read_excel(sales_data, 'april')
Sheet3 = pd.read_excel(sales_data, 'may')
Sheet4 = pd.read_excel(sales_data, 'june')
Sheet5 = pd.read_excel(sales_data, 'july')
Sheet6 = pd.read_excel(sales_data, 'august')
Sheet7 = pd.read_excel(sales_data, 'september')
Sheet8 = pd.read_excel(sales_data, 'october')
Sheet9 = pd.read_excel(sales_data, 'november')
Sheet10 = pd.read_excel(sales_data, 'december')


# In[26]:


#Export all sheets as .csv

Sheet1.to_csv('march.csv')
Sheet2.to_csv('april.csv')
Sheet3.to_csv('may.csv')
Sheet4.to_csv('june.csv')
Sheet5.to_csv('july.csv')
Sheet6.to_csv('august.csv')
Sheet7.to_csv('september.csv')
Sheet8.to_csv('october.csv')
Sheet9.to_csv('november.csv')
Sheet10.to_csv('december.csv')


# In[ ]:




