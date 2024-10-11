import networkx as nx
import matplotlib.pyplot as plt

# Criação de um grafo direcionado, pois algumas ruas são de mão única.
G = nx.DiGraph()

# Adicionando arestas com pesos que dessa vez será o tempo de deslocamento
G.add_edge('F1', 'F2', weight=12)  # essa daqui é de Mão única
G.add_edge('F2', 'F3', weight=10)  # essa daqui é de Mão única
G.add_edge('F2', 'F4', weight=7)   # essa daqui é de Mão dupla
G.add_edge('F3', 'F5', weight=15)  # essa daqui é de Mão única
G.add_edge('F4', 'F5', weight=5)   # essa daqui é de Mão única
G.add_edge('F5', 'F6', weight=10)  # essa daqui é de Mão única

# Encontrando o caminho mais curto de F1 até F6
caminho = nx.shortest_path(G, source='F1', target='F6', weight='weight')
# Aqui vai ser do mesmo jeito da questão anterior, vai Calcula a soma dos pesos das arestas do caminho mais curto que vai 
# percorrendo cada par de nós que está representado por 'u' e 'v' no caminho e 
# vai somando os valores dos pesos das arestas.
soma_das_arestas = sum(G[u][v]['weight'] for u, v in zip(caminho[:-1], caminho[1:]))

#Aqui eu exibo no terminal os rsultados
print("O caminho mais rápido de F1 até F6 é:", caminho)
print("O tempo total de deslocamento é de:", soma_das_arestas, "minutos")


pos = nx.spring_layout(G)  # Aqui é as posições dos nós 
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold')
rt = nx.get_edge_attributes(G, 'weight')  # Aqui são os pesos das arestas, ou seja, os atributos
nx.draw_networkx_edge_labels(G, pos, edge_labels=rt)
plt.show()
