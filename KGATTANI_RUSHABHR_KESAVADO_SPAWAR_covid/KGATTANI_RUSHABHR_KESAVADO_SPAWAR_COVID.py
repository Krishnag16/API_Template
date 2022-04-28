# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:23:35 2022

@author: Krishna Gattani
"""

import pandas as pd
from sodapy import Socrata
import folium
import numpy as np
import geopy # calling into the function
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
import datetime
import matplotlib.pyplot as plt

client = Socrata("health.data.ny.gov", None)

results = client.get("xdss-u53e", limit=20000)

results_df = pd.DataFrame.from_records(results)

county = results_df["county"].unique()
county = np.delete(county,np.where(county == "Central New York"),None)
county = np.delete(county,np.where(county == "Capital Region"),None)

results_df['tested_positive']=results_df['test_positive'].apply(lambda x: x.replace('%',""))
results_df['tested_positive'] = results_df['tested_positive'].apply(lambda x : float(x))
results_df['new_positives'] = results_df['new_positives'].apply(lambda x : int(x))
results_df[["date","zeros"]]= results_df['test_date'].str.split("T",expand = True)
positives = pd.DataFrame(results_df.groupby('county')['new_positives'].sum())
county_positives = list(positives['new_positives'])

def co_ordinates(a): # defining the function for returning the co-ordinates
    geolocator = Nominatim(user_agent="MyApp")
    b = geolocator.geocode('{0}'",NY".format(a))
    return b.latitude,b.longitude

co_ordinate = []  # collecting the co-ordinates
for i in range (0,len(county)):
    lat,long=co_ordinates(county[i])
    co_ordinate.append([lat,long])
    
lati=[]
longi=[]
for i in range(0,len(co_ordinate)):
    a=co_ordinate[i][0]
    lati.append(a)

for i in range(0,len(co_ordinate)):
    a=co_ordinate[i][1]
    longi.append(a)
    
temperature_map=folium.Map(Location=[42.6511674, -73.754968],zoom_start=12)
fg=folium.FeatureGroup(name='Cases')

for i in range(0,len(county)):
    fg.add_child(folium.Marker(location=[co_ordinate[i][0],co_ordinate[i][1]],popup=county[i]+","+str(county_positives[i]),icon=folium.Icon(color='green')))
temperature_map.add_child(fg)

cases = results_df.groupby('test_date')['tested_positive'].sum()

cases_t = results_df.groupby('test_date')['new_positives'].sum()

cases_t = pd.DataFrame(cases_t)

cases_t["new_positives"].plot()

def mov_avg(data, n):
    return sum(data[len(data)+1-1-n:len(data)+1-1])/n

numbers = list(cases_t["new_positives"])

numbers.append(mov_avg(numbers,3))

a = list(results_df['date'].unique())

chart_date=[]
county_date=[]
start = datetime.datetime.strptime(a[len(a)-1], "%Y-%m-%d")
end = datetime.datetime.strptime(a[0], "%Y-%m-%d")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+2)]
date_generated1 = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1)]

for date in date_generated:
    chart_date.append(date.strftime("%Y-%m-%d"))

for date in date_generated1:
    county_date.append(date.strftime("%Y-%m-%d"))


plt.figure(figsize = (50,40))
plt.plot(chart_date, numbers, color='red')
plt.title('Cases Vs Date', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Cases', fontsize=14)
plt.show()