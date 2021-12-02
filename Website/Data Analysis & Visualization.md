# Summary data analysis - Marie
After the problem is clearly defined, the summary of all datasets was carried out using Python.

To give a quick overview of all the data that we used, the summary statistics table (Table 1) is presented with descriptive summary statistics for all datasets used in our research.

-analysis of outliers

<img width="819" alt="Capture d’écran 2021-11-29 à 3 04 18 PM" src="https://user-images.githubusercontent.com/93673467/143891708-727777cc-0269-45ab-a7ce-919f7cb19dd1.png">


The histograms are plotted using Python to show data distribution.

<img width="594" alt="Capture d’écran 2021-11-29 à 10 27 37 AM" src="https://user-images.githubusercontent.com/93673467/143891846-1bdcde02-2561-4122-951e-e414f09825e3.png">
<img width="384" alt="Capture d’écran 2021-11-29 à 3 06 47 PM" src="https://user-images.githubusercontent.com/93673467/143892331-066d53b0-e96f-4207-9176-ae5722abce1d.png">
<img width="390" alt="Capture d’écran 2021-11-29 à 3 06 57 PM" src="https://user-images.githubusercontent.com/93673467/143892341-013a3eb5-dbee-4088-814d-5617a01770f2.png">
<img width="337" alt="Capture d’écran 2021-11-29 à 3 07 04 PM" src="https://user-images.githubusercontent.com/93673467/143892351-f462777b-f9bc-4a46-a0c0-069c83302773.png">
<img width="385" alt="Capture d’écran 2021-11-29 à 3 07 09 PM" src="https://user-images.githubusercontent.com/93673467/143892369-cddc5266-5e11-4797-8e1e-c81cf51309eb.png">

 
# ANOVA & Regression - Ling
linear regression graphs + multiple regression graphs

-line graph
--> analyse the Pearson coefficients, R-squared values etc., Kendall tau correlation coefficients - to show that there is a non-linear relationship between two variables
<img width="897" alt="Capture d’écran 2021-11-29 à 3 08 58 PM" src="https://user-images.githubusercontent.com/93673467/143892495-1446642f-bb19-4530-81de-afa4de4828da.png">
<img width="443" alt="Capture d’écran 2021-11-29 à 3 09 56 PM" src="https://user-images.githubusercontent.com/93673467/143892683-e4b1c59b-2947-4d40-93be-036ebcb133c6.png">
(TEG: total electricity generation)

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

x-axis: Year; y-axis: Total Electricity generation  

repeat regression and clusering for the data on Jordan
