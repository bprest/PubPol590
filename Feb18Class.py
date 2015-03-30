from __future__ import division  # imports the division capacity from the future version of Python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import xlrd
import time
import csv
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.special import stdtr

print(time.ctime())
start = time.time()
main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
#main_dir = u'C:/Users/Brianprest/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
pathlist = [os.path.join(main_dir,v) for v in os.listdir(main_dir) if v.startswith("file")]
df = pd.concat([pd.read_csv(v, sep = ",", names = ['panid','time','kwh'], parse_dates = [1]) for v in pathlist], ignore_index = True)

assign = pd.read_csv(main_dir + "/sample_assignments.csv", sep = ",", usecols = [0,1])
#assign = assign[[0,1]]

df = pd.merge(df,assign)

grp = df.groupby(['assignment','time'])
grpdictionary = grp.groups
grpdictionary.keys()

trt = {k[1]: df.kwh[v] for k,v in grp.groups.iteritems() if k[0]=="T"} # if we did this, it would keep the index values in our treatment dictionary. we don't want this.
trt = {k[1]: df.kwh[v].values for k,v in grp.groups.iteritems() if k[0]=="T"} # .values only keeps the values, not the index.
ctrl = {k[1]: df.kwh[v].values for k,v in grp.groups.iteritems() if k[0]=="C"}

keys = trt.keys()

# create dataframes of this info
tstats = DataFrame([(k, np.abs(ttest_ind(trt[k],ctrl[k], equal_var=False)[0])) for k in keys], columns=['date','tstat'])
pvals = DataFrame([(k, np.abs(ttest_ind(trt[k],ctrl[k], equal_var=False)[1])) for k in keys], columns=['date','pval'])
t_p = pd.merge(tstats,pvals)
t_p.sort(['date'], inplace=True) # inplace replaces it (assigns t_p to the new thing. equivalent to t_p = t_p.sort(['date'])
t_p.reset_index(inplace=True, drop=True) # By default, it saves the old index. But drop=True drops this.

# Plotting -----------------------------------------
fig1 = plt.figure() # initialize a figure. (get our canvas)
ax1 = fig1.add_subplot(2,1,1) # picture within a picture. (rows,cols,first plot). So ax1 only corresponds to 1st plot. (2,1,2) would only affect the second plot
#ax1.plot(t_p['date'],t_p['tstat'])
ax1.plot(t_p['tstat'])
ax1.axhline(2, color='red', linestyle="--")
ax1.set_title('t-stats over time')

ax2 = fig1.add_subplot(2,1,2) # picture within a picture. (rows,cols,first plot). So ax1 only corresponds to 1st plot. (2,1,2) would only affect the second plot
#ax2.plot(t_p['date'],t_p['tstat'])
ax2.plot(t_p['pval'])
ax2.axhline(0.05, color='red', linestyle="--")
ax2.set_title('p-values over time')

#plt.show()