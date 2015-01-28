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
print str2 + str3

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

## lists. [] lists can be changed, tuples cannot. Hence the focus on lists.
list1 = []
print list1
list2 = [1,2,'hey',4,5,6]
print list2
print list2[2]
list2[5]
list2[0] = 88
print list2

# tuples, () can't change them
tup1 = (8,3,74)
print tup1[2]
tup1(3)=36
print tup1

# can convert things
list3 = list(tup1)
tup2 = tuple(list2)

# can extend and append lists
# append sticks the vector [3,'joe'] into the last element I.e. the last element of list2 is itself a 2x1 vector
list2 = [1,2,19]
list2.append([3,'joe'])
print len(list2)
print list2

# extend takes the new vector and sticks it on the end of the existing list.
list4 = [8, 3, 90]
list4.extend([6,'bp'])
print len(list4)
print list4

# Converting lists to series and dataframes
list5 = range(5,10) # range(n,m) gives a list counting from n to m-1
print list5
list6 = range(5) # from 0 to n-1
print list6
list7 = ['q','r','s','t','u']
print list7

## list to Series (Series being a pandas object)
fivetonine = Series(list4)
letters = Series(list7)
print fivetonine
print letters



