import networkx as nx
from random import uniform

g = nx.Graph()

g.add_nodes_from(range(2))
g.add_edge(*(0, 1))

# 

# Barabási-Albert model
def BA_model(g, final_number_of_nodes=20, alpha=1.):
    while g.number_of_nodes() < final_number_of_nodes:
        # allow auto loops?
        # allow nodes with a clearly opposite behaviour
        den = sum([g.degree(node)**alpha for node in g.nodes])
        probabilities = [g.degree(node)**alpha/den for node in g.nodes]
        new_node = g.number_of_nodes() # label of new node
        g.add_node(new_node)
        for i in range(new_node):
            if uniform(0, 1) < probabilities[i]:
                g.add_edge(*(new_node, i))
        
BA_model(g)
nx.draw(g, with_labels=True)

# compute and visualize some metrics, like:
# - expected degree of the node i at the j-th iteration
# - number of isolated nodes
# - growth of number of edges 

    