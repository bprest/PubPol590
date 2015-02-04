from __future__ import division  # imports the division capacity from the future version of Python
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
git_dir = "C:/Users/bcp17/OneDrive/Grad School/GitHub/PubPol590"
csv1="small_data_w_missing_duplicated.csv"
csv2 = "sample_assignments.csv"

# Import
df1 = pd.read_csv(os.path.join(main_dir,csv1), na_values=['-','NA'])
df2 = pd.read_csv(os.path.join(main_dir,csv2))

# clean df1
df1 = df1.drop_duplicates()
df1 = df1.drop_duplicates(['panid','date'], take_last=True)

# clean df2
df2=df2[[0,1]] # contains identifiers telling us which panids are in treatment or control.

# Copying dataframes
df3 = df2 # references df3 to the object of df2, even if df2 changes (doesn't take extra space in memory).
df4 = df2.copy() # copies dataframe as a separate object (takes extra space in memory).

# Replacing data
df2.group.replace(['T','C'], [1,0])
df2.group = df2.group.replace(['T','C'], [1,0]) # replaces T/C with dummy variable.

print df3 # Note that our replacement of T/C with 1/0 in df2 is transferred to df3 as well.

# Merging
# So we want to merge df2 (small set, one obs per panid) to the panel in df1 (many obs per panid)
mergeddf = pd.merge(df1, df2) # many-to-one using intersection. automatically finds the common keys (in this case, just "panid")
mergeddf.group.mean() # half of the panids are treated.

pd.merge(df1,df2, on = ['panid']) # specify key to merge on.

pd.merge(df1, df2, on = ['panid'], how = 'inner') 
# inner-join: returns intersection of keys. only includes panids that appear in both dataframes (here, 1-4)

pd.merge(df1, df2, on = ['panid'], how = 'outer') 
# outer-join: returns union of keys. includes any panids that appear in either (here, 1-5, where 5 appears in the smaller set).

df5 = pd.merge(df1, df2, on = ['panid'], how = 'inner') 

# Combining and Stacking
# Column Binds and Row Binds 
df2
df4
# Row Bind ("Stack")
pd.concat([df2, df4]) # by default, binds on rows (stacks/appends).
pd.concat([df2, df4], axis = 0 ) # same thing. bind on axis 0, ie rows
# Note that the index repeats from the original database.
pd.concat([df2, df4], axis = 0, ignore_index = True) # Resets the index.
# Col Bind
pd.concat([df2, df4], axis = 1 ) 


