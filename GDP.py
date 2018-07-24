# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:20:59 2018

@author: Niladri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

GDP_Data=pd.read_csv('gdp_growth.csv')

#1. What was the biggest increase in the GDP in the last ten years?

biggest_increase = 0

for v in GDP_Data['annual_GDP_growth']:
    if v>biggest_increase:
        biggest_increase=v
        
print(biggest_increase)

#Alterantive :

Max_increase = np.max(GDP_Data['annual_GDP_growth'])
print(Max_increase)

#2. What was the biggest decrease in the GDP in the last ten years?

biggest_decrease = 0

for v in GDP_Data['annual_GDP_growth']:
    if v<biggest_decrease:
        biggest_decrease=v
        
print(biggest_decrease)

#Alterantive :

Max_decrease = np.min(GDP_Data['annual_GDP_growth'])
print(Max_decrease)


#3. How many times the GDP has increased at least 2%?

count = 0

for v in GDP_Data['annual_GDP_growth']:
    if v>2:
        count=count+1
        
print(count)


#4. How many times the GDP has decreased?

count = 0

for v in GDP_Data['annual_GDP_growth']:
    if v<0:
        count=count+1
        
print(count)


#5. What was the average growth of the last ten years?

Average_growth=round(np.average(GDP_Data['annual_GDP_growth']),2)

print ('The average growth of the decade was {}.'.format(Average_growth))

#6.   2005 increase
value_increase=((47209-45619)/45619)*100