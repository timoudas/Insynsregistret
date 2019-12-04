import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool
import multiprocessing as mp
from lxml import html

df = pd.DataFrame()
list_of_links = []
url = 'https://marknadssok.fi.se/publiceringsklient?Page='
for link in range(1,20):
    urls = url + str(link)
    list_of_links.append(urls) 
    
#Establish connection
data = []
for i in list_of_links:
    r = requests.get(i)
    html = BeautifulSoup(r.content, "html.parser")
#Append each column to it's attribute
    table_body = html.find('tbody')
    if table_body == None:
        print("No Table:", i)
    else:
        rows = table_body.find_all('tr')
    
    
    for row in rows:
        cols = row.find_all('td')
        cols = [x.text.strip() for x in cols]
        data.append(cols)

df = pd.DataFrame(data, columns=['Publiceringsdatum', 'utgivare', 'person', 'befattning',
                                 'Närstående', 'karaktär', 'Instrumentnamn', 'ISIN', 'transaktionsdatum',
                                 'volym', 'volymsenhet', 'pris', 'valuta', 'handelsplats', 
                                 'status', 'detaljer' ])