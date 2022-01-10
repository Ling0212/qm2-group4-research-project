# PEARSON CORRELATION COEFFICIENT IN PYTHON
# We first import the libraries we are going to use in order to compute Pearson'r: pandas, numpy and spicy.stats. Then, we import and read the data using pandas, stored in a .csv file. We will give as an example the code analysing the correlation between the Total Electricity Generation per Capita and Life Expectancy in Lebanon, from 1990 to 2019. 

import pandas as pd
import numpy as np
import scipy.stats

data = pd.read_csv("lebanon_data.csv")
data.head()

# We now define our x and y variables, corresponding to the columns Total Electricity Generation per Capita and Life Expectancy in the imorted .csv file. With spicy.stats library, we calculate the Pearson correlation coefficient as presented in the following lines of code:

x = data['Total Electricity Generation  per Capita (GWh)']
y = data['Life expectancy (years)']

scipy.stats.pearsonr(x, y)
