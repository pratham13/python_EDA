# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:45:26 2020

@author: Prathmesh Jirange
"""

#%% SUmamry statistics

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy import stats

import warnings
warnings.filterwarnings('ignore')


wholesale_data = pd.read_csv('Wholesale customers data.csv')


wholesale_data.head()


max(wholesale_data.Grocery)
min(wholesale_data.Grocery)


col_names = list(wholesale_data)
print(col_names)

max_dict = {col_names[2]: max(wholesale_data.Fresh),
            col_names[3]: max(wholesale_data.Milk),
            col_names[4]: max(wholesale_data.Grocery),
            col_names[5]: max(wholesale_data.Frozen),
            col_names[6]: max(wholesale_data.Detergents_Paper),
            col_names[7]: max(wholesale_data.Delicassen)}

print(max_dict)


max(max_dict, key = max_dict.get)


plt.bar(range(len(max_dict)),
        list(max_dict.values()),
        align = 'center')

plt.xticks(range(len(max_dict)),
           list(max_dict.keys()))

plt.xlabel('Products')
plt.ylabel('Max spend by clients')
plt.show()


sum_dict = {col_names[2]: sum(wholesale_data.Fresh),
            col_names[3]: sum(wholesale_data.Milk),
            col_names[4]: sum(wholesale_data.Grocery),
            col_names[5]: sum(wholesale_data.Frozen),
            col_names[6]: sum(wholesale_data.Detergents_Paper),
            col_names[7]: sum(wholesale_data.Delicassen)}

sum_dict

max(sum_dict, key = sum_dict.get)


# function for plotting the bar graph for different level of summary statistics
def plt_hist(x):  # x will be the name of desired summary dict
    plt.bar(range(len(x)),
        list(x.values()),
        align = 'center')

    plt.xticks(range(len(x)),
               list(x.keys()))

    plt.xlabel('Products')
    plt.ylabel('Max spend by clients')
    plt.show()


plt_hist(max_dict)
plt_hist(sum_dict)
