#!/usr/bin/env python
# coding: utf-8

# # Top 5 cities with Top 20 Hotel

# ## IMPORT LIBRARIES

# In[2]:


import pandas as pd
import plotly.express as px


# # TOP 5 CITIES

# In[26]:


data = pd.read_csv("meteo7days.csv")


# In[27]:


data.head()


# In[28]:


#Create a new dataframe

data_mean = pd.DataFrame()


# In[29]:


# Calculate the mean of the columns, and put them in the new dataframe

data_mean["mean_temp_max_day"] = (data["temp_max_day1"] +  data["temp_max_day2"] +  data["temp_max_day3"]
                            +  data["temp_max_day4"] + data["temp_max_day5"] +  data["temp_max_day6"]
                            +  data["temp_max_day7"])/7

data_mean["mean_clouds_day"] = (data["clouds_day1"] +  data["clouds_day2"] +  data["clouds_day3"]
                            +  data["clouds_day4"] + data["clouds_day5"] +  data["clouds_day6"]
                            +  data["clouds_day7"])/7

data_mean["mean_wind_speed_day"] = (data["wind_speed_day_1"] +  data["wind_speed_day_2"] +  data["wind_speed_day_3"]
                            +  data["wind_speed_day_4"] + data["wind_speed_day_5"] +  data["wind_speed_day_6"]
                            +  data["wind_speed_day_7"])/7

data_mean["mean_pop_day"] = (data["pop_day_1"] +  data["pop_day_2"] +  data["pop_day_3"]
                            +  data["pop_day_4"] + data["pop_day_5"] +  data["pop_day_6"]
                            +  data["pop_day_7"])/7

data_mean["mean_temp_min_day"] = (data["temp_min_day1"] +  data["temp_min_day2"] +  data["temp_min_day3"]
                            +  data["temp_min_day4"] + data["temp_min_day5"] +  data["temp_min_day6"]
                            +  data["temp_min_day7"])/7

data_mean["lat"] = data["lat"]

data_mean["lon"] = data["lon"]

data_mean["city"] = data["city"]

data_mean.head()


# In[30]:


data_mean.shape


# - Criteria for a good temp

# mean_temp_max_day < 38
# <br> mean_clouds_day < 70
# <br> mean_wind_speed_day <7
# <br> mean_pop_day < 0.50
# <br> mean_temp_min_day < 18

# - New data frame of the cities with a good temp

# In[31]:


top_5_cities = data_mean[(data_mean["mean_clouds_day"]<70)
                                   & (data_mean["mean_wind_speed_day"]<7)
                                   & (data_mean["mean_pop_day"]<0.70)
                                   & (data_mean["mean_temp_min_day"]<18)
                                  ]

top_5_cities = top_5_cities.sort_values(by=["mean_temp_min_day"], ascending=False)

top_5_cities = top_5_cities.iloc[0:5, :]

top_5_cities


# In[32]:


top_5_cities.shape


# In[33]:


fig = px.scatter_mapbox(
        top_5_cities, 
        lat="lat", 
        lon="lon",
        color="mean_temp_min_day",
        mapbox_style="open-street-map",
)

fig.show("notebook")


# In[40]:


#best_cities = [(top_5_cities["city"]).to_string(index=False)]
print("The best cities with the best temp are")
print((top_5_cities["city"]).to_string(index=False))


# In[42]:


best_cities = ["Aix en Provence",
        "Avignon",
          "Nimes",
           "Uzes",
       "Grenoble"]


# # TOP 20 HOTEL IN THE AREA

# In[20]:


data2 = pd.read_csv("hotels.csv", lineterminator='\n')
data2.head()


# ### Analyse of the dataset

# In[4]:


data2.info()


# In[21]:


data2 = data2.dropna()


# In[22]:


data2['rating'] = data2['rating'].str.replace(',','.')
data2['rating'] = data2['rating'].astype('str').astype('float')
data2['rating']


# In[10]:


data2.head()


# In[ ]:


### Separate the GPS column


# In[23]:


data2[['lat', 'lon']] = data2['GPS'].str.split(',', 1, expand=True)
data2 = data2.drop(['GPS'],axis = 1)
data2.head()


# In[49]:


print(data2[data2['location'].str.contains("Aix en Provence")])


# In[46]:


top_20_hotels = data2.loc[(data2["location"].str.contains(["Aix en Provence",
        "Avignon",
          "Nimes",
           "Uzes",
       "Grenoble"]))
                        & (data2["rating"]>8)
                                  ]
(df[df['a'].str.contains('b')])
top_20_hotels = top_20_hotels.sort_values(by=["rating"], ascending=False)

#top_20_hotels = top_20_hotels.iloc[:20, :]

top_20_hotels


# In[37]:


fig = px.scatter_mapbox(
        top_20_hotels, 
        lat="lat", 
        lon="lon",
        color="rating",
        mapbox_style="open-street-map",
)

fig.show("notebook")


# In[ ]:




