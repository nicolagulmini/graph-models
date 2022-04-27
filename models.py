import networkx as nx
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

def custom_barabasi(n=50, alpha=.1, p_opp=.1, p_m=.1, p_c=.1):
    '''
    This model is based on the Barabasi Albert one, but
    p_opp = probability to swap the preferential attachment of a node
    p_m = probability for a node to be removed for each iteration
    p_c = probability for an edge to be changed into another random one
    '''
    g = nx.Graph()
    g.add_nodes_from(range(2))
    g.add_edge(*(0, 1))
    while g.number_of_nodes() < n:
        den = sum([g.degree(node)**alpha for node in g.nodes])
        probabilities = [g.degree(node)**alpha/den for node in g.nodes]
        new_node = g.number_of_nodes() # label of new node
        g.add_node(new_node)
        for i in range(new_node):
            if uniform(0, 1) < probabilities[i]:
                g.add_edge(*(new_node, i))
    return g
    