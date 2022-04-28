Exploratory Data Analysis of COVID-19

Authors:  Kesava Dogga, Rushabh Mehta, Krishna Gattani and Sanket Pawar

## Introduction
On March 1, 2020, Covid-19, started effecting the world and became a pandemic. People became aware of their health, and started focusing on health. Vast amount of research was done, to get a vaccine for this disease. FOrtunately, the world got a vaccines, and people were vaccinated. But even after vaccination, we have still have covid-19 cases effecting the world. The data we are importing has the covid-19 cases for each county of New York, USA 

This dataset includes information on the number of tests of individuals for COVID-19 infection performed in New York State beginning March 1, 2020, when the first case of COVID-19 was identified in the state. The primary goal of publishing this dataset is to provide users timely information about local disease spread and reporting of positive cases. 

We referenced this data from New York State Government website

The data is updated daily. 

---

## Sources
- The source code came from https://dev.socrata.com/foundry/health.data.ny.gov/xdss-u53e
- The reference for lamba functions and visualizations https://blog.dominodatalab.com/creating-interactive-crime-maps-with-folium
 							https://www.geeksforgeeks.org/applying-lambda-functions-to-pandas-dataframe/


---

## Explanation of the Code

The code, begins by importing necessary Python packages:
```
import pandas as pd
from sodapy import Socrata
import folium
import numpy as np
import geopy                        # calling into the function
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
import datetime
import matplotlib.pyplot as plt
'''

We have to download Sodapy package 
 	pip install Sodaypy

We then import data from (https://dev.socrata.com/foundry/health.data.ny.gov/xdss-u53e). 	

Finally, we visualize the data.
```
cases_t["new_positives"].plot()
	This plot gives information about total number of Covid-19 cases across New York starting from March 1, 2020
```

## How to Run the Code

1. Open a terminal window.

2. Change directories to where `KESAVADO_RUSHABHR_KGATTANI_SPAWAR.py` is saved.

3. Type the following command:
	```
	python KESAVADO_RUSHABHR_KGATTANI_SPAWAR.py
	```
---
