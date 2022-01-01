# K-MEANS CLUSTERING IN PYTHON


# This program performs a k-means clustering on data stored in a csv file,

# The data file must be two columns of numbers, the x values and y values - no column labels, etc.
# It must be saved as a csv file (e.g. use "Save As" in Excel and choose csv format).
# It must be saved in the same folder as this program.

# [Actually, the file can have more than two columns. The clustering works for data with many fields.
# However, it will only plot the first two columns against each other, for obvious reasons.]

# This program plots:
#   - A scatter plot of all the data, unclustered;
#   - A scatter plot of each cluster separately;
#   - A scatter plot of all the data, coloured by cluster.
# All of these plots are saved to your computer, in the same folder as this Python file.

# This program also saves a csv file of the original data, with an extra column,...
# indicating which cluster each point has been assigned to.

# The program also prints the silhouette score for your clustering...
# This is a measure of how well the data is clustered, from -1 (extremely poor) to 1 (extremely strong).


# SET THE FOLLOWING VARIABLES TO CONTROL HOW THE PROGRAM FUNCTIONS:

    
# CLUSTERING VARIABLES

# This line sets the number of clusters you want to find:
num_clusters = 2
# [Note that this program only plots in 7 different colours,...
# if you have more clusters, they will not all be distint in the final figure.]
    
    
# FILENAMES

# In the next line, replace clustering_example_data.csv with the filename of your data:
data_filename = 'clustering_example_data.csv'

# In the next line, replace clustering_figure with the filename you wish to save the images as:
output_figure_filename = 'clustering_figure'
# [Each image will start with this string, with a little extra to differentiate the different images.]

# In the next line, replace complete_data_with_clusters.csv with the filename you wish to save the clustered data as:
output_data_filename = 'complete_data_with_clusters'


# FIGURE PARAMETERS

# Use the next line to set figure height and width (experiment to check the scale):
figure_width, figure_height = 10,10

# These lines set the figure title and axis labels and the font sizes:
fig_title = 'figure title'
x_label   = 'Standardised data (min-max rescaled) of electricity generation per capita'
y_label   = 'Standardised data (min-max rescaled) of gross national income per capita'
title_fontsize = 13
label_fontsize = 10

# These lines set the limits of the x and y axes, so that all plots are on the same scale.
#x_min, x_max = -0.1, 1
#y_min, y_max = -0.1, 1


# SETUP

# The following lines import the necessary packages. You can ignore them.
import matplotlib.pyplot as plt # For plotting
import numpy as np              # For working with numerical data
import sklearn.cluster as sklc  # For clustering
import sklearn.metrics as sklm  # For the silhouette score

# The next line imports the data:
data = np.genfromtxt(data_filename,delimiter = ',')


# PERFORM CLUSTERING

# This line performs the k-means clustering:
kmeans_output = sklc.KMeans(n_clusters=num_clusters, n_init=1).fit(data)

# This line creates a list giving the final cluster number of each point:
clustering_ids_kmeans = kmeans_output.labels_


# DATA PROCESSING

# These lines add the cluster IDs to the original data, sort by cluster, and save the data with these added cluster IDs.

complete_data_with_clusters = np.hstack((data,np.array([clustering_ids_kmeans]).T))
np.savetxt(output_data_filename + '_unsorted.csv',complete_data_with_clusters,delimiter=",")

order_of_rows = np.argsort(complete_data_with_clusters[:,-1])
complete_data_with_clusters = complete_data_with_clusters[order_of_rows]
np.savetxt(output_data_filename + '_sorted.csv',complete_data_with_clusters,delimiter=",")

# The loop below creates a separate data array for each cluster, and puts these arrays together in a list:
data_by_cluster = []

for i in range(num_clusters):
    
    this_data = []
    
    for row in complete_data_with_clusters:
        
        if row[-1] == i:
            this_data.append(row)
    
    this_data = np.array(this_data)
    
    data_by_cluster.append(this_data)
 

# CREATE FIGURES

# This is a function that sets up each figure's x-limits and y-limits and axis labels.

def setup_figure():
    
    # If you want to specify the x and y limits (which will be the same for all plots),
    # uncomment the following four lines and set limits as required:
    
    #x_min, x_max = -0.1, 1
    #y_min, y_max = -0.1, 1
    #plt.xlim([x_min, x_max])
    #plt.ylim([y_min, y_max])
    
    plt.xlabel(x_label,fontsize=label_fontsize)
    plt.ylabel(y_label,fontsize=label_fontsize)


# FIGURE 0 : UNCLUSTERED DATA

# These lines extract the y-values and the x-values from the data:
x_values = data[:,0]
y_values = data[:,1]

# The next lines create and save the plot:
plt.figure(0,figsize=(figure_width,figure_height))
setup_figure()
plt.title(fig_title,fontsize=title_fontsize)
plt.plot(x_values,y_values,'k.')
plt.savefig(output_figure_filename + '_unclustered_data.png')


# FIGURES 1-N : SEPARATE CLUSTER PLOTS

# This is a list of colours to differentiate each cluster.
color_list = ['b','r','g','m','c','k','y']
marker_list = ['o','x','+','s','d','D','v','^','<','>','p','*','h','H','o']
num_colors = len(color_list)
num_markers = len(marker_list)

# This loop goes through each cluster, plots it and saves it:
for i in range(num_clusters):
    
    plt.figure(i+1,figsize=(figure_width,figure_height))
    setup_figure()
    plt.title(fig_title + ' - Cluster ' + str(i),fontsize=title_fontsize)
    
    x_values = data_by_cluster[i][:,0]
    y_values = data_by_cluster[i][:,1]
    
    print(i,color_list[i % num_colors])
    
    plt.plot(x_values,y_values,color_list[i % num_colors] + '.')
    plt.savefig(output_figure_filename + '_cluster_' + str(i) + '.png')


# FIGURE N + 1 : COMBINED CLUSTER PLOT

# These lines create a plot with all the data points, coloured by cluster.
plt.figure(num_clusters + 1,figsize=(figure_width,figure_height))
setup_figure()
# plt.title(fig_title + 'Coloured by Cluster',fontsize=title_fontsize)

for i in range(num_clusters):
    
    x_values = data_by_cluster[i][:,0]
    y_values = data_by_cluster[i][:,1]
    
    print(i,color_list[i % num_colors])
    
    plt.plot(x_values,y_values,color_list[i % num_colors] + marker_list[i % num_markers],ms=7)
      
plt.savefig(output_figure_filename + '.png')


# SILHOUETTE SCORE

# These lines calculate the silhouette score...
silhouette_kmeans = sklm.silhouette_score(data,clustering_ids_kmeans)

# ... and print it:
print("Silhouette Score:", silhouette_kmeans)


