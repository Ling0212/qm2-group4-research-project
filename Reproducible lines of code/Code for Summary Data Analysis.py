# SUMMARY STATISTICS IN PYTHON
# We obtain all the values we need to build our summary statistics table using pandas, numpy and spicy libraries.
# We need to successively select the values for each variable, for either Jordan's or Lebanon's data contained in the corresponding csv file. In other words, we consecutively select one column of the csv file.
# The following lines of code allow us to compute for each variable the summary statistics values. We present for example the code used in the case of the Total Energy Supply per capita in Leabanon, from 1990 to 2019.

import pandas as pd
import numpy as np
from scipy import stats

data=pd.read_csv('lebanon_data.csv', delimiter=',')
TES=data['Total Energy Supply (TJ) per capita']

mean=np.mean(TES)
median=np.median(TES)
mode=stats.mode(TES)
variance=np.var(TES)
standard_deviation=np.std(TES)
minimum=np.amin(TES)
maximum=np.amax(TES)
range=maximum-minimum
lower_quartile=np.quantile(TES,0.25)
upper_quartile=np.quantile(TES,0.75)
interquarile_range=upper_quartile-lower_quartile
lower_tukeyfence=lower_quartile-1.5*interquarile_range
upper_tukeyfence=upper_quartile+1.5*interquarile_range

print(mean)
print(median)
print(mode)
print(variance)
print(standard_deviation)
print(minimum)
print(maximum)
print(range)
print(lower_quartile)
print(upper_quartile)
print(interquarile_range)
print(lower_tukeyfence)
print(upper_tukeyfence)
