from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os
data=0

main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw'
git_dir = "C:/Users/bcp17/OneDrive/Grad School/GitHub/PubPol590"
csv_file="sample_data_clean.csv"
#cd 'main_dir'

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
#tup1(3)=36 # won't work
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

# create DataFrames from lists or series. Note that merging two series requires the series be the same length.
list8 = range(60,65)
print list5
print list7
print list8
zip1 = zip(list5,list7,list8)
df1 = DataFrame(zip1)
print df1
df1[1] # 2nd column
df2 = DataFrame(zip1,columns=['row1','orange',':)']) # here, the column labels, 2, 'orange', ':)', are called "Keys".
df2
df2['orange'] # orange column
df2[3:4] # For rows, you have to use the colon bit.
df2[['orange',':)']][3:5] # df2[listofkeys][startrow:endrow+1], where listofkeys=['orange',':)']
df2[range(1,3)][3:5] # cols 1-2, rows 3-4.
df2
print len(fivetonine)
print len(letters)
# make dataframe using dict notation
print list4
print list6
df4= DataFrame({ ':(' : list4, 9  : list6}) # DataFrame({col1name : col1list, col2name : col2list})
df4

# stacking Series
df5 = pd.concat([fivetonine, letters]) # concatenate (stack) lists, but it messes up the indices.

df5

