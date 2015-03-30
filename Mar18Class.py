from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import time
import os

print(time.ctime())
start = time.time()
main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw/'
root = main_dir

paths = [root + v for v in os.listdir(root) if v.startswith("08_")]

df = pd.read_csv(paths[1], header=0, parse_dates=[1], date_parser=np.datetime64)
df_assign = pd.read_csv(paths[0], header=0)

df['year'] = df['date'].apply(lambda x: x.year)
df['month'] = df['date'].apply(lambda x: x.month)

grp = df.groupby(['year','month','panid'])
df = grp['kwh'].sum().reset_index()

# pivot
df['mo_str'] = ['0' + str(v) if v<10 else str(v) for v in df['month']] # add leading 0 to single-digit months

df['kwh_ym'] = 'kwh_' + df.year.apply(str) + "_" + df.mo_str.apply(str)

df_piv = df.pivot('panid','kwh_ym','kwh') # i,j,v. i is rows. j is columns, v is values to go in j columns.

df_piv.reset_index(inplace=True)
df_piv.columns.name = None # gets rid of top left thing

df = pd.merge(df_assign,df_piv) 

#df['male'] = 0 + (df.gender=='M')
df = pd.get_dummies(df, columns=['gender']) # by default, makes dummies for all categorical variables. or you restrict it to certain columns
# good for time fixed effects, which uses a lot of dummies
df.drop(['gender_M'], axis=1, inplace=True)

kwh_cols = [v for v in df.columns.values if v.startswith('kwh')]
kwh_cols = [v for v in kwh_cols if int(v[-2:]) < 4]
cols = ['gender_F'] + kwh_cols

y = df['assignment']
X = df[cols]
X = sm.add_constant(X)

logit_model = sm.Logit(y,X)
logit_results = logit_model.fit()

print(logit_results.summary())
