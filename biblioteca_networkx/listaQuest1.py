import networkx as nx
import matplotlib.pyplot as plt

# Cria um grafo não direcionado
G = nx.Graph()

# Adiciona os nós
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_node("D")
G.add_node("E")

# Adiciona as arestas
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("C", "D")
G.add_edge("D", "E")

# Desenha o grafo usando o layout circular
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16, font_weight='bold')

# Mostra o grafo
plt.show()
