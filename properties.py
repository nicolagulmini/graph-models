'''
Another important characteristic of scale-free networks is the 
clustering coefficient distribution, which decreases as the node 
degree increases. This distribution also follows a power law. 
This implies that the low-degree nodes belong to very dense 
sub-graphs and those sub-graphs are connected to each other 
through hubs. 

Consider a social network in which nodes are 
people and links are acquaintance relationships between people. 
It is easy to see that people tend to form communities, i.e., 
small groups in which everyone knows everyone (one can think of 
such community as a complete graph). In addition, the members of 
a community also have a few acquaintance relationships to people 
outside that community. Some people, however, are connected to a 
large number of communities (e.g., celebrities, politicians). 
Those people may be considered the hubs responsible for the 
small-world phenomenon.

Properties of random graph may change or remain invariant under 
graph transformations. Mashaghi A. et al., for example, demonstrated 
that a transformation which converts random graphs to their edge-dual 
graphs (or line graphs) produces an ensemble of graphs with nearly 
the same degree distribution, but with degree correlations and a 
significantly higher clustering coefficient. Scale free graphs, 
as such, remain scale free under such transformations.
'''

import networkx as nx
import matplotlib.pyplot as plt
from visualization import visualize
import models

# g = models.BA_model(number_of_nodes=1000, alpha=.1)
g = nx.barabasi_albert_graph(n=1000, m=2)
# visualize(g, name="test")
degree_dist = nx.degree_histogram(g)
clustering_coeffs = nx.clustering(g).values()

'''
Clustering coefficient is a measure of the degree to which nodes 
in a graph tend to cluster together.
'''

g_complement = nx.complement(g)
# visualize(g_complement, name="complement")
degree_dist_complement = nx.degree_histogram(g_complement)
clustering_coeffs_comp = nx.clustering(g_complement).values()

plt1 = plt.figure('Degree distributions')
plt.plot(range(len(degree_dist)), degree_dist)
plt.plot(range(len(degree_dist_complement)), degree_dist_complement)
plt.xscale('log')
plt.yscale('log')

plt2 = plt.figure('Clustering coeff distribution')
plt.hist(clustering_coeffs)

plt3 = plt.figure('Clustering coeff distribution for complement')
plt.hist(clustering_coeffs_comp)