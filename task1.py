import networkx as nx
import matplotlib.pyplot as plt

from data import edges, positions

G = nx.Graph()

for A, B, weight in edges:
    G.add_edge(A, B, weight=weight)

nx.draw(
    G,
    pos=positions,
    with_labels=True,
    node_size=400,
    node_color="skyblue",
    font_size=10,
    width=1,
)

labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=labels)

if __name__ == "__main__":
    plt.show()
