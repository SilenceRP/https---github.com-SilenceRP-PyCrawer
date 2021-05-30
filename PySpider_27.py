#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


URL = 'https://www.ptt.cc/bbs/NBA/index.html'
resp = requests.get(url=URL)


# In[3]:


soup = BeautifulSoup(markup=resp.text, features='html.parser')
nodes = soup.select(selector = 'div.title a')
for i in nodes:
    print(i.text)


# In[ ]:




