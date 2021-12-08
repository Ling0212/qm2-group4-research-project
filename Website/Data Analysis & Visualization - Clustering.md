# Clustering - Lydia
As we have different units and distributions in the five variables, technical standardization will be applied across the datasets using the formula 𝑧 = (𝑥−𝜇 )/𝜎 (whether use Z-score standardization depends on whether all data points are roughly symmetrically distributed) in Excel, to obtain manipulated data on a comparable scale. 		
Perform clustering on all the variables by years & calculate Silhouette scores to assess the clustering quality, i.e. how strongly data is clustered→ The clustering results with the optimal number of clusters (highest silhouette scores) will be ultimately presented, summarized and analyzed.→ to identify different clusters of years→ analyse the electricity generation/energy supply per capita & social wellbeing relationship in relation to turbulent events that repeatedly happened in certain clustered years
* present six clustering graphs

1. Please don’t type the title for each clustering graph on Python, later I will manually add the title underneath each graph (also for aesthetics purpose), but could you name the x-axis and y-axis for each graph in this way⬇️? It seems clearer and more precise naming in this way.

for example

X-axis: Standardised data (min-max rescaled) of electricity generation per capita

Y-axis: Standardised data (min-max rescaled) of life expectancy at birth

2. for each clustering graph, use ONE TABLE to clearly summarise: the number of data points in each cluster, max, min, mean for each variable in each cluster - Lydia works on 3 graphs & Marie works on 3 graphs

—> then combine clustering findings from all the 6 clustering graphs on Lebanon to analyse the relationship between TES per capita/EG per capita and social wellbeing

* repeat "2" for Jordan - Diane works on 3 graphs and Enrico works on 3 graphs

## Lebanon

![EGC vs GNi](https://user-images.githubusercontent.com/92082534/145262344-fa215b44-2ae6-478c-b173-482c99e738fb.png)
![EGC vs life](https://user-images.githubusercontent.com/92082534/145262348-3a750da9-9a2a-4100-82a2-adbebc9bd051.png)
![EGC vs schooling](https://user-images.githubusercontent.com/92082534/145262350-f9761e42-dc02-4467-b760-83f2f55e01ca.png)
<img width="620" alt="Screen Shot 2021-12-08 at 6 17 07 pm" src="https://user-images.githubusercontent.com/92082534/145262355-5a70ffc5-dd37-4c63-a8f4-1f3d391b9610.png">
![TES vs GNI](https://user-images.githubusercontent.com/92082534/145262357-bcb2a0bb-4d9d-4c86-ae28-e1260a59b110.png)
![tes vs life](https://user-images.githubusercontent.com/92082534/145262359-93a7cbc9-390f-45d3-8ea9-20453fb71ba1.png)
![tes vs schooling](https://user-images.githubusercontent.com/92082534/145262367-28f2d7d6-f661-4261-849e-13d8de5bfee0.png)

## Jordan

![EGC vs GNI](https://user-images.githubusercontent.com/92082534/145262486-f5627c09-4e34-4cb7-8f43-c97c62a90fff.png)
![EGC vs life](https://user-images.githubusercontent.com/92082534/145262489-e0b8196d-b32e-4732-9a00-45c1910f70a7.png)
![EGC vs schooling](https://user-images.githubusercontent.com/92082534/145262495-c6cdc0af-cb8a-4e12-b721-61d16395a04e.png)
<img width="452" alt="Screen Shot 2021-12-08 at 6 17 22 pm" src="https://user-images.githubusercontent.com/92082534/145262497-8671d5e1-26bc-461c-966c-dc821f7fcbe9.png">
![tes vs GNI](https://user-images.githubusercontent.com/92082534/145262501-55af67fe-e7fd-426f-8b9b-eecc2fb15b74.png)
![tes vs life](https://user-images.githubusercontent.com/92082534/145262505-90fcd721-3233-4a4f-a18d-36ce328397df.png)
![tes vs schooling](https://user-images.githubusercontent.com/92082534/145262506-c34787c3-bbbc-4d57-bf88-e7980def459e.png)


## K-MEANS CLUSTERING IN PYTHON

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



