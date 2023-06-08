import urllib.request
import gzip
import networkx as nx
import matplotlib.pyplot as plt

# Download the dataset
url = "http://snap.stanford.edu/data/ca-AstroPh.txt.gz"
dataset_path = "ca-AstroPh.txt.gz"

urllib.request.urlretrieve(url, dataset_path)

# Extract the dataset
with gzip.open(dataset_path, "rb") as file_in:
    with open("ca-AstroPh.txt", "wb") as file_out:
        file_out.write(file_in.read())

# Read the dataset and generate the graph
graph = nx.read_edgelist("ca-AstroPh.txt")

# Print some basic information about the graph
print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())

# Visualize the graph
plt.figure(figsize=(10, 6))
pos = nx.layout.spring_layout(graph, seed=42)
nx.draw_networkx(graph, pos, with_labels=False, node_size=10)
plt.title("Astro Physics Collaboration Network")
plt.axis("off")
plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 25 :
# 25 Erdös–Rényi random graph (G(n, m): Generate a random instance of this model
# by using the number of nodes and edges as the real world graph

n = 18772  # Number of nodes
m = 198110  # Number of edges

# Generate the Erdös-Rényi random graph
graph = nx.gnm_random_graph(n, m)

# Print some basic information about the graph
print("Number of nodes:", graph.number_of_nodes())
print("Number of edges:", graph.number_of_edges())

# Visualize the graph
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(graph, seed=42)
nx.draw_networkx(graph, pos, with_labels=False, node_size=10)
plt.title("Erdös-Rényi Random Graph")
plt.axis("off")
plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------

# problem 26:
# 26 Configuration model random graph: Generate a random instance of this model
# by using the graph in the dataset.

# Erdös–Rényi graph
n = graph.number_of_nodes()
m = graph.number_of_edges()
erdos_renyi_graph = nx.gnm_random_graph(n, m)

# Configuration Model graph
degree_sequence = [degree for (node, degree) in graph.degree()]
configuration_model_graph = nx.configuration_model(degree_sequence)

# Degree distributions
real_world_degree_sequence = [degree for node, degree in graph.degree()]
erdos_renyi_degree_sequence = [degree for node, degree in erdos_renyi_graph.degree()]
configuration_model_degree_sequence = [degree for node, degree in configuration_model_graph.degree()]

# Plot degree distributions
plt.figure(figsize=(10, 6))

plt.hist(real_world_degree_sequence, bins=50, alpha=0.5, label='Real World')
plt.hist(erdos_renyi_degree_sequence, bins=50, alpha=0.5, label='Erdös-Rényi')
plt.hist(configuration_model_degree_sequence, bins=50, alpha=0.5, label='Configuration Model')

plt.title('Degree Distributions')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.legend()

plt.show()


# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 27:
# 27 Degree distributions

# Shortest path length distributions
real_world_shortest_path_lengths = nx.shortest_path_length(graph)
shortest_path_lengths = [length for source in real_world_shortest_path_lengths for length in source[1].values()]

# Plot shortest path length distribution
plt.figure(figsize=(10, 6))

plt.hist(shortest_path_lengths, bins=50, alpha=0.5)

plt.title('Shortest Path Length Distribution')
plt.xlabel('Shortest Path Length')
plt.ylabel('Frequency')

plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 28
# 28 Shortest path length distributions

# Clustering coefficient distributions
clustering_coefficients = list(nx.clustering(graph).values())

# Plot clustering coefficient distribution
plt.figure(figsize=(10, 6))

plt.hist(clustering_coefficients, bins=50, alpha=0.5)

plt.title('Clustering Coefficient Distribution')
plt.xlabel('Clustering Coefficient')
plt.ylabel('Frequency')

plt.show()

# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# ---------------------------------
# problem 29
# 29 Clustering coefficient distributions

# Connected Components (CC) size distributions
cc_sizes = [len(cc) for cc in nx.connected_components(graph)]

# Plot CC size distribution
plt.figure(figsize=(10, 6))

plt.hist(cc_sizes, bins=50, alpha=0.5)

plt.title('Connected Components Size Distribution')
plt.xlabel('CC Size')
plt.ylabel('Frequency')

plt.show()