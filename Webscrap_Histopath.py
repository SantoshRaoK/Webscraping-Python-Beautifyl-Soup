import requests
import pandas as pd
from bs4 import BeautifulSoup
response=requests.get("https://www.histopath.com.au/locations/nsw-locations")
soup=BeautifulSoup(response.content,'html.parser')
#clinic names
names=soup.find_all('h3',class_='heading-3')
name=[]
for i in names:
    d=i.get_text()
    name.append(d)
#Clinic opening hours
opening_hours=soup.find_all('div',class_='text-block-4')
open=[]
for i in opening_hours:
    d=i.get_text()
    open.append(d)
#Clinic location

location=soup.find_all('div',class_='color-text center')
loc=[]
for i in location:
    d=i.get_text()
    loc.append(d)
df=pd.DataFrame()
df['names']=name
df['opening_hours']=open
df['location']=loc
df.to_csv('Histopath.pdf')