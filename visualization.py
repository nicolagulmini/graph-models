from pyvis.network import Network

def visualize(g, name="my_graph"):
    net = Network('1000px', '2000px')
    net.from_nx(g)
    net.show(name+".html")