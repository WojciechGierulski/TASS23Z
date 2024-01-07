# RYSUNEK PODSTAWOWY
# można odkomentować linijki poniżej, żeby wyświetlić krawędzie

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd


df = pd.read_csv('FINANSES_dataset.csv')
G = nx.Graph()

for index, row in df.iterrows():
    G.add_edge(row['Country'], row['Partner'], weight=row['Value'])


# df = pd.read_csv('ORGANIZATIONS_dataset.csv')
# G = nx.Graph()

# for index, row in df.iterrows():
#     G.add_edge(row['country1'], row['country2'], weight=row['degree'])

    

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

pos = nx.spring_layout(G, seed=7)

nx.draw_networkx_nodes(G, pos, node_size=700)
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
# nx.draw_networkx_edges(G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed")
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

edge_labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()
