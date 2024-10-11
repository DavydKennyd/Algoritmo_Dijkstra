import networkx as nx
import matplotlib.pyplot as plt

#LISTA 03

# ---------- QUESTÃ 01 ----------

"""G = nx.Graph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

G.add_edges_from([
     ('A', 'B', {'weight' : 10}),
     ('A', 'C', {'weight' : 15}),
     ('B', 'D', {'weight' : 12}),
     ('C', 'D', {'weight' : 10}),
     ('B', 'E', {'weight' : 15}),
     ('D', 'E', {'weight' : 2}),
     ('D', 'F', {'weight' : 5}),
     ('E', 'F', {'weight' : 5}),
 ])

# # Layout para a visualização
pos = nx.spring_layout(G) 

 #Edição visual do Grafo
nx.draw(G, pos, with_labels=True, node_color='lightgreen')

 #Seleção dos atributos nas arestas
edge_labels = nx.get_edge_attributes(G, 'weight')

#Calculando o menor caminho
menor_caminho = nx.shortest_path(G, 'A', 'F', weight= 'weight')
peso_arestas = nx.shortest_path_length(G, 'A', 'F', weight= 'weight')

# #Mostrando a menor rota de A para F
print(f'O menor caminho de A até F é: {menor_caminho}, Com a distancia de {peso_arestas} KM')

# #Finalização e exibição do Grafo
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show() """

# ---------- QUESTÃ 02 ----------

"""G = nx.Graph()

G.add_nodes_from(['S1', 'S2', 'S3', 'S4'])

G.add_edges_from([
     ('S1', 'S2', {'weight' : 20}),
     ('S1', 'S3', {'weight' : 50}),
     ('S2', 'S3', {'weight' : 30}),
     ('S2', 'S4', {'weight' : 10}),
     ('S3', 'S4', {'weight' : 20})
 ])

# # Layout para a visualização
pos = nx.spring_layout(G)

# # Edição visual do grafo completo
nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold')

# # Seleção dos atributos nas arestas (pesos)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de Dijkstra para encontrar o caminho mais rápido de S1 até S4
shortest_path = nx.shortest_path(G, 'S1', 'S4', weight='weight')
path_length = nx.shortest_path_length(G, 'S1', 'S4', weight='weight')

# # Exibindo o caminho mais rápido e o tempo total
print(f"O caminho mais rápido de S1 até S4 é: {shortest_path} com tempo total: {path_length}ms")

# # Exibição do grafo com o caminho mais rápido destacado
plt.show()"""

# ---------- QUESTÃ 03 ----------

G = nx.Graph()

G.add_nodes_from(['A', 'B', 'C', 'D', 'F'])

G.add_edges_from([
     ('A', 'B', {'weight' : 5}),
     ('A', 'C', {'weight' : 7}),
     ('B', 'D', {'weight' : 3}),
     ('C', 'D', {'weight' : 8}),
     ('B', 'E', {'weight' : 10}),
     ('D', 'E', {'weight' : 2}),
     ('E', 'F', {'weight' : 4}),
 ])


# # Layout para a visualização
pos = nx.spring_layout(G)

# Edição visual do grafo completo
nx.draw(G, pos, with_labels=True, node_color='lightgreen', font_weight='bold')

# # Seleção dos atributos nas arestas (pesos)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de Dijkstra para encontrar o caminho mais rápido de S1 até S4
shortest_path = nx.shortest_path(G, 'A', 'F', weight='weight')
path_length = nx.shortest_path_length(G, 'A', 'F', weight='weight')

# # Exibindo o caminho mais rápido e o tempo total
print(f"O caminho mais rápido de A até F é: {shortest_path} com tempo total: {path_length} min")

# # Exibição do grafo com o caminho mais rápido destacado
plt.show()


# ---------- QUESTÃ 04 ----------

# import networkx as nx
# import matplotlib.pyplot as plt

# # Criação do grafo ponderado
# G = nx.Graph()

# # Adição de nós (cidades)
# G.add_nodes_from(['X', 'Y', 'W', 'Z'])

# # Adição de arestas ponderadas (custos das rotas)
# G.add_edges_from([
#     ('X', 'Y', {'weight': 200}),
#     ('X', 'W', {'weight': 300}),
#     ('Y', 'Z', {'weight': 100}),
#     ('W', 'Z', {'weight': 150}),
#     ('Y', 'W', {'weight': 50})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo completo
# nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')

# # Seleção dos atributos nas arestas (custos)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de Dijkstra para encontrar a rota mais barata de X até Z
# shortest_path = nx.shortest_path(G, source='X', target='Z', weight='weight')
# path_length = nx.shortest_path_length(G, source='X', target='Z', weight='weight')

# # Exibindo a rota mais barata e o custo total
# print(f"A rota mais barata de X até Z é: {shortest_path} com custo total: ${path_length}")

# # Destaque visual da rota mais barata
# path_edges = list(zip(shortest_path, shortest_path[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# # Exibição do grafo com a rota mais barata destacada
# plt.show()


# ---------- QUESTÃ 05 ----------

# import networkx as nx
# import matplotlib.pyplot as plt

# # Criação do grafo ponderado
# G = nx.Graph()

# # Adição de nós (estações de carregamento)
# G.add_nodes_from(['P1', 'P2', 'P3', 'P4', 'P5'])

# # Adição de arestas ponderadas (distâncias em metros)
# G.add_edges_from([
#     ('P1', 'P2', {'weight': 30}),
#     ('P1', 'P3', {'weight': 40}),
#     ('P2', 'P3', {'weight': 25}),
#     ('P2', 'P4', {'weight': 50}),
#     ('P3', 'P4', {'weight': 20}),
#     ('P3', 'P5', {'weight': 35}),
#     ('P4', 'P5', {'weight': 15})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo completo
# nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')

# # Seleção dos atributos nas arestas (distâncias)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de Dijkstra para encontrar a menor distância de P1 até P5
# shortest_path = nx.shortest_path(G, source='P1', target='P5', weight='weight')
# path_length = nx.shortest_path_length(G, source='P1', target='P5', weight='weight')

# # Exibindo a menor distância e o caminho
# print(f"O menor caminho de P1 até P5 é: {shortest_path} com distância total: {path_length}m")

# # Destaque visual do caminho mais curto
# path_edges = list(zip(shortest_path, shortest_path[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# # Exibição do grafo com o caminho mais curto destacado
# plt.show()


# ---------- QUESTÃ 09 ----------

# # Criação do grafo direcionado
# G = nx.DiGraph()

# # Adição de nós (cidades)
# G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# # Adição de arestas direcionadas com pesos (tempos de viagem em minutos)
# G.add_edges_from([
#     ('A', 'B', {'weight': 20}),
#     ('A', 'C', {'weight': 30}),
#     ('B', 'C', {'weight': 25}),
#     ('B', 'D', {'weight': 15}),
#     ('C', 'D', {'weight': 10}),
#     ('D', 'E', {'weight': 5})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo completo
# nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', arrows=True)

# # Seleção dos atributos nas arestas (tempos)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de Dijkstra para encontrar a rota mais rápida de A até E
# shortest_path = nx.shortest_path(G, source='A', target='E', weight='weight')
# path_length = nx.shortest_path_length(G, source='A', target='E', weight='weight')

# # Exibindo a rota mais rápida e o tempo total
# print(f"A rota mais rápida de A até E é: {shortest_path} com tempo total: {path_length} minutos")

# # Destaque visual da rota mais rápida
# path_edges = list(zip(shortest_path, shortest_path[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# # Exibição do grafo com a rota mais rápida destacada
# plt.show()
