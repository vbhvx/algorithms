from collections import deque
def is_bipartite(adj):
    color = {}
    for node in adj:
        if node not in color:
            q = deque([node]); color[node] = 0
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if v not in color: color[v] = 1 - color[u]; q.append(v)
                    elif color[v] == color[u]: return False
    return True
