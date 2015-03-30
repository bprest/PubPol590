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

df_kwh = pd.read_csv(root + kwh, header=0)
# merge kwh to 
#pd.merge

#df = zip(selection_control, selection_A1, selection_A3, selection_B1, selection_B3)