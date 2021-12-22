Here, we perform the same quantitative techniques on the data collected for Jordan and adopt the same approaches for analysing the outcomes.

# Correlation & Linear regression 

<img width="746" alt="correlogram (Jordan)" src="https://user-images.githubusercontent.com/93497630/146651216-279d3c69-846b-40d5-9564-86edbdd0efad.png">

*Correlogram showing Jordan's data with linear regression model performed on each subplot*

Table: Summary of correlation coefficients and regression statistics  
<img width="733" alt="Screen Shot 2021-12-19 at 1 36 45 PM" src="https://user-images.githubusercontent.com/93497630/146676861-8f0518a9-a40b-42de-b877-a32cecfa9908.png">

## Analysis of statistical values

Primarily observing the scatterplots depicted in subplots B and F, we can assume that there is no linear or monotonic relationship existing between the Total Energy Supply (TES) per capita and Life Expectancy, as well as between the Total Electricity Generation (TEG) and Expected Years of Schooling. The corresponding Pearson and Kendall tau coefficients confirm our first review, since these values are way below the significance level set at 0.5.


Subplot A visualises the correlation between the TES per capita and the Gross National Income (GNI) per capita, which at first appears to follow a linear relationship. With a Pearson coefficient of 0.63 and a low p-value of 0.0002, the model found is indeed linear and significantly affirmed. However, the Kendall tau and R-squared value prove that the relation is not monotonic and strong.

The three subplots C, D and E illustrate the most relevant correlations to examine in our complementary analysis concerning Jordan data, from 1990 to 2019. They respectively portray the relationship between the TES per capita and expected years of schooling, the TEG per capita and the GNI per capita, and finally between the TEG per capita  and life expectancy. According to Pearson coefficients, Kendall tau, p-values and R-squared values, we establish three strong and significant linear-monotonic relationships between our variables. Indeed, all the coefficients and statistical values calculated respect their proper significance level or interval.  


# Clustering graphs & Analysis
![TES   GNI (Jordan)](https://user-images.githubusercontent.com/93497630/146656234-21d0724c-191b-4b8c-bb05-4d6d2371fd78.png)

*Figure 1: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and GNI per capita – Coloured by Cluster*

<img width="1353" alt="Capture d’écran 2021-12-22 à 23 46 25" src="https://user-images.githubusercontent.com/93881303/147163504-1eb35e0b-3097-4f6a-83e7-023919c6cf24.png">

![TES   life (Jordan)](https://user-images.githubusercontent.com/93497630/146656237-b63c07d4-099a-495d-92d0-5042ef171ecf.png)

*Figure 2: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and life expectancy at birth – Coloured by Cluster*

![TES   school (Jordan)](https://user-images.githubusercontent.com/93497630/146656239-1c5baa56-0606-45fc-b406-f1c4e8876bca.png)

*Figure 3: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and expected years of schooling – Coloured by Cluster*

![TEG   GNI (Jordan)](https://user-images.githubusercontent.com/93497630/146656245-9027f778-5449-4ed4-82c9-26b86387dd02.png)

*Figure 4: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and GNI per capita – Coloured by Cluster*

![TEG   life (Jordan)](https://user-images.githubusercontent.com/93497630/146656247-439f33c4-0789-4f63-8389-66a9596e581b.png)

*Figure 5: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and life expectancy at birth – Coloured by Cluster*

![TEG   school (Jordan)](https://user-images.githubusercontent.com/93497630/146656248-dac232c0-5e67-48db-8ce8-88cf41caad14.png)

*Figure 6: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and expected years of schooling – Coloured by Cluster*

## [put at the bottom of the webpage]

The code used to plot the correlogram can he found here. (give a link to the GitHub page with the lines of code on it)
<img width="620" alt="Capture d’écran 2021-12-09 à 4 29 44 PM" src="https://user-images.githubusercontent.com/93673467/145436543-87e2fba6-0ef3-4d3d-a08f-4b25db372135.png">

The code used to calculate the correlation coefficients and regression statistics can be found here. (give a link to the GitHub page with the lines of code on it)

The code used to calculate the Kendall tau coefficients can be found here.

The code used to plot clustering graphs and calculate Silhouette scores can be found here.
