import networkx as nx
from pyvis.network import Network
from random import uniform, sample
import itertools

# Erdős–Rényi models
def ER_model_Gnp(number_of_nodes, edge_probability):
    g = nx.Graph()
    g.add_nodes_from(range(number_of_nodes))
    for el in itertools.combinations(range(number_of_nodes), 2):
        if uniform(0, 1) < edge_probability:
            g.add_edge(*el)
    return g

def ER_model_GnM(number_of_nodes, number_of_edges): # clearly number_of_edges has to be <= n(n-1)/2
    g = nx.Graph()
    g.add_nodes_from(range(number_of_nodes))
    sampled_edges = sample([pair for pair in itertools.combinations(range(number_of_nodes), 2)], number_of_edges)
    g.add_edges_from(sampled_edges)
    return g
    
# Watts–Strogatz model
def WS_model(g):
    return

# Barabási-Albert model
def BA_model(g, final_number_of_nodes=30, alpha=1.):
    while g.number_of_nodes() < final_number_of_nodes:
        den = sum([g.degree(node)**alpha for node in g.nodes])
        probabilities = [g.degree(node)**alpha/den for node in g.nodes]
        new_node = g.number_of_nodes() # label of new node
        g.add_node(new_node)
        for i in range(new_node):
            if uniform(0, 1) < probabilities[i]:
                g.add_edge(*(new_node, i))
   

# g = nx.Graph()

# g.add_nodes_from(range(2))
# g.add_edge(*(0, 1))

# BA_model(g)

g = ER_model_GnM(100, 100)

net = Network('1000px', '2000px')
net.from_nx(g)
net.show("my_graph.html")

# compute and visualize some metrics, like:
# - expected degree of the node i at the j-th iteration
# - number of isolated nodes
# - growth of number of edges 
# - degree distribution

# allow auto loops?
# allow nodes with a clearly opposite behaviour