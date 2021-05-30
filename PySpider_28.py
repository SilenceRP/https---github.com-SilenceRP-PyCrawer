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


def ptt():
    content = []
    link = []
    article = []
    URL = 'https://www.ptt.cc/bbs/NBA/index.html'
    resp = requests.get(url=URL)
    soup = BeautifulSoup(markup=resp.text, features='html.parser')
    nodes = soup.select(selector = 'div.title a')
    for i in nodes:
        content.append(i.text)
        
    for j in nodes:
        link.append('https://www.ptt.cc' + j.get('href'))


# In[24]:


def ptt():
    content = []
    link = []
    article = []
    URL = 'https://www.ptt.cc/bbs/NBA/index.html'
    resp = requests.get(url=URL)
    soup = BeautifulSoup(markup=resp.text, features='html.parser')
    nodes = soup.select(selector = 'div.title a')
    for i in nodes:
        link.append('https://www.ptt.cc' + i.get('href'))
    for j in nodes:
        content.append(j.text)

    for i in link:
        resp = requests.get(url=i)
        soup = BeautifulSoup(markup=resp.text, features='html.parser')
        nodes2 = soup.select(selector = 'div #main-content')
        text = ''
        for x in nodes2:
            text += x.text
        article.append(text)
    return content, link, article

