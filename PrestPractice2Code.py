from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

#all = [var for var in globals() if var[0]!="_"]
#for var in all:
#    del globals()[var]


main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
git_dir = "C:/Users/bcp17/OneDrive/Grad School/GitHub/PubPol590"
csv_file="small_data_w_missing_duplicated.csv"

#### Part 1
df = pd.read_csv(os.path.join(main_dir,csv_file))
df.head(7)

df['consump'].head(10).apply(type) 
## applies a function to this subset. here, it applies the type functino, which returns the type. They're strings!!! Let's convert.

# re-import
missing = ['.','NA','NULL','','-']
df = pd.read_csv(os.path.join(main_dir,csv_file),na_values = missing)
df['consump'].head(10)
df['consump'].head(10).apply(type) 

#### Part 2
# missing data types: None, np.nan
# None is standard Python missing value. This is an object, so takes more memory
# np.nan is not a number from NumPy. This is just a variable.
type(None)
type(np.nan)
df.isnull()
np.isnan(df['consump'])
df.count()
df_fill = df.fillna(9999)
df_fill.count()

df.dropna(axis = 0 , how='any') # drop rows with any missings
df.dropna(axis = 1, how='any') # drop cols with any missings
df.dropna(axis = 0 , how='all') # rows that are entirely missing

# See rows with missing data
df.dropna(how = 'all')

# rows is an indicator for whether we're missing consumption
rows = df['consump'].isnull()

df[rows]

# Part 2: Duplicated values
df.count()
df[df.duplicated()].count()
df[df.duplicated()==False].count()
# **2
df_nodupes = df[df.duplicated()==False]

# Part 3: Extract rows with missing consump.
missing_cons = np.isnan(df_nodupes.consump)
df_nodupes_missing = df_nodupes[missing_cons] # rows missing cons
df_nodupes_nonmissing = df_nodupes[~missing_cons] # rows having cons

# Part 4: Check for duplicate dates and drop missings.
df_nodupes_nonmissing_nodupdates = df_nodupes_nonmissing[~df_nodupes_nonmissing.duplicated(['panid','date'])] # check for duplicated dates on cleaned data.
df_nodupes_nonmissing_nodupdates = df_nodupes_nonmissing_nodupdates[~np.isnan(df_nodupes_nonmissing_nodupdates.consump)] # clean out any NaNs for consump.

df_nodupdates = df[~df.duplicated(['panid','date'])] # check for duplicated date on original data.
df_nodupdates = df_nodupdates[~np.isnan(df_nodupdates.consump)] # clean out any NaNs for consump.

# Are these matrices identical?
(df_nodupdates==df_nodupes_nonmissing_nodupdates).sum() # count number of times they match
(df_nodupdates==df_nodupes_nonmissing_nodupdates).count() # count size of matrix
(df_nodupdates==df_nodupes_nonmissing_nodupdates).sum()==(df_nodupdates==df_nodupes_nonmissing_nodupdates).count() # See if #matches = size of matrix.
# Yup they're identical.

# Part 5: Mean Consumption = 0.917 kwh.
df_nodupdates.consump.mean()






