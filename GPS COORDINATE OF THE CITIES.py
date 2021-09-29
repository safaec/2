#!/usr/bin/env python
# coding: utf-8

# # GPS COORDINATE OF THE CITIES

# ## IMPORT LIBRARIES

# In[2]:


get_ipython().system('pip install geopy ')
get_ipython().system('pip install Nominatim')


# In[ ]:


from geopy.geocoders import Nominatim


# ## LIST OF THE CITIES

# In[3]:


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


# In[6]:


# GPS 

gps = []

for i in cities :
    
    geolocator = Nominatim(user_agent="Safae")

    location = geolocator.geocode(i)
    
    coordinate = (location.latitude, location.longitude)
    
    gps.append(coordinate)

    print(i)
    
    print(gps)


# In[5]:


gps

