import bisect
import random
from networkx import MultiDiGraph

def scale_free_graph(n, alpha=0.41,beta=0.54,delta_in=0.2,delta_out=0):
    def _choose_node(G,distribution,delta):
        cumsum = 0.0
        psum = float(sum(distribution.values()))+float(delta)*len(distribution)
        r = random.random()
        for i in range(0, len(distribution)):
            cumsum += (distribution[i]+delta)/psum
            if r < cumsum:
                break
        return i

    G = MultiDiGraph()
    G.add_edges_from([(0,1),(1,2),(2,0)])
    gamma = 1 - alpha - beta

    while len(G)<n:
        r = random.random()
        if r < alpha:
            v = len(G)
            w = _choose_node(G, G.in_degree(),delta_in)
        elif r < alpha+beta:
            v = _choose_node(G, G.out_degree(),delta_out)
            w = _choose_node(G, G.in_degree(),delta_in)
        else:
            v = _choose_node(G, G.out_degree(),delta_out)
            w = len(G)
        G.add_edge(v,w)
    return G
