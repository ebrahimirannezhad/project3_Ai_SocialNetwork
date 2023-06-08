import urllib.request
import gzip
import networkx as nx
import matplotlib.pyplot as plt

url = "https://snap.stanford.edu/data/ca-GrQc.txt.gz"
output_file = "ca-GrQc.txt.gz"

# Download the dataset
urllib.request.urlretrieve(url, output_file)

# Extract the dataset from the gzip file
with gzip.open(output_file, 'rb') as f_in:
    with open("ca-GrQc.txt", 'wb') as f_out:
        f_out.write(f_in.read())
# Load the graph from the dataset file
graph = nx.read_edgelist("ca-GrQc.txt")

# Print some basic information about the graph
print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 33:
# 33 Degree distribution

# Compute the degree distribution
degree_sequence = [degree for _, degree in graph.degree()]
degree_count = nx.degree_histogram(graph)

# Plot the degree distribution
plt.loglog(degree_count, 'b-', marker='o')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Count")
plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 34:
# 34 Short path length distribution

# Compute the shortest path lengths
shortest_path_lengths = dict(nx.shortest_path_length(graph))

# Collect the unique shortest path lengths and their frequencies
lengths = []
counts = []
for lengths_dict in shortest_path_lengths.values():
    for length in lengths_dict.values():
        lengths.append(length)
        counts.append(1)

# Compute the histogram of shortest path lengths
length_count = {}
for length in lengths:
    if length not in length_count:
        length_count[length] = 0
    length_count[length] += 1

# Sort the lengths and their counts based on length value
sorted_lengths = sorted(length_count.keys())
count_values = [length_count[length] for length in sorted_lengths]

# Plot the shortest path length distribution
plt.bar(sorted_lengths, count_values)
plt.title("Shortest Path Length Distribution")
plt.xlabel("Shortest Path Length")
plt.ylabel("Count")
plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 35:
# 35 Clustering Coefficient Distribution (توزیع ضریب خوشه‌ای):

# Compute the clustering coefficients
clustering_values = nx.clustering(graph)

# Compute the histogram of clustering coefficients
clustering_count = {}
for clustering in clustering_values:
    if clustering not in clustering_count:
        clustering_count[clustering] = 0
    clustering_count[clustering] += 1

# Sort the clustering coefficients and their counts
sorted_clustering = sorted(clustering_count.keys())
count_values = [clustering_count[clustering] for clustering in sorted_clustering]

# Plot the clustering coefficient distribution
plt.bar(sorted_clustering, count_values)
plt.title("Clustering Coefficient Distribution")
plt.xlabel("Clustering Coefficient")
plt.ylabel("Count")
plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 36:
# 36 WCC size distribution

# Compute the weakly connected components
wcc = nx.connected_components(graph.to_undirected())

# Compute the size of each weakly connected component
wcc_sizes = [len(component) for component in wcc]

# Compute the histogram of weakly connected component sizes
wcc_count = {}
for size in wcc_sizes:
    if size not in wcc_count:
        wcc_count[size] = 0
    wcc_count[size] += 1

# Sort the weakly connected component sizes and their counts
sorted_wcc = sorted(wcc_count.keys())
count_values = [wcc_count[size] for size in sorted_wcc]

# Plot the weakly connected component size distribution
plt.bar(sorted_wcc, count_values)
plt.title("WCC Size Distribution")
plt.xlabel("Size of WCC")
plt.ylabel("Count")
plt.show()
