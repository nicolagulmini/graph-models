from pyvis.network import Network

def visualize(g):
    net = Network('1000px', '2000px')
    net.from_nx(g)
    net.show("my_graph.html")