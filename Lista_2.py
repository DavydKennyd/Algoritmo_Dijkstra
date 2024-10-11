import networkx as nx
import matplotlib.pyplot as plt

#---------------------------------------------Questão 01

# #Cria um grafo vazio
# G = nx.Graph()

# #Adição de nós no grafo
# G.add_nodes_from(['A', 'B', 'C', 'D'])

# #Adição de arestas aos grafo
# G.add_edges_from([
#     ('A', 'B', {'weight' : 1 }),
#     ('B', 'C', {'weight' : 2 }),
#     ('A', 'C', {'weight' : 2 }),
#     ('C', 'D', {'weight' : 1 })
# ])

# Visualizando o grafo ponderado com pesos nas arestas

# # Layout para a visualização
# pos = nx.spring_layout(G) 

# #Edição visual do Grafo
# nx.draw(G, pos, with_labels=True, node_color='lightgreen')

# #Seleção dos atributos nas arestas
# edge_labels = nx.get_edge_attributes(G, 'weight')

# #Finalização e exibição do Grafo
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
# plt.show()

#---------------------------------------Questão 02

# #Criação do grafo 
# G = nx.DiGraph()

# #Adição de nós
# G.add_nodes_from([1, 2, 3, 4, 5])

# #Adição de arestas ponderadas
# G.add_edges_from([
#     (1, 2, {'weight' : 3}),
#     (1, 3, {'weight' : 1}),
#     (2, 4, {'weight' : 1}),
#     (3, 4, {'weight' : 5}),
#     (4, 5, {'weight' : 2})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G) 

# #Edição visual do Grafo
# nx.draw(G, pos, with_labels=True, node_color='lightgreen', arrows = True)

# #Seleção dos atributos nas arestas
# edge_labels = nx.get_edge_attributes(G, 'weight')

# #Finalização e exibição do Grafo
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# #Algoritmo de menor caminho
# menor_caminho = nx.shortest_path(G, 1, 5, weight='weight') #Retorna uma lista de valores

# #Mostrando o menor caminho
# print(menor_caminho)

# plt.show()


#---------------------------------------Questão 03

# import networkx as nx
# import matplotlib.pyplot as plt

# # Criação do grafo não direcionado
# G = nx.Graph()

# # Adição de nós
# G.add_nodes_from(['X', 'Y', 'Z', 'W'])

# # Adição de arestas ponderadas
# G.add_edges_from([
#     ('X', 'Y', {'weight': 2}),
#     ('X', 'Z', {'weight': 5}),
#     ('Y', 'Z', {'weight': 1}),
#     ('Y', 'W', {'weight': 3}),
#     ('Z', 'W', {'weight': 2})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo
# nx.draw(G, pos, with_labels=True, node_color='lightblue')

# # Seleção dos atributos nas arestas
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de menor caminho (usando Dijkstra)
# shortest_path = nx.shortest_path(G, source='X', target='W', weight='weight')

# # Exibindo o menor caminho e o peso total do caminho
# path_length = nx.shortest_path_length(G, source='X', target='W', weight='weight')

# print(f"O menor caminho de X até W é: {shortest_path} com peso total: {path_length}")

# # Exibição do grafo
# plt.show()



#---------------------------------------Questão 04

# import networkx as nx
# import matplotlib.pyplot as plt

# # Criação do grafo direcionado
# G = nx.DiGraph()

# # Adição de nós
# G.add_nodes_from(['A', 'B', 'C', 'D'])

# # Adição de arestas ponderadas
# G.add_edges_from([
#     ('A', 'B', {'weight': 2}),
#     ('B', 'C', {'weight': 3}),
#     ('C', 'D', {'weight': 4}),
#     ('D', 'A', {'weight': 1})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo
# nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)

# # Seleção dos atributos nas arestas
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de menor caminho (usando Dijkstra)
# shortest_path = nx.shortest_path(G, source='A', target='C', weight='weight')

# # Exibindo o menor caminho e o peso total do caminho
# path_length = nx.shortest_path_length(G, source='A', target='C', weight='weight')

# #Exibindo as informações do grafo 
# print(f'Menor caminho: {shortest_path} e Peso: {path_length}')

# # Exibição do grafo
# plt.show()


#---------------------------------------Questão 05

# import networkx as nx
# import matplotlib.pyplot as plt

# # Criação do grafo não direcionado
# G = nx.Graph()

# # Adição de nós
# G.add_nodes_from(['P', 'Q', 'R', 'S'])

# # Adição de arestas ponderadas
# G.add_edges_from([
#     ('P', 'Q', {'weight': 6}),
#     ('P', 'R', {'weight': 2}),
#     ('R', 'Q', {'weight': 1}),
#     ('R', 'S', {'weight': 5}),
#     ('Q', 'S', {'weight': 2})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo
# nx.draw(G, pos, with_labels=True, node_color='lightblue')

# # Seleção dos atributos nas arestas
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de menor caminho de todos os nós até S
# nodes = ['P', 'Q', 'R', 'S']
# menores_caminhos = {}
# pesos_caminhos = {}

# for node in nodes:
#     if node != 'S':
#         path = nx.shortest_path(G, source=node, target='S', weight='weight')
#         path_length = nx.shortest_path_length(G, source=node, target='S', weight='weight')
#         menores_caminhos[node] = path
#         pesos_caminhos[node] = path_length

# # Exibindo os caminhos e custos
# for node in menores_caminhos:
#     print(f"O menor caminho de {node} até S é: {menores_caminhos[node]} com custo total: {pesos_caminhos[node]}")

# # Exibição do grafo
# plt.show()


#---------------------------------------Questão 08

# import networkx as nx
# import matplotlib.pyplot as plt

# # Criação do grafo não direcionado
# G = nx.Graph()

# # Adição de nós
# G.add_nodes_from([1, 2, 3, 4, 5, 6])

# # Adição de arestas ponderadas
# G.add_edges_from([
#     (1, 2, {'weight': 7}),
#     (1, 3, {'weight': 9}),
#     (1, 6, {'weight': 14}),
#     (2, 3, {'weight': 10}),
#     (2, 4, {'weight': 15}),
#     (3, 4, {'weight': 11}),
#     (3, 6, {'weight': 2}),
#     (4, 5, {'weight': 6}),
#     (5, 6, {'weight': 9})
# ])

# # Layout para a visualização
# pos = nx.spring_layout(G)

# # Edição visual do grafo completo
# nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold')

# # Seleção dos atributos nas arestas (pesos)
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Algoritmo de Dijkstra para encontrar o menor caminho de 1 até 5
# shortest_path = nx.shortest_path(G, source=1, target=5, weight='weight')
# path_length = nx.shortest_path_length(G, source=1, target=5, weight='weight')

# # Exibindo o menor caminho e o peso total
# print(f"O menor caminho de 1 até 5 é: {shortest_path} com custo total: {path_length}")

# # Destaque visual do caminho mais curto
# path_edges = list(zip(shortest_path, shortest_path[1:]))
# nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

# # Exibição do grafo com o caminho destacado
# plt.show()


