# Summary data analysis - Marie
After the problem is clearly defined, the summary of all datasets was carried out using Python.

To give a quick overview of all the data that we used, the summary statistics table (Table 1) is presented with descriptive summary statistics for all datasets used in our research.

<img width="825" alt="Capture d’écran 2021-12-03 à 11 09 59 AM" src="https://user-images.githubusercontent.com/93673467/144619317-a19aa063-9bc1-46bd-8d37-a9aaf4ed7b07.png">

-analysis of outliers: Seen from this table above, there is one lower outlier in the data on total energy supply per capita. The minimum value of 29.2 TJ (the data point in 1990 - just at the end of Lebanese civil war) is lower than 34.6 TJ, the lower bound of tukey fence. We think, however, it is a true data point that should be included in our data analysis and visualisation.

The histograms are plotted using Python to show data distribution.

<img width="350" alt="Capture d’écran 2021-12-03 à 11 20 40 AM" src="https://user-images.githubusercontent.com/93673467/144619371-6046db6e-b62e-4167-a028-529d283be27c.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 06 47 PM" src="https://user-images.githubusercontent.com/93673467/143892331-066d53b0-e96f-4207-9176-ae5722abce1d.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 06 57 PM" src="https://user-images.githubusercontent.com/93673467/143892341-013a3eb5-dbee-4088-814d-5617a01770f2.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 07 04 PM" src="https://user-images.githubusercontent.com/93673467/143892351-f462777b-f9bc-4a46-a0c0-069c83302773.png">
<img width="340" alt="Capture d’écran 2021-11-29 à 3 07 09 PM" src="https://user-images.githubusercontent.com/93673467/143892369-cddc5266-5e11-4797-8e1e-c81cf51309eb.png">

 
# Linear regression & Correlogram - Ling
-multiple regression graphs

<img width="564" alt="Capture d’écran 2021-12-03 à 11 50 48 AM" src="https://user-images.githubusercontent.com/93673467/144619556-1c82a9a1-da03-416c-b302-723e002a0849.png">

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



# Complementary investigation
## Lydia (clustering), Ling (regression)

repeat regression and clusering for the data on Jordan
![JordanEGC_School](https://user-images.githubusercontent.com/92082534/144684163-f5f4bf20-897b-43b9-b854-810dd25f8819.png)
![JordanEGC_Life](https://user-images.githubusercontent.com/92082534/144684165-6fd03fae-8a2e-482c-931f-f1047867857e.png)
![JordanEGC_GNI](https://user-images.githubusercontent.com/92082534/144684166-835177e5-9c34-4546-8f97-21f218c27de1.png)
![JordanTES_vs_GNI](https://user-images.githubusercontent.com/92082534/144684169-2bfd857b-bf5a-4252-83bd-7156e5414b46.png)
![JordanTES_vs_Life](https://user-images.githubusercontent.com/92082534/144684172-0cc0adf5-a4dd-4c0d-a0e6-67650c67bf29.png)
![JordanTES_vs_Schooling](https://user-images.githubusercontent.com/92082534/144684174-380738a6-814c-4d14-9baa-f02f3f85adf7.png)
<img width="457" alt="jordan" src="https://user-images.githubusercontent.com/92082534/144684175-232d58ed-b0f3-4433-a266-263e154ac806.png">


# Data analysis
+ analyse outcomes of linear regression plots & correlogram for Lebanon - Ling
+ analyse outcomes of linear regression plots & correlogram for Jordan - Marie
+ analyse/summarise outcomes of clustering graphs for Lebanon, using tables - Lydia (reponsible for the first 3 graphs), Marie (reponsible for the other 3 graphs)
+ analyse/summarise outcomes of clustering graphs for Jordan, using tables - Diane (reponsible for the first 3 graphs), Enrico (reponsible for the other 3 graphs)
