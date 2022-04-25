import networkx as nx
from pyvis.network import Network
from random import uniform, sample, choice
import itertools

# Erdős–Rényi models
def ER_model_Gnp(number_of_nodes=100, edge_probability=.01):
    g = nx.Graph()
    g.add_nodes_from(range(number_of_nodes))
    for el in itertools.combinations(range(number_of_nodes), 2):
        if uniform(0, 1) < edge_probability:
            g.add_edge(*el)
    return g

def ER_model_GnM(number_of_nodes=100, number_of_edges=100): # clearly number_of_edges has to be <= n(n-1)/2
    g = nx.Graph()
    g.add_nodes_from(range(number_of_nodes))
    sampled_edges = sample([pair for pair in itertools.combinations(range(number_of_nodes), 2)], number_of_edges)
    g.add_edges_from(sampled_edges)
    return g
    
# Watts–Strogatz model
def WS_model(number_of_nodes=100, mean_degree=6, beta=0.01): 
    # number_of_nodes >> mean degree >> log(number of nodes) >> 1 
    # beta between 0 and 1
    # mean degree has to be an even integer
    g = nx.Graph()
    g.add_nodes_from(range(number_of_nodes))
    for i, j in itertools.combinations(range(number_of_nodes), 2):
        if abs(i-j) % (number_of_nodes - 1 - mean_degree/2) <= mean_degree/2:
            g.add_edge(*(i, j))
    for i in g.nodes:
        for j in range(i+1, i+1+int(mean_degree/2)):
            if uniform(0, 1) < beta:
                g.remove_edge(i, j % number_of_nodes)
                neighbors = list(g.neighbors(i))
                neighbors.append(i)
                g.add_edge(*(i, choice(list(set(g.nodes)-set(neighbors)))))
    return g        

# Barabási-Albert model
def BA_model(number_of_nodes=30, alpha=1.):
    g = nx.Graph()
    g.add_nodes_from(range(2))
    g.add_edge(*(0, 1))
    while g.number_of_nodes() < number_of_nodes:
        den = sum([g.degree(node)**alpha for node in g.nodes])
        probabilities = [g.degree(node)**alpha/den for node in g.nodes]
        new_node = g.number_of_nodes() # label of new node
        g.add_node(new_node)
        for i in range(new_node):
            if uniform(0, 1) < probabilities[i]:
                g.add_edge(*(new_node, i))
    return g
   
g = WS_model()

net = Network('1000px', '2000px')
net.from_nx(g)
net.show("my_graph.html")

# compute and visualize some metrics, like:
# - expected degree of the node i at the j-th iteration
# - number of isolated nodes
# - growth of number of edges 
# - degree distribution

# allow auto loops when it is possible
# allow nodes with a clearly opposite behaviour and study the changes in the model