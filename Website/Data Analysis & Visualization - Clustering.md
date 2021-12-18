
## Lebanon
![EGC vs GNI](https://user-images.githubusercontent.com/92082534/145281836-82c7f29d-9b5a-4779-a08e-523b9bbe0e0f.png)
![EGC vs life](https://user-images.githubusercontent.com/92082534/145281839-d98b636b-eed1-4ce9-ae31-4644cc0d79b7.png)
![EGC vs schooling](https://user-images.githubusercontent.com/92082534/145281845-d27b5125-014a-4a7d-a782-bac49f6c7d72.png)
<img width="620" alt="Screen Shot 2021-12-08 at 6 17 07 pm" src="https://user-images.githubusercontent.com/92082534/145281848-33e8e229-c775-437d-9289-4ca0be93e301.png">
![TES vs GNI](https://user-images.githubusercontent.com/92082534/145281851-fe092dc7-2f09-4510-9061-5dfa129f00dd.png)
![tes vs life](https://user-images.githubusercontent.com/92082534/145281853-faae8564-d854-4be2-b544-ff633c770b20.png)
![tes vs schooling](https://user-images.githubusercontent.com/92082534/145281857-98160c7a-2f13-40ce-ae30-06874303b875.png)



## [put at the bottom of the webpage]

The code used to plot clustering graphs can be found here.

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



