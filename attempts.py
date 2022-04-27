import visualization as vis
import models as m
import networkx as nx
import matplotlib.pyplot as plt

g = m.custom_barabasi(n=100, p_opp=.5, p_m=.5, t=0.5)
vis.visualize(g, name='attempt')

degree_dist = nx.degree_histogram(g)

plt.plot(range(len(degree_dist)), degree_dist)