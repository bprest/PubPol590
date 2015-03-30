from __future__ import division  # imports the division capacity from the future version of Python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import xlrd
import time
import csv
import matplotlib.pyplot as plt
from dateutil import parser # ensures dates are parsed correctly
from scipy.stats import ttest_ind
from scipy.special import stdtr

print(time.ctime())
start = time.time()
main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
root = main_dir

# import

df = pd.read_csv(root+"/sample_30min.csv", header=0,parse_dates=[1], date_parser=parser.parse)

df_assign = pd.read_csv(root+"/sample_assignments.csv", usecols = [0,1])

# merge
df = pd.merge(df, df_assign)

# turn date/time to year/month/etc variables
df['year'] = df['date'].apply(lambda x: x.year) 
df['month'] = df['date'].apply(lambda x: x.month)
df['day'] = df['date'].apply(lambda x: x.day)
df['ymd'] = df['date'].apply(lambda x: x.date())
# lambda functions allow you to apply any function to subobjects within an object (eg elements of a vector)
# we need this because df['date'] is a Series object, so you can't use the function ".year" on a Series object.
# But you can iteratively apply it.
#grp = df.groupby(['year','month','day','panid','assignment'])
grp = df.groupby(['ymd','panid','assignment'])

df1 = grp['kwh'].sum().reset_index()

# pivot from long to wide
## step 1: create column names for wide data
# create string names and denoate consumption and date

# use ternery expression:[true-expr(x) if condition else false-expr(x) for x in list]
# for each x in list, check the condition. if true, return true-expr(x).
# a for loop combined with an if statement, but in only one line.
# so lets create a new Series that contains the name of the value's destination column
#df1['day_str'] = ['0' + str(v) if v < 10 else str(v) for v in df1['day']] # add a 0 in front of single-digit days.
#df1['kwd_ymd'] = 'kwd_' + df1.year.apply(str) + "_" + df1.month.apply(str) + "_" + df1.day.str

df1['kwh_ymd'] = 'kwh_' + df1['ymd'].apply(str)
# now we have column names

# pivot
df1_piv = df1.pivot('panid','kwh_ymd','kwh') # pivot(i,j,v) where i's are rows and j's are cols, and v are the values that go wide.
# but we lost time invariant stuff (treatment/control)
# note: panid is now the first row. and the col name for the first column is "kwh_ymd"
df1_piv.reset_index(inplace=True)
df1_piv.columns.name = None # gets rid of top left thing

df2 = pd.merge(df_assign,df1_piv) # by putting df_assign first, it puts the assignment data at the beginning of the columns instead of the end.

# export data for regressions
df2.to_csv(root+"/07_kwh_wide.csv", sep=",", index=False)