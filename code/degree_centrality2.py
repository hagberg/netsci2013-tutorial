import networkx as nx

def degree_centrality(G):

    centrality = {} # empty dictionary
    n = len(G) - 1.
    for v in G:
       centrality[v] = G.degree(v)/n
    return centrality

G = nx.star_graph(3)
dc = degree_centrality(G)
for v in dc:
    print v,dc[v]
# 0 1.0
# 1 0.333333333333
# 2 0.333333333333
# 3 0.333333333333
print dc
# {0: 1.0, 1: 0.33333, 2: 0.33333, 3: 0.33333}
