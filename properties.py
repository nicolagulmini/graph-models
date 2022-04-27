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

g = nx.barabasi_albert_graph(n=10, m=3, seed=42)
degree_dist = nx.degree_histogram(g)

plt.plot(range(len(degree_dist)), degree_dist)

g_transform = nx.random_reference(g)
degree_dist_transform = nx.degree_histogram(g_transform)
plt.plot(range(len(degree_dist_transform)), degree_dist_transform)

g_lattice = nx.lattice_reference(g)
degree_dist_lattice = nx.degree_histogram(g_lattice)
plt.plot(range(len(degree_dist_lattice)), degree_dist_lattice)

plt.show()

sigma = nx.sigma(g)
omega = nx.omega(g)

sigma_t = nx.sigma(g_transform)
omega_t = nx.omega(g_transform)

sigma_l = nx.sigma(g_lattice)
omega_l = nx.omega(g_lattice)

print(sigma, omega)
print(sigma_t, omega_t)
print(sigma_l, omega_l)

