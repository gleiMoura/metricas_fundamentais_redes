import networkx as nx
import matplotlib.pyplot as plt

G=nx.read_edgelist('citation.edgelist.txt')

graus = dict(G.degree())

print("Grau médio:", sum(graus.values()) / G.number_of_nodes()) #Calcula grau médio

#Verifica se o grafo é conexo antes de calcular o comprimento médio do caminho
if nx.is_connected(G):
    caminho_medio = nx.average_shortest_path_length(G)
    print("O grafo é conexo. Comprimento médio do caminho:", caminho_medio)
else:
    print("O grafo não é conexo. Comprimento médio do caminho não pode ser calculado.")

#histograma de distribuição de grau
plt.hist(list(graus.values()), bins=20, color="skyblue", edgecolor="black")
plt.xlabel("Grau")
plt.ylabel("Frequência")
plt.title("Distribuição de Grau")
plt.savefig("distribuicao_grau.png")
#Analisando a imagem verificamos que a maioria dos nós tem grau baixo, enquanto poucos nós têm grau muito alto, caracterizando uma distribuição de grau típica de redes complexas.


#Verifica se é lei de potência
plt.figure()
plt.hist(graus.values(), bins=100, color="skyblue", edgecolor="black")
plt.yscale("log")
plt.xscale("log")
plt.xlabel("Grau (log)")
plt.ylabel("Frequência (log)")
plt.title("Distribuição de Grau (Escala Log-Log)")
plt.savefig("distribuicao_grau_loglog.png")
#Imagem indica que o grafo segue uma distribuição de lei de potência, típica de redes complexas, onde poucos nós têm muitos links e muitos nós têm poucos links.

#clusterização local de cada nó
clustering_local = nx.clustering(G)
print("Clusterização do nó 5:", clustering_local[5])

#clusterização global que mede a proporção de triângulos na rede
transitividade = nx.transitivity(G)
print("Transitividade (Clusterização Global):", transitividade)