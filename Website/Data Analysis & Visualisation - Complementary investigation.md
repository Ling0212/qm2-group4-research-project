Here, we perform the same quantitative techniques on the data collected for Jordan and adopt similar approaches to analysing the outcomes.

# Correlation & Linear regression 

<img width="746" alt="correlogram (Jordan)" src="https://user-images.githubusercontent.com/93497630/146651216-279d3c69-846b-40d5-9564-86edbdd0efad.png">

*Correlogram showing Jordan's data with linear regression model performed on each subplot*

Table: Summary of correlation coefficients and regression statistics  
<img width="1165" alt="Screen Shot 2021-12-31 at 10 45 14 PM" src="https://user-images.githubusercontent.com/93497630/147840582-a6aa5f9c-d9e3-4cc7-a599-d2b1c714b568.png">

## Analysis of statistical values

Primarily observing the scatterplots depicted in subplots B and F, we can assume that there is no linear or monotonic relationship existing between the Total Energy Supply (TES) per capita and Life Expectancy, as well as between the Total Electricity Generation (TEG) and Expected Years of Schooling. The corresponding Pearson and Kendall tau coefficients confirm our first review, since these values are way below the significance level set at 0.5.


Subplot A visualises the correlation between the TES per capita and the Gross National Income (GNI) per capita, which at first appears to follow a linear relationship. With a Pearson coefficient of 0.63 and a low p-value of 2e-04, the model found is indeed linear and significantly affirmed. However, the Kendall tau and R-squared value prove that the relation is not monotonic and strong.

The three subplots C, D and E illustrate the most relevant correlations to examine in our complementary investigation concerning Jordan data, from 1990 to 2019. They respectively portray the relationship between the TES per capita and expected years of schooling, the TEG per capita and the GNI per capita, and finally between the TEG per capita  and life expectancy. According to Pearson coefficients, Kendall tau, p-values and R-squared values, we establish three strong and significant linear-monotonic relationships between our variables. Indeed, all the coefficients and statistical values calculated respect their proper significance level or interval.  


# Clustering graphs & Analysis
![TES   GNI (Jordan)](https://user-images.githubusercontent.com/93497630/146656234-21d0724c-191b-4b8c-bb05-4d6d2371fd78.png)

*Figure 7: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and GNI per capita – Coloured by Cluster*
<img width="1114" alt="Screen Shot 2022-01-01 at 2 30 22 PM" src="https://user-images.githubusercontent.com/93497630/147852902-7617493b-c196-4429-a3e6-3305fec1d6e5.png">
 
![TES   life (Jordan)](https://user-images.githubusercontent.com/93497630/146656237-b63c07d4-099a-495d-92d0-5042ef171ecf.png)

*Figure 8: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and life expectancy at birth – Coloured by Cluster*
<img width="1115" alt="Screen Shot 2022-01-01 at 2 30 48 PM" src="https://user-images.githubusercontent.com/93497630/147852906-3bbeb829-7fa5-46c9-8e38-08050fdbd207.png">

![TES   school (Jordan)](https://user-images.githubusercontent.com/93497630/146656239-1c5baa56-0606-45fc-b406-f1c4e8876bca.png)

*Figure 9: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and expected years of schooling – Coloured by Cluster*
<img width="1115" alt="Screen Shot 2022-01-01 at 2 31 12 PM" src="https://user-images.githubusercontent.com/93497630/147852908-88a11ad6-2ad6-47f3-8f88-03c469d892bc.png">

![1a525d28-d9b1-448d-a8c6-c7bcd3b55db9-1](https://user-images.githubusercontent.com/93497630/147822017-b2ba6ded-a8c4-4ede-bfbc-e865beee14ed.jpg)

*Figure 10: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and GNI per capita – Coloured by Cluster*
<img width="1114" alt="Screen Shot 2022-01-01 at 2 31 36 PM" src="https://user-images.githubusercontent.com/93497630/147852910-7b4c65a9-2e1d-4305-b0c0-2c4ed1aa19b1.png">

![TEG   life (Jordan)](https://user-images.githubusercontent.com/93497630/146656247-439f33c4-0789-4f63-8389-66a9596e581b.png)

*Figure 11: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and life expectancy at birth – Coloured by Cluster*
<img width="1114" alt="Screen Shot 2022-01-01 at 2 31 54 PM" src="https://user-images.githubusercontent.com/93497630/147852913-043ec142-6fa0-4470-9ff0-c663803f2292.png">

![TEG   school (Jordan)](https://user-images.githubusercontent.com/93497630/146656248-dac232c0-5e67-48db-8ce8-88cf41caad14.png)

*Figure 12: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and expected years of schooling – Coloured by Cluster*
<img width="1116" alt="Screen Shot 2022-01-01 at 2 32 30 PM" src="https://user-images.githubusercontent.com/93497630/147852917-22373fa5-2887-4e9e-bcc8-bf9b8340aedb.png">


## [put at the bottom of the webpage]

The code used to plot the correlogram can he found here. (give a link to the GitHub page with the lines of code on it)
<img width="620" alt="Capture d’écran 2021-12-09 à 4 29 44 PM" src="https://user-images.githubusercontent.com/93673467/145436543-87e2fba6-0ef3-4d3d-a08f-4b25db372135.png">

The code used to calculate the correlation coefficients and regression statistics can be found here. (give a link to the GitHub page with the lines of code on it)

The code used to calculate the Kendall tau coefficients can be found here.

The code used to plot clustering graphs and calculate Silhouette scores can be found here.
