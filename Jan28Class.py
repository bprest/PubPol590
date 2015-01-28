from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
data=0
#main_dir = "C:\Users\bcp17\OneDrive\Grad School\2015-Spring\Big Data\data\raw"
#git_dir = "C:\Users\bcp17\OneDrive\Grad School\GitHub\PubPol590"
main_dir = "C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw"
git_dir = "C:/Users/bcp17/OneDrive/Grad School/GitHub/PubPol590"
csv_file="sample_data_clean.csv"

# OS Module
data = pd.read_csv(os.path.join(main_dir,csv_file))
print data

# Python Data Types

# Strings
str1 = "hello comp"
str2 = 'single quotes work, too'
str3 = u'eep'

print type(str1)
print type(str2)
print type(str3)
# u is for unicode, which is a universallly readable text type. (e.g stata and python treat strings differently, but unicode is universal

# numeric
int1 = 10
float1 = 20.567
long1 = 986734754

##
bool1 = True
bool2 = False
zero = 0
bool2 = bool(zero)
print zero
print bool2





print str2 + str3
