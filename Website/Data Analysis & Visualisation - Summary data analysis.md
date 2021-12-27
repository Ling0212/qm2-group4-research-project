# Summary data analysis

After clearly defining the problem and collecting data for the variables of research interest, to have a quick overview of all the data that we will use, we computed the descriptive summary statistics for both Lebanon data and Jordan data on Python. (The low outlier limit and high outlier limit for Tukey fences are computed afterwards using the formula "lower quartile - 1.5 x interquartile range" and "upper quartile + 1.5 x interquartile range" respectively.) 

The results are presented in the two summary statistics tables below.

<img width="1097" alt="Screen Shot 2021-12-10 at 9 18 39 PM" src="https://user-images.githubusercontent.com/93497630/145646934-0d78df8b-c3d1-4970-9148-bfde03804147.png">

<img width="1096" alt="Screen Shot 2021-12-10 at 9 19 26 PM" src="https://user-images.githubusercontent.com/93497630/145646971-89b8d527-f4f4-47a8-a639-bf0e5aedbc4e.png">


*Note*: Seen from the tables, if using Tukey fences as benchmarks, for the Lebanon data, there are two lower outliers in the data of total energy supply per capita and one lower outlier in the data of GNI per capita (the data values are from 1990 and 1992 - the years fairly close to the end of Lebanese civil war), while for the Jordan data, there are six higher outliers in the data of total energy supply per capita. 

Although these data values are lower or higher outliers (i.e. lower than the corresponding low outlier limits or higher than the corresponding high outlier limit), they should and will be included in the following analysis. There is no valid reason to remove them because they are true data points with real-world meanings constituting an important part of the data pattern.

The code used to calculate the descriptive summary statistics can be found _here_. 
>> Example of the code used for computing the Summary Statistics values for the Total Energy Supply (TJ) per capita, in Lebanon
<img width="477" alt="Capture d’écran 2021-12-27 à 6 31 35 PM" src="https://user-images.githubusercontent.com/93673467/147494621-6a7b2f17-0f76-40a6-8336-60c2ead96290.png">
