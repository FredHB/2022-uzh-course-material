import pandas as pd
import numpy as np

unemp = pd.Series([[3.5, 2.4, 3.8], [2.3]])
print(unemp)

unemp = pd.DataFrame(np.random.randint(0,10, size = (100,5)))
print('head:\n', unemp.head())

unemp

unemp = pd.Series([3.1,2,1], index = ['Cali', 'DC', 'Florida'])
print(unemp.head())

unemp = {'Cali':1, 'DC':2, 'Florida':3.3}
print(unemp)

df = pd.DataFrame({'states' : ['Cali', 'DC', 'Florida'], 'unemp' : [3.1,2,1]})
print(df)

print(
	df.loc[[1],['unemp','states']],
	df['unemp'] > 3,
	df[df['unemp'] > 3],
	df.shape,len(df), np.array(df),
	sep = '\n\n'
	)

## The interesting bit: reading-in data
