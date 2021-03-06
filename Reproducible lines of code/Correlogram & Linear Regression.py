# CORRELOGRAMS IN PYTHON
# We first import and read the data (using pandas) we intend to plot in a correlogram, stored in a .csv file.

import pandas as pd
import numpy as np
pd.read_csv('lebanon_data.csv', delimiter=',')

# With pandas, we have here imported and read Lebanon's data saved as a .csv file. For Jordan's data, we store it in a csv file and then read it in the same manner.

# Working with matplotlib.pyplot and seaborn libraries, we now plot the correlogram thanks to the following lines of code:

import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('lebanon_data.csv', delimiter=',')

sns.pairplot(data, kind='reg', diag_kind='kde', height=5)
plt.show()

# In order to simplify the code, we choose to name the data included in the .csv file 'data'.


# SIMPLE LINEAR REGRESSION ANALYSIS IN PYTHON
# To code the linear regression analysis method, we use a diversity of libraries in python: pandas, numpy, matplotlib.pyplot, sklearn.linear_model, sklearn.metrics and statsmodels.api.
# We first import these libraries and download our data from the chosen .csv file. As an example, we choose to apply linear regression analysis to Total Electricity Generation per Capita and Life Expectancy, from 1990 to 2019 in Lebanon. We will then assess the revelancy of this model.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm

data = pd.read_csv("lebanon_data.csv")

X = data['Total Electricity Generation  per Capita (GWh)'].values.reshape(-1,1)
y = data['Life expectancy (years)'].values.reshape(-1,1)

reg = LinearRegression()
reg.fit(X, y)

# We now compute the linear relationship that modelise the correlation between our two variables, using the following code:

print(reg.coef_[0][0])
print(reg.intercept_[0])

print("The linear model is: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))

# We may also visualise this precise linear model in a scatter plot:

predictions = reg.predict(X)

plt.figure(figsize=(16, 8))
plt.scatter(
    data['Total Electricity Generation  per Capita (GWh)'],
    data['Life expectancy (years)'],
    c='black'
)
plt.plot(
    data['Total Electricity Generation  per Capita (GWh)'],
    predictions,
    c='blue',
    linewidth=2
)
plt.xlabel("Total Electricity Generation  per Capita (GWh)")
plt.ylabel("Life expectancy (years)")
plt.show()

# Afterwards, statsmodels.api library allows us to generate a 'regression results' table including the R-squared values and p-values. These respectively evaluate the strengh and significance of the model.

X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())

# Nevertheless, this table gives an approximate p-value. As a means to calculate a precise p-value for the model, we add the next line of code:

print(est2.pvalues)
