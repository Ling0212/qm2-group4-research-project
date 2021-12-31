As we have a multivariate dataset, a correlogram (or a correlation matrix) is used to analyse the relationship between each pair of numerical variables. It allows us to visualise the relationships of the whole dataset in a glimpse and to elegantly present them. Within the matrix, for each sub-scatterplot, a linear regression model is performed on the data for the purpose of investigating the strength of linear association between the two variables where there is any linear relationship. The diagonal also displays the distribution (evolution) of each variable over the past 30 years using a density plot.

<img width="723" alt="Correlogram (Lebanon)" src="https://user-images.githubusercontent.com/93497630/145657733-35ad0fe8-ed5f-4223-b79d-fb009b6de607.png">

*Correlogram showing Lebanon's data with linear regression model performed on each subplot*

## *Explanation of rationale behind our choice of statistical methods*
To achieve a concrete and precise understanding of the results of correlation and regression, we calculated the correlation coefficients and regression statistics for analysis. It is noteworthy from the correlogram that data in both Subplot D and Subplot E appear to be homoscedastic (i.e. points lie equally on both sides of the line of best fit) (Magiya, 2019), showing a linear relationship. In Subplot E, the two variables (‘Total Energy Supply per capita’ and ‘Life expectancy’) even exhibit a monotonic-like relationship. Therefore, we incorporate both parametric (Pearson) and non-parametric (Kendall tau) coefficients into analysis - Pearson coefficients are used to measure linear relationships, while Kendall tau coefficients are used to measure monotonic relationships (Magiya, 2019). Kendall tau coefficient serves exactly the same purpose as Spearman correlation and has a value between -1 and +1 that indicates how strongly two variables are monotonously related, but its absolute values generally tend to be smaller than Spearman coefficients (Berg, n.d.). We chose to use Kendall tau coefficients rather than Spearman’s for our sample size is relatively small (Magiya, 2019) and the variables are continuous with outliers (StatsTest.com, n.d.). The calculation results are summarised in the table below.

The 𝑅-squared value (also known as the coefficient of determination) is a statistical measure of how well the linear regression line fits the data points. More specifically, it determines the proportion of variance in the dependent variable (in our case, GNI per capita or life expectancy at birth or expected years of schooling) that can be explained by the independent variable (TES per capita or TEG per capita). The value can range from 0 to 1, indicating, for example, 0% to 100% of the variation in the dependent variable can be explained by the independent variable (Glen, 2020).

Table: Summary of correlation coefficients & regression statistics
<img width="1166" alt="Screen Shot 2021-12-31 at 10 44 42 PM" src="https://user-images.githubusercontent.com/93497630/147840552-8eb0bd1b-48ca-49af-851f-5c69fb81653a.png">

## *Correlation & Linear regression analysis*
For regression in Subplot A, B, C and F, the low Pearson coefficients highlight a very weak linear correlation between the two paired variables in each case, which can also be observed from the scatterplot per se. 

The p-value of 0.11 for Subplot C, much higher than the threshold significance level 0.05, indicates that there is a 11% probability (very likely) that the relationship shown could have arisen by random chance. There is no real evidence for any of the regression results being valid in this case. Thus, there is no statistically significant linear relationship between TES per capita and expected years of schooling. Likewise, given the fairly high p-value of 0.35 for Subplot F, a similar conclusion can be reached that no genuine linear relationship exists between TEG per capita and expected years of schooling. This informs us that linear correlation is unlikely to exist between the amount of energy supply (or electricity generation) available to an average Lebanese resident and the ‘education’ dimension measured by the years of school education that a child of school entrance age may expect to receive in Lebanon. 

While, for Subplot A and B, despite the linear correlation between TES per capita and GNI per capita, or between TES per capita and life expectancy is quite weak, the low p-values of 0.002 and 0.042 coming from regression imply that the relationships found are of statistical significance. 

What is more, we indeed found a statistically significant, strong positive linear relationship between TEG per capita & GNI per capita, TEG per capita & life expectancy in Lebanon from 1990 to 2019, with p-values of 2.44e-08 and 1.99e-05 respectively (both much lower than 0.05) and fairly high Pearson coefficients - 0.82 and 0.97 respectively, and high 𝑅-squared values (close to 1), all of which seem suitable for the relationship displayed in Subplot D and Subplot E. High 𝑅-squared values also imply that the calculated regression statistics might be useful for predicting real-world relationship between the variables. Put otherwise, for instance, in Lebanon in 1990-2019, 94% variation in life expectancy can be explained by variation in total electricity generation per capita. The gradient of the best-fitted line being 8194 in Subplot E reveals that for each 1% increase in electricity generation per capita, a newborn infant could expect to live for around 82 years more if prevailing patterns of age-specific mortality rates at the time of birth stay the same throughout the infant’s life, for which research finding might also have practically significant implications.

Meanwhile, the high positive Kendall tau coefficients suggest that the relationship between TEG per capita & GNI per capita, TEG per capita & life expectancy in Lebanon from 1990 to 2019 can also be defined as having strong positive monotonic correlation. This finding sheds light on the importance for Lebanon’s officials or policymakers to ensure sufficient electricity generation if aiming to achieve certain macroeconomic targets or national health outcomes.

## [put at the bottom of the webpage]
The code used to plot the correlogram can he found here. (give a link to the GitHub page with the lines of code on it)
<img width="620" alt="Capture d’écran 2021-12-09 à 4 31 54 PM" src="https://user-images.githubusercontent.com/93673467/145436979-17c19500-4418-47ca-85ae-40cb85caaec4.png">

The code used to calculate the correlation coefficients and regression statistics can be found here. (give a link to the GitHub page with the lines of code on it)

The code used to calculate the Kendall tau coefficients can be found here.
<img width="760" alt="Capture d’écran 2021-12-13 à 7 36 53 PM" src="https://user-images.githubusercontent.com/93673467/145877331-7f126a70-2dfd-421a-a39c-522527fe3e38.png">




