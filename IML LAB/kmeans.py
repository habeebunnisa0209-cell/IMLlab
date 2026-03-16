import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv("Mall_Customers.csv")

# Select only X and Y features
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Number of clusters
k = 3

# Apply K-Means
kmeans = KMeans(n_clusters=k, random_state=0)
kmeans.fit(X)

# Add cluster column
data['Cluster'] = kmeans.labels_

# -------- OUTPUT --------
print("Number of Clusters:", k)

print("\nCluster Assignment (X, Y, Cluster):")
print(data[['Annual Income (k$)', 
            'Spending Score (1-100)', 
            'Cluster']])

print("\nNumber of Points in Each Cluster:")
for i in range(k):
    print("Cluster", i, ":", len(data[data['Cluster'] == i]), "points")

print("\nCentroids of Each Cluster:")
for i, centroid in enumerate(kmeans.cluster_centers_):
    print("Cluster", i, "Centroid:", centroid)

# -------- GRAPH --------
plt.scatter(X.iloc[:,0], X.iloc[:,1], 
            c=data['Cluster'], cmap='rainbow')

plt.scatter(kmeans.cluster_centers_[:,0],
            kmeans.cluster_centers_[:,1],
            s=200, c='black', marker='X')

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("K-Means Clustering - Customer Data")
plt.show()

    
