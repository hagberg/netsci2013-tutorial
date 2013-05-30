from itertools import combinations
from random import random
def gnp_random_graph(n, p):
    G=empty_graph(n)  # NetworkX
    edges=combinations(range(n),2)
    for e in edges:
        if random() < p:        
            G.add_edge(*e) # NetworkX
    return G
