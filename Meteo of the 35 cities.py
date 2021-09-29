#!/usr/bin/env python
# coding: utf-8

# # METEO

# ## IMPORT LIBRARIES

# In[1]:


import requests
import pandas as pd
import json
import itertools 


# - GPS LIST OF THE CITIES

# In[87]:


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


# In[2]:


gps = [(48.6355232, -1.5102571),
 (48.6454528, -2.015418),
 (49.2764624, -0.7024738),
 (49.4938975, 0.1079732),
 (49.4404591, 1.0939658),
 (48.8566969, 2.3514616),
 (49.8941708, 2.2956951),
 (50.6365654, 3.0635282),
 (48.584614, 7.7507127),
 (48.249489800000006, 7.34429620253195),
 (48.0777517, 7.3579641),
 (48.0447968, 7.3079618),
 (47.2380222, 6.0243622),
 (47.3215806, 5.0414701),
 (45.8992348, 6.1288847),
 (45.1875602, 5.7357819),
 (45.7578137, 4.8320114),
 (43.7497, 6.32859),
 (43.1506968, 6.3419285),
 (43.2140359, 5.5396318),
 (43.2961743, 5.3699525),
 (43.5298424, 5.4474738),
 (43.9492493, 4.8059012),
 (44.0121279, 4.4196718),
 (43.8374249, 4.3600687),
 (43.5658225, 4.1912837),
 (43.4522771, 4.4287172),
 (42.52505, 3.0831554),
 (43.2130358, 2.3491069),
 (42.9455368, 1.4065544156065486),
 (43.6044622, 1.4442469),
 (44.0175835, 1.3549991),
 (43.471143749999996, -1.552726590666314),
 (43.4933379, -1.475099),
 (46.1591126, -1.1520434)]


# - SEPARATE LAT ET LON

# In[3]:


lat=[]
for x in gps :
    lat.append(x[0])
lat


# In[4]:


lon=[]
for x in gps :
    lon.append(x[1])
lon


# ## SCRAPPE API 

# In[68]:


response =requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=48.6355232&lon=-1.5102571&exclude=minutely,hourly,current&appid=14e120e33e7ac812d1312806f1ce923e")
r = response.json()
r.keys()


# - METEO

# In[69]:


meteo = []
for x, y in zip(lat, lon): 
    r = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=current,minutely,hourly&appid=14e120e33e7ac812d1312806f1ce923e".format(x, y))
    meteo.append(r.json())
                 
meteo


# In[78]:


meteo_daily =[]
for a in meteo:
    meteo_daily.append(a["daily"])


# In[79]:


meteo_daily[0][0]


# - Create a dataframe of the weather

# In[80]:


meteo_daily = pd.DataFrame(meteo_daily)


# In[81]:


def categorize(x):
    for i in range(8):
        x["temp_min_day{}".format(i)] = x[i]["temp"]["min"]
        x["temp_max_day{}".format(i)] = x[i]["temp"]["max"]
        x["clouds_day{}".format(i)] = x[i]["clouds"]
        x["wind_speed_day_{}".format(i)] = x[i]["wind_speed"]
        x["pop_day_{}".format(i)] = x[i]["pop"]
    return x


# In[82]:


meteo_daily = meteo_daily.apply(categorize, axis=1)
meteo_daily.head()


# In[83]:


removed_columns = meteo_daily.drop(meteo_daily.iloc[:, 0:8], inplace =True, axis=1)


# In[88]:


meteo_daily["lat"] = lat
meteo_daily["lon"] = lon
meteo_daily["city"] = cities


# In[89]:


meteo_daily.head()


# In[90]:


meteo_daily.to_csv("meteo7days.csv", index = False)


# In[ ]:




