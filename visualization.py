# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:26:06 2020

@author: Prathmesh Jirange
"""

#%% Load the basic libraries

import matplotlib.pyplot as plt

x = range(0,11)
y = range(0,11)[::-1]
z = range(0,11)

#%%
plt.plot(x,y,marker = '^', markerfacecolor = 'yellow',
         markersize = 10,
         linewidth = 3,
         linestyle = '-.',
         label = 'line 1', color = 'b')
#plt.plot(x,z, label = 'line 2', color = 'm')
plt.xlabel('x-axis')
plt.ylabel('y-label')
plt.title('Linear function in opposite direction')
plt.legend()
plt.show()


x = ('cat', 'dog', 'camel')
y = ('ram', 'matt', 'ted')


#%% Lines using the numpy modules

import numpy as np


x = np.arange(0,2*(np.pi), 0.1)
y = np.cos(x)

plt.plot(x,y,
         color = 'orange',
         linewidth = 2,
         linestyle = ':')
plt.title('THe cosine curve')
plt.show()

#%% scatter plot


x = range(0,11)
y = range(10,21)

plt.scatter(x,y,
            marker = '*',
            s = 50,
            color = 'deeppink')
plt.title('scatter plot')
plt.show()



#%% Visualize a real dataset

import pandas as pd
 

absentees_data = pd.read_csv('Absenteeism_at_work.csv',
                             sep = r'\s*,\s*',
                             engine = 'python')



absentees_data.head()

absentees_data.describe()


x = absentees_data["Age"]
y = absentees_data["Distance from Residence to Work"]

plt.scatter(x,y,
            marker = 'o',
            color = 'green',
            s = 10)

''' If required to focus on a subset

plt.xlim(0,30)
plt.ylim(35,60)

'''

plt.show()




#%% Specific months of the year where absentism is higher


fig, ax= plt.subplots(figsize = (12,6))

ax.hist(absentees_data["Month of absence"], bins = 12)

plt.title('Absence with Months')
plt.xlabel('Months')
plt.show()


#%% Using aggregate to see the month average

data = absentees_data.groupby(['Month of absence']).mean()

data = data['Absenteeism time in hours']

data.plot(kind = 'line')

plt.show()


#%% boxlot

figure = plt.figure()

ax = figure.add_subplot(1,1,1)

ax.boxplot(absentees_data['Work load Average/day'])
plt.show()



#%%

data = absentees_data.groupby(['Seasons']).sum().stack()  #indexed by the group by variable the returned variable is a pd.dataframe

data_temp = data.unstack()

x = data_temp['Absenteeism time in hours']
label  = data_temp.index


plt.axis("equal")
plt.pie(x,
        labels = label, # can be passed as a string list containing the name of respective seasons
        autopct = "%1.1f%%")

plt.title('Absenteeism by season')
plt.legend()
plt.show()










