import networkx as nx
import matplotlib.pyplot as plt

#Carregar rede de txt
G=nx.read_edgelist('citation.edgelist.txt')

#informações básicas sobre a rede
print("Número de Nós:", G.number_of_nodes()) #Calcula número de nós
print("Número de Arestas:", G.number_of_edges()) #Calcula número de arestas
print("Direcionada?", G.is_directed())#Verifica se é direcionada
print("Densidade:", nx.density(G)) #Calcula densidade
print("Número de Componentes Conexos:", nx.number_connected_components(G)) #Calcula número de componentes conexos
