from __future__ import division  # imports the division capacity from the future version of Python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
import xlrd
import time
import csv
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy.stats import ttest_ind
from scipy.special import stdtr

print(time.ctime())
start = time.time()
main_dir = u'C:/Users/Brianprest/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
root = main_dir

df = pd.read_csv(root+"/07_kwh_wide.csv", header=0)

# Linear Probability Model
df['T'] = (df['assignment']=='T') # Returns boolean column
df['T'] = 0 + (df['assignment']=='T') # Returns 0/1 variable

# Set up data
# get X matrix (RHS)
kwh_cols = [v for v in df.columns.values] # df.columns returns Index of names of columns. ".values" gives a list of the names of the columns
# so this returns an array of the columns
kwh_cols = [v for v in df.columns if v.startswith('kwh')] 
kwh_cols = [v for v in df.columns.values if v[:3]=='kwh'] # same thing

# pretend treatment occurred at 1/4/2015. So we test for equiprobability based on kwh before then.
# how do find dates before 1/4/2015?
# Test
cols =     [v for v in kwh_cols if v<'kwh_2015-01-04'] # but this is bad since it will is based on sorting strings. e.g. '4'>'04'
kwh_cols = [v for v in kwh_cols if int(v[-2:])<4] # grab day (last 2 digits), convert to integer, see if it's earlier than 4.

# set up y and X
y = df['T']
X = df[kwh_cols]
X = sm.add_constant(X) # adds "const". Note that this will throw an error if there is already a var name const.
#dfconst = DataFrame(range(0,31))
#dfconst.columns = ['const']
#sm.add_constant(dfconst)

ols_model = sm.OLS(y,X) # linear prob model.
ols_results = ols_model.fit() # fitted values
print(ols_results.summary())
