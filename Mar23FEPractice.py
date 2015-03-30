from __future__ import division
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import statsmodels.api as sm
import os

#main_dir = u'C:/Users/bcp17/OneDrive/Grad School/2015-Spring/Big Data/data/raw/'
main_dir = u'C:/Users/Brianprest/OneDrive/Grad School/2015-Spring/Big Data/data/raw/'
root = main_dir

paths = [root + v for v in os.listdir(root) if v.startswith("08_")]

df = pd.read_csv(paths[1], header=0, parse_dates=[1], date_parser=np.datetime64)
df_assign = pd.read_csv(paths[0], header=0)
df_assign.rename(columns={'assignment':'T'}, inplace=True)
"""Note: use notation from Allcott 2010"""

# Change date format
ym = pd.DatetimeIndex(df['date']).to_period('M') # 'M'=month, 'D',=day, etc.
df['ym'] = ym.values # integers. e.g. Jan 2015 = 540, Feb 2015 = 541. Like Stata's date format.
df['ym'].values.astype('datetime64[M]') # Converts integers back to dates.

# Monthly aggregation
grp = df.groupby(['ym','panid'])
df = grp['kwh'].sum().reset_index()

# Merge static variables
df = pd.merge(df,df_assign)
df.reset_index(drop=True, inplace=True)

# FE Model by Demeaning

"""demean function"""

# sends a dataframe (df), a list of its columns to demean (cols), and the individual identifier (panid)
# returns df with "cols" demeaned.
def demean(df, cols, panid):
    """
    inputs: df (pandas dataframe), cols (list of str of column names from df),
                    panid (str of panel ids)
    output: dataframe with values in df[cols] demeaned
    """

    from pandas import DataFrame
    import pandas as pd
    import numpy as np

    cols = [cols] if not isinstance(cols, list) else cols
    panid = [panid] if not isinstance(panid, list) else panid
    avg = df[panid + cols].groupby(panid).aggregate(np.mean).reset_index()
    cols_dm = [v + '_dm' for v in cols]
    avg.columns = panid + cols_dm
    df_dm = pd.merge(df[panid + cols], avg)
    df_dm = DataFrame(df[cols].values - df_dm[cols_dm].values, columns=cols)
    return df_dm

# set up data
df['log_kwh'] = df['kwh'].apply(np.log)
# df['log_kwh'] = np.log(df['kwh']) # also works
# period indicator (P=1 if post-treatment, i.e., after treatment has begun)
df['P'] = 0 + (df['ym']>541)
df['TP'] =df['T']*df['P'] # TreatmentGroup*DuringTreatment interaction.
# time fixed effects
mu = pd.get_dummies(df['ym'], prefix = 'ym').iloc[:,1:-1] 
# iloc: returns 2nd col (1) to second-to-last col ((-1)-1).
# we're dropping the first and last because to avoid the dummy variable trap
# and to ensure that constant+dummies are not perfectly collinear with time df['ym']. 

cols = ['log_kwh','TP','P']
panid = 'panid'
df_dm = demean(df, cols, panid)

y_dm = df_dm['log_kwh']

X_dm = df_dm[['TP','P']]
X_dm = sm.add_constant(X_dm)

# run model 
fe_model = sm.OLS(y_dm,pd.concat([X_dm,mu], axis =1))
fe_results = fe_model.fit()
print(fe_results.summary())






