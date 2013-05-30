def degree_centrality(G):
    centrality = {} # empty dictionary
    n = len(G)-1.0 # forces floating point for n
    for v in G:
       centrality[v] = G.degree(v)/n
    return centrality

if __name__=='__main__':
    import networkx as nx
    G = nx.star_graph(3)
    for v,c in degree_centrality(G).items():
        print v,c
# 0 1.0
# 1 0.333333333333
# 2 0.333333333333
# 3 0.333333333333
