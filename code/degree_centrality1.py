import networkx as nx

def degree_centrality(G):

    n = len(G) - 1.0 # forces floating point for n
    for v in G:
        print v,G.degree(v)/n

    return

G = nx.star_graph(3)
degree_centrality(G)
# 0 1.0
# 1 0.333333333333
# 2 0.333333333333
# 3 0.333333333333
