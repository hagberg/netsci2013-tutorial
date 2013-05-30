def fast_gnp_random_graph(n, p):
    G = empty_graph(n)
    G.name="fast_gnp_random_graph(%s,%s)"%(n,p)

    if not seed is None:
        random.seed(seed)

    if p <= 0 or p >= 1:
        return nx.gnp_random_graph(n,p)

    v = 1  # Nodes in graph are from 0,n-1
    w = -1
    lp = math.log(1.0 - p)  
    while v < n:
        lr = math.log(1.0 - random.random())
        w = w + 1 + int(lr/lp)
        while w >= v and v < n:
            w = w - v
            v = v + 1
        if v < n:
            G.add_edge(v, w)
    return G


