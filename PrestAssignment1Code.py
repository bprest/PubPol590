from pandas import Series, DataFrame
import pandas as pd
import numpy as np

#  3: Assign directories.
# Two user paths. One for my home machine, the other for my office machine.
userpath = "Brianprest"
# sourcepath = "bcp17"
main_dir = "/Users/" + userpath + "/OneDrive/Grad School/GitHub/PubPol590/"
txtpath =  "data/raw/sample_data_clean.csv"

# This is for the larger set of data. Saving this code for later.
#main_dir = "/Users/" + sourcepath + "/Google Drive/THE RAGDOLLS_ 590 Big Data/CER_Data/"
#txtpath =  "File1.txt"

# 4: Read data. Two ways to check consistency.
data1 = pd.read_csv(main_dir+txtpath)
data2 = pd.read_table(main_dir+txtpath,sep=",")

# Check that all cells are equal.
d=(data1==data2)
pd.value_counts(d['panid'])
pd.value_counts(d['date'])
pd.value_counts(d['consump'])

type(data1)
list(data1)
cons = data1.consump
cons2 = data1['consump']

d=(cons==cons2)
pd.value_counts(d)

type(cons)

# 5: Extract Rows 60-99.
data1[60:100]

# 6: Rows where consump>30.
# I was unclear of the question being asked: is it A: "extract all rows that have average consumption
# per hour over 30 kwh?" or B: "extract all rows that have total daily consumption over 30 kwh".
# Since I wasn't clear, I answer both questions. If it's A there are no such rows. If it's B,
# there are 110 such rows.
#
# I presume that the reported figures are average daily load (e.g., the first row's
# value of 0.93 represents that meter 1 consumed 0.93 kwh per hour on average on Jan 1, 2013.
#
# There are no meters that consumed 30 kwh/h on any day. The max daily average 
# consumption is 3.96 kw.
data1[data1.consump>30]
max(data1.consump)

# If the question is instead, how many homes consumed 30 kwh total over the 
# course of a day, then there are 110 such observations:
highload = data1[data1.consump*24>30]
highload
max(data1.consump)*24
min(highload.consump)*24

