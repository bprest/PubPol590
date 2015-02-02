from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

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

# Part 2: Duplicated values
df_nodupes = df[df.duplicated()==False]

# Part 3: Extract rows with missing consump.
missing_cons = np.isnan(df_nodupes.consump)
df_nodupes_missing = df_nodupes[missing_cons] # rows missing cons
df_nodupes_nonmissing = df_nodupes[~missing_cons] # rows having cons

# Part 4: Check for duplicate dates and drop missings.
df_nodupes_nonmissing_nodupdates = df_nodupes_nonmissing[~df_nodupes_nonmissing.duplicated(['panid','date'])] # check for duplicated dates on cleaned data.
df_nodupes_nonmissing_nodupdates = df_nodupes_nonmissing_nodupdates[~np.isnan(df_nodupes_nonmissing_nodupdates.consump)] # clean out any NaNs for consump.

# Part 5: Mean Consumption = 0.917 kwh.
print df_nodupes_nonmissing_nodupdates.consump.mean()






