## Correlogram

As we have a multivariate dataset, a correlogram (or a correlation matrix) is used to analyse the relationship between each pair of numerical variables. It allows us to visualize the relationships of the whole dataset in a glimpse and to elegantly present them. Within the matrix, for each sub-scatterplot, a linear regression model is performed on the data for the purpose of investigating the strength of linear association between the two variables where there is any linear relationship. The diagonal also displays the distribution (evolution) of each variable over the past 30 years using a density plot.

To achieve a concrete and precise understanding of the results of correlation and regression, we calculated the correlation coefficients and regression statistics. Seen from the sub-scatterplots: the data on both Subplot D and Subplot E appear to be homoscedastic (points lie equally on both sides of the line of best fit), showing a linear relationship (Magiya, 2019); while for the rest of the sub-scatterplots, no clear pattern can be directly observed from the plots. Therefore, we incorporate both parametric (Pearson) and non-parametric coefficients (Kendall tau) into analysis. We chose to use Kendall tau coefficients rather than Spearman’s as our sample size is relatively small (Magiya, 2019). Kendall Tau coefficient of correlation is usually smaller values than Spearman coefficients….
 
Pearson coefficients are used to measure linear relationships, while Kendall tau coefficients are used to measure monotonic relationships ( ).
 
<img width="723" alt="Correlogram (Lebanon)" src="https://user-images.githubusercontent.com/93497630/145657733-35ad0fe8-ed5f-4223-b79d-fb009b6de607.png">

*Correlogram showing the whole dataset on Lebanon with linear regression model performed on each subplot*

Table: Summary of regression statistics & correlation coefficients
<img width="1053" alt="Screen Shot 2021-12-17 at 2 35 26 PM" src="https://user-images.githubusercontent.com/93497630/146560509-210c30ab-693c-44fe-8972-e3b8e67816c8.png">

 

## Correlation & linear regression analysis

analyse the Pearson correlation coefficients, Kendall tau correlation coefficients (to explore if there is a significant relationship between the two variables) + p-values, R-squared values
+ Subplot D and Subplot E are the most relevant applications of linear regression analysis on the Lebanon's datasets

...






## [put at the bottom of the webpage]
The code used to plot the correlogram can he found here. (give a link to the GitHub page with the lines of code on it)

<img width="620" alt="Capture d’écran 2021-12-09 à 4 31 54 PM" src="https://user-images.githubusercontent.com/93673467/145436979-17c19500-4418-47ca-85ae-40cb85caaec4.png">

The code used to calculate the correlation coefficients and regression statistics can be found here. (give a link to the GitHub page with the lines of code on it)

The code used to calculate the Kendall tau 

<img width="760" alt="Capture d’écran 2021-12-13 à 7 36 53 PM" src="https://user-images.githubusercontent.com/93673467/145877331-7f126a70-2dfd-421a-a39c-522527fe3e38.png">




