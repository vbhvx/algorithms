def tarjan_scc(n, adj):
    idx = 0; indices = [-1]*n; low = [-1]*n; on_stack = [False]*n; stack = []; sccs = []
    def strongconnect(u):
        nonlocal idx
        indices[u] = low[u] = idx; idx += 1; stack.append(u); on_stack[u] = True
        for v in adj.get(u, []):
            if indices[v] == -1: strongconnect(v); low[u] = min(low[u], low[v])
            elif on_stack[v]: low[u] = min(low[u], indices[v])
        if low[u] == indices[u]:
            scc = []
            while True:
                w = stack.pop(); on_stack[w] = False; scc.append(w)
                if w == u: break
            sccs.append(scc)
    for i in range(n):
        if indices[i] == -1: strongconnect(i)
    return sccs
