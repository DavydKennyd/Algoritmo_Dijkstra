import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()

edges = [
    ('A', 'B', 10),
    ('A', 'C', 15),
    ('B', 'D', 12),
    ('C', 'D', 10),
    ('B', 'E', 15),
    ('D', 'E', 2),
    ('D', 'F', 5),
    ('E', 'F', 5)  
]

G.add_weighted_edges_from(edges)
caminho = nx.dijkstra_path(G, source='A', target='F')
resultado = nx.dijkstra_path_length(G, source='A', target='F')


print('Caminho mais curto de A até F:')
print(caminho)
print('Distância total do caminho mais curto: ')
print(resultado)



pos = nx.spring_layout(G) # Layout para a visualização
nx.draw(G, pos, with_labels=True, node_color='lightgreen')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

