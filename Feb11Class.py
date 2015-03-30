from __future__ import division  # imports the division capacity from the future version of Python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import xlrd
import time
import csv

print(time.ctime())
start = time.time()
#main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
main_dir = u'C:/Users/Brianprest/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
pathlist = [os.path.join(main_dir,v) for v in os.listdir(main_dir) if v.startswith("file")]
df = pd.concat([pd.read_csv(v, sep = ",", names = ['panid','time','kwh']) for v in pathlist], ignore_index = True)

assign = pd.read_csv(main_dir + "/sample_assignments.csv", sep = ",", usecols = [0,1])
#assign = assign[[0,1]]

df = pd.merge(df,assign)

grp1 = df.groupby(['assignment'])
grp1.mean()
grp1.apply(np.mean)
gd1 = grp1.groups # with big data sets, this will be huge, so don't try to display it.
# Note: this is a dictionary.
gd1.keys() # displays keys in the dict
gd1.values()
gd1['C'] 
gd1.values()[0] # a list. returns the same thing, since 'C' is the first key.
gd1.values() 
gd1.viewvalues() # same thing, but easier to read ("transposed")

grp1.groups.keys() # shows the keys in grp1.

# iteration properties of the dictionary
gd1.itervalues()
[v for v in gd1.itervalues()] # prints values in a loop
gd1.values() # same thing
[v for v in gd1.iterkeys()] # prints values in a loop
gd1.keys() # same thing
[v+'X' for v in gd1.iterkeys()] # concatenates an X onto the keys

[(k,v) for k,v in gd1.iteritems()] # note: (.,.) is a tuple
gd1

## split and apply
grp1.mean()
grp1['kwh'].mean()

## split and apply: panel/timeseries data

grp2 = df.groupby(['assignment','time'])
gd2 = grp2.groups
gd2 
# Note: now the cross of assignment and time is a single key. 
# E.g. ('C','10-Jan') is a single key, corresponding to all control observations on Jan 10th.
grp2['kwh'].mean()
grp2['kwh'].mean().unstack('assignment')

df['kwh'][[0,90,120]].mean()  # from the dict, we can see that these rows correspond to control on January 1st.

type(grp2['kwh'].mean().unstack('assignment')) # a DF

# Testing for Balance
from scipy.stats import ttest_ind
from scipy.special import stdtr


# example
a = [1, 4, 9, 2]
b = [1, 7, 8, 9]

t,p = ttest_ind(a, b, equal_var=False)
grp = df.groupby(['assignment','time'])

trt = {k[1]: df.kwh[v].values for k,v in grp.groups.iteritems() if k[0]=="T"}
# iteritems returns a key (k) and a value (v). For each such key, there are sub-elements. 
# E.g., one key is ("T","10-Jan"), so the first element of this key is "T". So k[0] returns the
# first element of that key, or "T".
# So it only grabs the keys where the first element is "T". It also grabs the associated 
# values (v).
# For each of these, assign k[1] (the date) as the key for the relevant values.
ctrl = {k[1]: df.kwh[v].values for k,v in grp.groups.iteritems() if k[0]=="C"}

keys = trt.keys()

diff = {k: (trt[k].mean() - ctrl[k].mean()) for k in keys}
# for each key, calculates difference in means.
tstats = {k: float(ttest_ind(trt[k],ctrl[k], equal_var = False)[0]) for k in keys}
pvals = {k: float(ttest_ind(trt[k],ctrl[k], equal_var = False)[1]) for k in keys}
t_p = {k: (tstats[k], pvals[k]) for k in keys}






grp1['kwh'].apply(np.mean)
grp1['kwh'].mean() # local function, faster than calling an external package like np
%timeit -n 100 groups1['kwh'].apply(np.mean) # times how long it takes to do this.

groups2 = df.groupby(['time', 'assignment']) # groups by cartesian product of options
groups2 = df.groupby(['assignment', 'time']) # note: order matters in terms of how it outputs things

groupmean = groups2['kwh'].mean()

gp_unstacked = groupmean.unstack('assignment')