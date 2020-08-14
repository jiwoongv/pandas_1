import pandas as pd
import numpy as np
import statsmodels.api as sm
import pylab as pl
import random

s2 = pd.Series([4, 7, -5, 3], index=['d','b','a','c'])
sdata = {'A':35000,'B':67000,'C':12000,'D':4000}
s1 = pd.Series([4, 7, -5, 3])
s3 = pd.Series(sdata)
s3.name = 'Salary'
s3.index.name = 'Names'
s3.index = ['E','F','G','H']

#Data Frame

data = {'name': ['A','A','A','B','B'], 'year':[2014, 2015,2016,2015,2016],
        'points':[1.5,1.7,3.6,2.4,2.9]}
df = pd.DataFrame(data)
df.index.name = 'Num'
df.columns.name = 'Info'

df2 = pd.DataFrame(data, columns=['year','name','points','penalty'], index=['one','two','three','four','five'])
df2['penalty'] = 0.5
df2['zeros'] = np.arange(5)

val = pd.Series([-1.2,-1.5,-1.7], index=['two','four','five'])
df2['debt'] = val

df2['net points'] = df2['points'] - df2['penalty']
df2['high points'] = df2['net points'] > 2

del df2['net points']
del df2['zeros']

df2.index.name = 'Order'
df2.columns.name = 'Info'
del df2['high points']
df2.loc['six',:] = [2013,'C',4.0,0.1,2.1]
df2.loc[df2['points'] > 3, 'penalty'] = 0

# DATA

df3 = pd.DataFrame(np.random.randn(6,4))
df3.columns = ['A','B','C','D']
df3.index = pd.date_range('20160701', periods=6)
df3['F'] = [1.0, np.nan, 3.5, 6.1, np.nan, 0]
df4 = df3.drop('F', axis=1)
df4 = pd.to_datetime('20160701')
df4 = df3.drop(pd.to_datetime('20160701'))

# Data Functions

data1 = [[1.4, np.nan], [7.1,-4.5],[np.nan, np.nan], [0.75,-1.3]]
df5 = pd.DataFrame(data1, columns=['one','two'], index=['a','b','c','d'])

df6 = pd.DataFrame(np.random.randn(6,4), columns=['A','B','C','D'], index=pd.date_range('20160701', periods=6))

print(df6['A'].cov(df6['B']))