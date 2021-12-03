# Summary data analysis - Marie
After the problem is clearly defined, the summary of all datasets was carried out using Python.

To give a quick overview of all the data that we used, the summary statistics table (Table 1) is presented with descriptive summary statistics for all datasets used in our research.

<img width="825" alt="Capture d’écran 2021-12-03 à 11 09 59 AM" src="https://user-images.githubusercontent.com/93673467/144619317-a19aa063-9bc1-46bd-8d37-a9aaf4ed7b07.png">

-analysis of outliers

The histograms are plotted using Python to show data distribution.

<img width="350" alt="Capture d’écran 2021-12-03 à 11 20 40 AM" src="https://user-images.githubusercontent.com/93673467/144619371-6046db6e-b62e-4167-a028-529d283be27c.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 06 47 PM" src="https://user-images.githubusercontent.com/93673467/143892331-066d53b0-e96f-4207-9176-ae5722abce1d.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 06 57 PM" src="https://user-images.githubusercontent.com/93673467/143892341-013a3eb5-dbee-4088-814d-5617a01770f2.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 07 04 PM" src="https://user-images.githubusercontent.com/93673467/143892351-f462777b-f9bc-4a46-a0c0-069c83302773.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 07 09 PM" src="https://user-images.githubusercontent.com/93673467/143892369-cddc5266-5e11-4797-8e1e-c81cf51309eb.png">

 
# ANOVA & Regression - Ling
linear regression graphs + multiple regression graphs

<img width="564" alt="Capture d’écran 2021-12-03 à 11 50 48 AM" src="https://user-images.githubusercontent.com/93673467/144619556-1c82a9a1-da03-416c-b302-723e002a0849.png">

-line graph
--> analyse the Pearson coefficients, R-squared values etc., Kendall tau correlation coefficients - to show that there is a non-linear relationship between two variables

<img width="819" alt="Capture d’écran 2021-12-03 à 11 50 07 AM" src="https://user-images.githubusercontent.com/93673467/144619582-7d9b7e84-5e1d-4511-ad11-4193b5c2768f.png">

# Clustering - Lydia
As we have different units and distributions in the five variables, technical standardization will be applied across the datasets using the formula 𝑧 = (𝑥−𝜇 )/𝜎 (whether use Z-score standardization depends on whether all data points are roughly symmetrically distributed) in Excel, to obtain manipulated data on a comparable scale. 		
Perform clustering on all the variables by years & calculate Silhouette scores to assess the clustering quality, i.e. how strongly data is clustered→ The clustering results with the optimal number of clusters (highest silhouette scores) will be ultimately presented, summarized and analyzed.→ to identify different clusters of years→ analyse the electricity consumption/energy supply per capita & social wellbeing relationship in relation to turbulent events that repeatedly happened in certain clustered years
* present six clustering graphs

![EGC_vs_GNI](https://user-images.githubusercontent.com/92082534/144406347-8700b560-c74f-4895-937d-f3af75c3823c.png)
![EGC_vs_LifeExpectancy](https://user-images.githubusercontent.com/92082534/144406362-2cdc467a-e2cc-4d80-be2e-b278cf840b1d.png)
![EGC_vs_schooling](https://user-images.githubusercontent.com/92082534/144406373-27648a0a-ea01-4a8c-a30b-fba3984454cd.png)
![TES_vs_Schooling](https://user-images.githubusercontent.com/92082534/144453938-b345085d-3e1f-4e91-a42b-7c13b2fbeb1f.png)
![TES_vs_GNI](https://user-images.githubusercontent.com/92082534/144453943-60513484-eda9-4119-8659-7e8f9b9bcfe3.png)
<img width="621" alt="Screen Shot 2021-12-02 at 3 39 10 pm" src="https://user-images.githubusercontent.com/92082534/144453947-c02e8609-961c-4b26-8945-36f5b27b983c.png">
![TES_vs_LifeExpectancy](https://user-images.githubusercontent.com/92082534/144453948-008bed8e-93f0-4e34-b57e-176fb154f33b.png)



# Violinplots & Complementary investigation
## Lydia (violinplots, clustering), Ling (regression)
Draw two grouped violinplots to visualise the same variable by different countries (input data points for Lebanon and Jordan across 29 years), to ascertain whether Jordan is a ‘similar’ country or not

https://www.python-graph-gallery.com/54-grouped-violinplot

x-axis: Year; y-axis: Total Energy Supply per capita

x-axis: Year; y-axis: Total Electricity generation per capita

repeat regression and clusering for the data on Jordan
<img width=![JordanEGC_School](https://user-images.githubusercontent.com/92082534/144684088-6067ca7d-0a5f-407a-87d2-69b21897d457.png)
![JordanEGC_Life](https://user-images.githubusercontent.com/92082534/144684090-d429daa5-0d1a-4f8e-be1c-7553c9ca7e0a.png)
![JordanEGC_GNI](https://user-images.githubusercontent.com/92082534/144684094-9d41dae4-fff6-494e-8489-fca29840a844.png)
![JordanTES_vs_GNI](https://user-images.githubusercontent.com/92082534/144684095-0c553e43-d98e-4054-9e5e-400fe5a9f719.png)
![JordanTES_vs_Life](https://user-images.githubusercontent.com/92082534/144684097-58ed57c8-8e19-475d-bbf0-ea02fbf1b963.png)
"457" alt="jordan" src="https://user-images.githubusercontent.com/92082534/144684075-a360466e-4f9f-4c2b-acf6-ec643dc87225.png">
![JordanTES_vs_Schooling](https://user-images.githubusercontent.com/92082534/144684101-ec26f47c-c9b1-4a36-b29c-4bb297a95a34.png)





