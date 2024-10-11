import networkx as nx
import matplotlib.pyplot as plt

# Aqui criei o grafo
G = nx.Graph()

#Montando as arestas e os pesos. 
#Como os pesos era o custo com a distancia, so precisei multiplicar custo X distancia 
G.add_edge('A', 'B', weight=20)
G.add_edge('A', 'C', weight=30)
G.add_edge('B', 'D', weight=18)
G.add_edge('C', 'D', weight=14)
G.add_edge('B', 'E', weight=15)
G.add_edge('D', 'E', weight=20)
G.add_edge('D', 'F', weight=18)
G.add_edge('E', 'G', weight=16)
G.add_edge('F', 'G', weight=15)

#procura o menor caminho no grafo
caminho = nx.shortest_path(G, 'A', target='G')


# Vai Calcula a soma dos pesos das arestas do caminho mais curto que vai 
# percorrendo cada par de nós que está representado por 'u' e 'v' no caminho e 
# vai somando os valores dos pesos das arestas.
soma_das_arestas = sum(G[u][v]['weight'] for u, v in zip(caminho[:-1], caminho[1:]))

print("O caminho mais perto é de: ", caminho)
print("O custo total é de: ", soma_das_arestas)


pos = nx.spring_layout(G) #aqui é as posições do no
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold')
dk = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=dk)
plt.show()


