To attempt to examine more closely the yearly variation regarding the relationship between energy supply (electricity generation) per capita & social wellbeing in Lebanon in the past three decades, K-means clustering is applied on the dataset to identify different clusters of years. The 30 years (from 1990 to 2019) are clustered by the variables of research interest, to produce more meaningful analysis.

As we have different units and distributions in the five variables, technical standardisation is applied across the dataset using the formula x’ = (x - xmin) / (xmax - xmin) in Excel, to obtain manipulated data on a comparable scale. Min-max rescaling is an appropriate approach to undertake here since the density plots drawn before (at the diagonal of the correlogram) show that most data points are unsymmetrically distributed (bar data for 'Expected years of schooling' and 'GNI per capita'). Rescaled data values are then inputted into a Python programme to implement K-means clustering and to calculate Silhouette scores for assessing the clustering quality, i.e. how strongly data is clustered. The clustering results with the optimal number of clusters (highest silhouette scores) will be ultimately presented, summarised and analysed using tables.

## Clustering graphs & analysis
![TES   GNI (Lebanon)](https://user-images.githubusercontent.com/93497630/146655857-1f75d45b-29ae-4168-b44c-aa58efb99b9e.png)

*Figure 1: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and GNI per capita – Coloured by Cluster*

Table 1: Summary and analysis of clustering results from Figure 1
<img width="736" alt="Screen Shot 2021-12-19 at 9 34 10 PM" src="https://user-images.githubusercontent.com/93497630/146691684-2689b342-3d69-4119-839d-185ee76538a9.png">

![TES   life (Lebanon)](https://user-images.githubusercontent.com/93497630/146655859-88aca7d8-e768-4b1b-b46a-f22af96eaea8.png)

*Figure 2: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and life expectancy at birth – Coloured by Cluster*

Table 2: Summary and analysis of clustering results from Figure 2 
 <img width="733" alt="Screen Shot 2021-12-19 at 9 34 37 PM" src="https://user-images.githubusercontent.com/93497630/146691690-3296dabd-6fa4-4473-964c-b3f83df83c96.png">

![TES   school (Lebanon)](https://user-images.githubusercontent.com/93497630/146655860-f1d76155-92b2-4159-9123-7af0c700cd43.png)

*Figure 3: Clustering 30 years (from 1990 to 2019) by total energy supply per capita and expected years of schooling – Coloured by Cluster*

![TEG   GNI (Lebanon)](https://user-images.githubusercontent.com/93497630/146655863-3b9fab71-66f9-491f-8094-68f4906a9bb4.png)

*Figure 4: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and GNI per capita – Coloured by Cluster*

![TEG   life (Lebanon)](https://user-images.githubusercontent.com/93497630/146655867-8eb66636-52b6-4a87-b36e-745bcd69cce3.png)

*Figure 5: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and life expectancy at birth – Coloured by Cluster*

![TEG   school (Lebanon)](https://user-images.githubusercontent.com/93497630/146655869-3aefca4d-e627-478c-987f-c9507dc4e2bf.png)

*Figure 6: Clustering 30 years (from 1990 to 2019) by electricity generation per capita and expected years of schooling – Coloured by Cluster*





## [put at the bottom of the webpage]

The code used to plot clustering graphs and calculate Silhouette scores can be found here.

    num_clusters = 2
    fig_title = 'title of graph'
    x_label   = 'Standardised data (min-max rescaled) of total energy supply per capita'
    y_label   = 'Standardised data (min-max rescaled) of gross national income per capita'
    title_fontsize = 13
    label_fontsize = 10


    import numpy as np              # For working with numerical data
    import sklearn.cluster as sklc  # For clustering
    import sklearn.metrics as sklm  # For the silhouette score

    data = np.genfromtxt(data_filename,delimiter = ',')



    kmeans_output = sklc.KMeans(n_clusters=num_clusters, n_init=1).fit(data)


    clustering_ids_kmeans = kmeans_output.labels_

    complete_data_with_clusters = np.hstack((data,np.array([clustering_ids_kmeans]).T))
    np.savetxt(output_data_filename + '_unsorted.csv',complete_data_with_clusters,delimiter=",")

    order_of_rows = np.argsort(complete_data_with_clusters[:,-1])
    complete_data_with_clusters = complete_data_with_clusters[order_of_rows]
    np.savetxt(output_data_filename + '_sorted.csv',complete_data_with_clusters,delimiter=",")

    data_by_cluster = []

    for i in range(num_clusters):

        this_data = []

        for row in complete_data_with_clusters:

            if row[-1] == i:
                this_data.append(row)

        this_data = np.array(this_data)

        data_by_cluster.append(this_data)


        def setup_figure():

        plt.xlabel(x_label,fontsize=label_fontsize)
        plt.ylabel(y_label,fontsize=label_fontsize)



    x_values = data[:,0]
    y_values = data[:,1]

    plt.figure(0,figsize=(figure_width,figure_height))
    setup_figure()
    plt.title(fig_title,fontsize=title_fontsize)
    plt.plot(x_values,y_values,'k.')
    plt.savefig(output_figure_filename + '_unclustered_data.png')

    color_list = ['b','r','g','m','c','k','y']
    marker_list = ['o','x','+','s','d','D','v','^','<','>','p','*','h','H','o']
    num_colors = len(color_list)
    num_markers = len(marker_list)


    for i in range(num_clusters):

        plt.figure(i+1,figsize=(figure_width,figure_height))
        setup_figure()
        plt.title(fig_title + ' - Cluster ' + str(i),fontsize=title_fontsize)

        x_values = data_by_cluster[i][:,0]
        y_values = data_by_cluster[i][:,1]

        print(i,color_list[i % num_colors])

        plt.plot(x_values,y_values,color_list[i % num_colors] + '.')
        plt.savefig(output_figure_filename + '_cluster_' + str(i) + '.png')


    plt.figure(num_clusters + 1,figsize=(figure_width,figure_height))
    setup_figure()
    plt.title(fig_title + 'Coloured by CLuster',fontsize=title_fontsize)

    for i in range(num_clusters):
    
    x_values = data_by_cluster[i][:,0]
    y_values = data_by_cluster[i][:,1]
    
    print(i,color_list[i % num_colors])
    
    plt.plot(x_values,y_values,color_list[i % num_colors] + marker_list[i % num_markers],ms=7)
      
    plt.savefig(output_figure_filename + '.png')


    silhouette_kmeans = sklm.silhouette_score(data,clustering_ids_kmeans)


    print("Silhouette Score:", silhouette_kmeans)



