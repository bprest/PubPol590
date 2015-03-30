from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import time
import os

print(time.ctime())
start = time.time()
main_dir = u'C:/Users/Brianprest/OneDrive/Grad School/2015-Spring/Big Data/data/raw/'
#main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw/'
root = main_dir
allocation = "allocation_subsamp.csv"
kwh = "kwh_redux_pretrial.csv"

df_assign = pd.read_csv(root + allocation, header=0)

control_ids = df_assign.ID[(df_assign['tariff']=='E') & (df_assign['stimulus']=='E')]
A1_ids = df_assign.ID[(df_assign['tariff']=='A') & (df_assign['stimulus']=='1')]
A3_ids = df_assign.ID[(df_assign['tariff']=='A') & (df_assign['stimulus']=='3')]
B1_ids = df_assign.ID[(df_assign['tariff']=='B') & (df_assign['stimulus']=='1')]
B3_ids = df_assign.ID[(df_assign['tariff']=='B') & (df_assign['stimulus']=='3')]

np.random.seed(seed=1789)

selection_control = np.random.choice(control_ids,size=300,replace=False).tolist()
selection_A1 = np.random.choice(A1_ids,size=150,replace=False).tolist()
selection_A3 = np.random.choice(A3_ids,size=150,replace=False).tolist()
selection_B1 = np.random.choice(B1_ids,size=50,replace=False).tolist()
selection_B3 = np.random.choice(B3_ids,size=50,replace=False).tolist()

selection_all = pd.DataFrame(selection_control+selection_A1+selection_A3+selection_B1+selection_B3, columns=["ID"])

df = pd.read_csv(root + kwh, header=0, parse_dates=[2], date_parser=np.datetime64)
# Merge on selected IDs
df = pd.merge(selection_all,df)
# Generate Month/Year variable
df['ym'] = pd.DatetimeIndex(df['date']).to_period('M').values # 'M'=month, 'D',=day, etc.

# Sum monthly consumption
monthgrp = df.groupby(['ID','ym'])
df = monthgrp['kwh'].sum().reset_index()

# Pivot to wide on monthly kwh
df['kwh_ym'] = 'kwh_' + df.ym.apply(str)

df_piv = df.pivot('ID','kwh_ym','kwh') # i,j,v. i is rows. j is columns, v is values to go in j columns.
df_piv.reset_index(inplace=True)
df_piv.columns.name = None # gets rid of top left thing

# Merge with treatment assignment
df_piv = pd.merge(df_assign,df_piv)

# Note that "code" is a constant =1 here, so we don't need to add a constant. just rename code "constant".
df_piv.rename(columns ={'code':'constant'}, inplace=True)

# Set up X variables
X_E  = df_piv[(df_piv.tariff=='E') & (df_piv.stimulus=='E')][[1]+range(4,10)] # columns 1 plus 4 thru 9
X_A1 = df_piv[(df_piv.tariff=='A') & (df_piv.stimulus=='1')][[1]+range(4,10)]
X_A3 = df_piv[(df_piv.tariff=='A') & (df_piv.stimulus=='3')][[1]+range(4,10)]
X_B1 = df_piv[(df_piv.tariff=='B') & (df_piv.stimulus=='1')][[1]+range(4,10)]
X_B3 = df_piv[(df_piv.tariff=='B') & (df_piv.stimulus=='3')][[1]+range(4,10)]

# Set up Y variable: 0 if control, 1 if treatment
y_E  = pd.DataFrame([0]*len(X_E), columns=['trt'])
y_A1 = pd.DataFrame([1]*len(X_A1), columns=['trt'])
y_A3 = pd.DataFrame([1]*len(X_A3), columns=['trt'])
y_B1 = pd.DataFrame([1]*len(X_B1), columns=['trt'])
y_B3 = pd.DataFrame([1]*len(X_B3), columns=['trt'])

# Run logit.
logit_model_A1 = sm.Logit(y_E.append(y_A1).reset_index(drop=True),X_E.append(X_A1).reset_index(drop=True))
logit_model_A3 = sm.Logit(y_E.append(y_A3).reset_index(drop=True),X_E.append(X_A3).reset_index(drop=True))
logit_model_B1 = sm.Logit(y_E.append(y_B1).reset_index(drop=True),X_E.append(X_B1).reset_index(drop=True))
logit_model_B3 = sm.Logit(y_E.append(y_B3).reset_index(drop=True),X_E.append(X_B3).reset_index(drop=True))

logit_results_A1 = logit_model_A1.fit()
logit_results_A3 = logit_model_A3.fit()
logit_results_B1 = logit_model_B1.fit()
logit_results_B3 = logit_model_A3.fit()

# Print results
print(logit_results_A1.summary())
print(logit_results_A3.summary())
print(logit_results_B1.summary())
print(logit_results_B3.summary())
