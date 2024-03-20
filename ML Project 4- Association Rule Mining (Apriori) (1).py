#!/usr/bin/env python
# coding: utf-8

# In[1]:


#conda install -c conda-forge mlxtend


# In[2]:


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[6]:


#load the online reatil data
df=pd.read_excel(r"C:\Users\aksha\OneDrive\Desktop\Introtallent\python\Data Files used in Projects\Online Retail.xlsx")


# In[8]:


df.head()


# In[5]:


df.shape


# In[9]:


#print the unique country names from country columns
df['Country'].unique()


# In[ ]:


#since buyer behaveiour differ from one geography to another and hence we will take one country at a time for this study


# In[10]:


#some of the description have spaces that need to be removed
df['Description']=df['Description'].str.strip()


# In[11]:


#check if an invoice number is missing
df.isnull().sum()


# In[13]:


#drop the rows that dont have invoice number
df.dropna(axis=0,subset=['InvoiceNo'],inplace=True)


# In[14]:


#looking at sales for france only for ease
basket=(df[df['Country']=="France"]
       .groupby(['InvoiceNo','Description'])['Quantity'].sum()
        .unstack()
        .reset_index().fillna(0)
        .set_index('InvoiceNo'))


# In[15]:


basket.shape


# In[17]:


basket.to_excel(r"C:\Users\aksha\OneDrive\Desktop\final_data.xlsx")


# In[18]:


#encode -ve or 0 value transaction to 0 and +ve one to 1 
def replace_quantity(x):
    if x>=1:
        return 1
    else:
        return 0
#applying encoding
basket_sets=basket.applymap(replace_quantity)


# In[19]:


basket_sets.to_excel(r"C:\Users\aksha\OneDrive\Desktop\basket_data.xlsx")


# In[20]:


#delete POSTAGE item from the data.it is included in many bills to add delivery cahrge
basket_sets.drop('POSTAGE',inplace=True,axis=1)


# In[21]:


#generate frequent item sets that have a support of atleast 7%
#(this number was chosen so that i could get enough useful examples)
frequent_itemsets=apriori(basket_sets,min_support=0.07,use_colnames=True)


# In[22]:


#the final step is to generate the rules with their corresponding support,confidence and lift
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
rules


# In[23]:


#wecan filter the data frame using standard pandas code
#in this case, look for a large lift(6) and high confidence(.8):
rules[(rules['lift']>=6) & (rules['confidence']>=0.8)]


# In[24]:


#export association rules to excel
rules.to_excel(r"C:\Users\aksha\OneDrive\Desktop\output_france.xlsx")


# In[ ]:




