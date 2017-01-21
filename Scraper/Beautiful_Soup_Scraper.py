# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 22:05:25 2017

@author: RJR
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd


url = "http://www.shelterlistings.org/county/ca-stanislaus-county.html"
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

table = soup.find_all('table')[0]
rows = table.find_all('td')[1:]

print(rows)