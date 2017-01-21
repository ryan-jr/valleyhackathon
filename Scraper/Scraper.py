# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:26:50 2017

@author: RJR
"""
# Simple web scraper to pull text from neeeded websites/community resources


from lxml import html
import requests

page = requests.get("http://www.homelessresourcesca.org/Cities/ModestoCaliforniaHomelessResources.html")


f = open('workfile.txt', 'w',encoding='utf8')
tree = html.fromstring(page.content)


info = tree.xpath('//span["@id=text"]/text()')


for item in info:
    
    f.write(item)
    
f.close
    
    

