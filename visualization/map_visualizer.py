import matplotlib.pyplot as plt
import networkx as nx

from simulation.city_graph import city_graph

plt.figure(figsize=(10, 8))

nx.draw(
    city_graph,
    with_labels=True,
    node_size=3000,
    font_size=9
)

plt.show()