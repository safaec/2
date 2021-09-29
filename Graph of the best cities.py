#!/usr/bin/env python
# coding: utf-8

# # ANALYSE

# ## IMPORT LIBRARIES

# In[4]:


import pandas as pd
import plotly.express as px


# In[33]:


data = pd.read_csv("meteo7days.csv")


# In[34]:


data.head()


# In[11]:


#Create a new dataframe

data_mean = pd.DataFrame()


# In[36]:


# Calculate the mean of the columns, and put them in the new dataframe

data_mean["mean_temp_max_day"] = (data["temp_max_day1"] + data["temp_max_day2"] + data["temp_max_day3"]
                                  + data["temp_max_day4"] + data["temp_max_day5"] + data["temp_max_day6"]
                                  + data["temp_max_day7"])/7

data_mean["mean_clouds_day"] = (data["clouds_day1"] + data["clouds_day2"] + data["clouds_day3"]
                                + data["clouds_day4"] + data["clouds_day5"] + data["clouds_day6"]
                                + data["clouds_day7"])/7

data_mean["mean_wind_speed_day"] = (data["wind_speed_day_1"] + data["wind_speed_day_2"] + data["wind_speed_day_3"]
                                    + data["wind_speed_day_4"] + data["wind_speed_day_5"] + data["wind_speed_day_6"]
                                    + data["wind_speed_day_7"])/7

data_mean["mean_pop_day"] = (data["pop_day_1"] + data["pop_day_2"] + data["pop_day_3"]
                             + data["pop_day_4"] + data["pop_day_5"] + data["pop_day_6"]
                             + data["pop_day_7"])/7

data_mean["mean_temp_min_day"] = (data["temp_min_day1"] + data["temp_min_day2"] + data["temp_min_day3"]
                                  + data["temp_min_day4"] + data["temp_min_day5"] + data["temp_min_day6"]
                                  + data["temp_min_day7"])/7

data_mean["lat"] = data["lat"]

data_mean["lon"] = data["lon"]

data_mean["city"] = data["city"]

data_mean.head()


# In[31]:


data_mean.shape


# - Criteria for a good temp

# mean_temp_max_day < 38
# <br> mean_clouds_day < 70
# <br> mean_wind_speed_day <7
# <br> mean_pop_day < 0.50
# <br> mean_temp_min_day < 18

# - New data frame of the cities with a good temp

# In[37]:


cities_with_good_temp = data_mean[(data_mean["mean_clouds_day"]<70)
                                   & (data_mean["mean_wind_speed_day"]<7)
                                   & (data_mean["mean_pop_day"]<0.70)
                                   & (data_mean["mean_temp_min_day"]<18)
                                  ]

cities_with_good_temp.head()


# In[29]:


cities_with_good_temp.shape


# In[38]:


fig = px.scatter_mapbox(
        cities_with_good_temp, 
        lat="lat", 
        lon="lon",
        color="mean_temp_min_day",
        mapbox_style="open-street-map",
)

fig.show("notebook")


# In[43]:


print("The best cities with the best temp are")
print((cities_with_good_temp["city"]).to_string(index=False))


# In[ ]:




