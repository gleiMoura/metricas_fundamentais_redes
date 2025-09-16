import networkx as nx
import matplotlib.pyplot as plt

#Carregar rede de txt
G=nx.read_edgelist('citation.edgelist.txt')

print("Número de Nós:", G.number_of_nodes()) #Calcula número de nós
print("Número de Arestas:", G.number_of_edges()) #Calcula número de arestas
print("Direcionada?", G.is_directed())#Verifica se é direcionada
print("Densidade:", nx.density(G)) #Calcula densidade
print("Número de Componentes Conexos:", nx.number_connected_components(G)) #Calcula número de componentes conexos
#
#
print("Grau médio:", sum(dict(G.degree()).values()) / G.number_of_nodes()) #Calcula grau médio
print("Comprimento médio do caminho:", nx.average_shortest_path_length(G)) #Calcula comprimento médio do caminho

if nx.is_connected(G):
    caminho_medio = nx.average_shortest_path_length(G)
    print("O grafo é conexo. Comprimento médio do caminho:", caminho_medio)
else:
    print("O grafo não é conexo. Comprimento médio do caminho não pode ser calculado.")
