#!/usr/bin/env python
# coding: utf-8

# # SCRAP BOOKING.COM

# ## IMPORT LIBRARIES

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# ## SCRAP

# In[2]:


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# List of information we need
name = []
link = []
loc = []
gps = []
rating = []
reviews = []
rating_desc = []
desc = []


# In[3]:


for i in range(0,40):
    
    print('page: '+str(i+1))
    
    #url of france's hotel
    url = 'https://www.booking.com/searchresults.fr.html?label=gen173nr-1DCAEoggI46AdIM1gEaLUBiAEBmAENuAEXyAEM2AED6AEBiAIBqAIDuALDxM2KBsACAdICJGMxZDE4N2EwLTZlNmEtNDdiOS1hMDUyLTExMTM4YjkwMjQ5MtgCBOACAQ&sid=f6a32638e7ad726bc4f5746cd06b94b9&tmpl=searchresults&ac_click_type=b&ac_position=1&city=20088325&class_interval=1&dest_id=73&dest_type=country&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=country&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=searchresults&src_elem=sb&srpvid=1a52853e43e50058&ss=France&ss_all=0&ss_raw=france&ssb=empty&sshis=0&ssne=New%20York&ssne_untouched=New%20York&top_ufis=1&rows=25&offset='+str(25*i)
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')

    for item in soup.select('.sr_property_block'):
        try:
            print(item.select('.sr-hotel__name')[0].get_text().strip())
            name.append(item.select('.sr-hotel__name')[0].get_text().strip())
        except Exception as e:
            name.append('')

        try:
            link.append('booking.com/'+item.select('.hotel_name_link')[0]['href'].split('\n')[1])
        except Exception as e:
            link.append('')
        
        try:
            loc.append(item.select('.bui-link')[0].get_text().strip().strip().split('\n')[0])
        except Exception as e:
            loc.append('')
        
        try:
            gps.append(item.select('.bui-link')[0]['data-coords'])
        except Exception as e:
            gps.append('')
        
        try:
            rating.append(item.select('.bui-review-score__badge')[0].get_text().strip())
        except Exception as e:
            rating.append('')
        
        try: 
            reviews.append(item.select('.bui-review-score__text')[0].get_text().strip())
        except Exception as e:
            reviews.append('')
        
        try:
            rating_desc.append(item.select('.bui-review-score__title')[0].get_text().strip())
        except Exception as e:
            rating_desc.append('')
        
        try:
            
            desc.append(item.select('.hotel_desc')[0].get_text().strip())
        except Exception as e:
            desc.append('')
    


# In[4]:


data = pd.DataFrame({'hotel_name':name,
                     'location':loc,
                     'GPS':gps,
                     'link':link,
                     'rating':rating,
                     'rating_desc':rating_desc,
                     'reviews':reviews,
                     'description':desc})


# In[6]:


data.to_csv('hotels.csv', index=False)

