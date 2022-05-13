# -*- coding: utf-8 -*-
"""
Created on Fri May 13 11:05:04 2022

@author: DennisLin
"""

import re
import requests
from bs4 import BeautifulSoup

URL = "https://www.dcard.tw/f"

def crawler_func(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    articles = []
    for div in soup.find_all('div', re.compile('PostEntry_content_\w{5}')):
        articles.append(
            {'title': div.h3.text.strip(),
             'excerpt': div.find_all('div')[0].text.strip(),
             'bookmark': re.findall(r'\d+', div.find_all('div')[1].text.strip())[0],
             'response': re.findall(r'\d+', div.find_all('div')[1].text.strip())[1],
             'href': div.parent.parent['href']
             }
            )
    return articles

if __name__=="__main__":
    articles = []
    articles = crawler_func(URL)
    print("共 %d 篇" % (len(articles)))
    for a in articles[:3]:
        print(a)