from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
git_dir = "C:/Users/bcp17/OneDrive/Grad School/GitHub/PubPol590"
csv_file="sample_data_clean.csv"
os.chdir(main_dir) #
# %reset will clean. need to confirm it with "y"

# For Loops
df = pd.read_csv(os.path.join(main_dir,csv_file))
list1 = range(10,15)
list2 = ['a','b','c']
list3 = [1, 'a', True]

for v in list3:
    print(v,type(v)) # need a tab within a for loop!!!

list1 = range(10,15)
list4 = []
list5 = []
for v in list1:
    v2 = v**2
    print(v,v2)
    list5.append(v2)
    #list4.extend([v2]) # note: input to extend() must be a list
print(list5)

# can do this in a single line:
print [v**2 for v in list1]
list6 = [v**2 < 144 for v in list1]
print list6

# iterating using enumerate
list7 = [ [i,float(v)/2] for i, v in enumerate(list1)] # counts from i=1,2,3...len(list1) and does each evaluation
# need float so that the result is not an integer.
print list7

s1= df['consump']
[v>2 for v in s1]
# iteritems will return the index value, which is useful if your index is not numeric or not 0,1,2...
[[i,float(v)*.3] for i, v in s1.iteritems()] # anonymous function (i.e., no inputs)

# iterate through a dataframe
[v for v in df] # cuts only through first layer (the key references are first)
[df[v] for v in df] # finds keys, and for each key, returns df[key]

[[i, v] for i, v in df.iteritems()]

len([v for v in df]) # number of columns
len(df) # number of rows
len(list(df))
df.ndim()
	