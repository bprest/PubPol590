# Tips for assignment
from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import time
import os

df_alloc = pd.read_csv(yadayada)
ids = df_alloc['ID']
tariffs = [v for v in pd.unique(df_alloc['tariff']) if v!='E']
stimuli = [v for v in pd.unique(df_alloc['stimulus']) if v!='E']
# similar for stimulus.

for i in tariffs:
        for j in stimuli:
                n = 150 if i=='A' else 50
                temp = np.random.choice(ids[(df_alloc['tariff']==i) & (df_alloc['stimulus']==j)], n, False)
                EE = np.hstack((EE,temp)) # horizontal stack

s