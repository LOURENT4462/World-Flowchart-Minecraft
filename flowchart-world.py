import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes
nodes = ["World", "Nether", "Resource-world", "Resource-nether", "Resource-end"]
G.add_nodes_from(nodes)

# Add edges
edges = [("World", "Nether"),
         ("Resource-world", "Resource-nether"),
         ("World", "Resource-end"),
         ("Resource-world", "Resource-end")]
G.add_edges_from(edges)

# Define node positions
pos = {
    "World": (0, 1),
    "Nether": (1, 1),
    "Resource-world": (0, 0),
    "Resource-nether": (1, 0),
    "Resource-end": (2, 0.5)
}

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', arrowsize=20, arrowstyle='-|>')

plt.title("World Flowchart - Survival V2 Season 2 (Foxy Network)")
plt.show()