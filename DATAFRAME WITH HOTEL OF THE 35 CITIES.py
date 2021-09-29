#!/usr/bin/env python
# coding: utf-8

# # CREATE A DATAFRAME WITH HOTEL OF THE 35 CITIES

# In[1]:


import pandas as pd


# In[2]:


cities = ["Mont Saint Michel",
"St Malo",
"Bayeux",
"Le Havre",
"Rouen",
"Paris",
"Amiens",
"Lille",
"Strasbourg",
"Chateau du Haut Koenigsbourg",
"Colmar",
"Eguisheim",
"Besancon",
"Dijon",
"Annecy",
"Grenoble",
"Lyon",
"Gorges du Verdon",
"Bormes les Mimosas",
"Cassis",
"Marseille",
"Aix en Provence",
"Avignon",
"Uzes",
"Nimes",
"Aigues Mortes",
"Saintes Maries de la mer",
"Collioure",
"Carcassonne",
"Ariege",
"Toulouse",
"Montauban",
"Biarritz",
"Bayonne",
"La Rochelle"]


# In[7]:


dataset = pd.read_csv("hotels.csv", lineterminator='\n')


# In[8]:


dataset = dataset.dropna()


# In[9]:


dataset['rating'] = dataset['rating'].str.replace(',','.')
dataset['rating'] = dataset['rating'].astype('str').astype('float')


# In[10]:


dataset[['lat', 'lon']] = dataset['GPS'].str.split(',', 1, expand=True)
dataset = dataset.drop(['GPS'],axis = 1)


# In[11]:


dataset.head()


# In[15]:


dataset = dataset[(dataset["Location"].str.isin(cities))]


# In[ ]:




