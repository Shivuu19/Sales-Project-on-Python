# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 11:10:55 2023

@author: SHIVAM
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
matplotlib inline
import seaborn as sns
import os 

os.chdir("D:\Python_Diwali_Sales_Analysis-main")


df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
df.shape
df.head()
df.info
df.drop(['Status','unnamed1'], axis=1, inplace=True)
df.info
pd.isnull(df).sum()
df.dropna(inplace=True)
df.shape

df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtypes
df.columns
df.rename(columns = {'Martial_Status' : 'Shaadi'})
df.info
df.describe
df[['Age','Orders','Amount']].describe()


# Exploratory Data Anaysis

#plotting a bar chart for gender and it's count

ax = sns.countplot(x = 'Gender',data = df)
for bars in ax.containers : ax.bar_label(bars)


#plotting a bar chart for gender Vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)

#From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)
    
    
    
# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)

#From above graphs we can see that most of the buyers are of age group between 26-35 yrs female



# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')

From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively




ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)
    
    
    
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')



#From above graphs we can see that most of the buyers are married (women) and they have high purchasing power


#Occupation
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)
    
    
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')

#From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector


#Product Category

sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)
    
    
    
    
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')

#From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category.




#product id

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


#qMarried women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
