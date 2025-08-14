"""Floyd-Warshall dynamic programming all-pairs shortest paths."""
from typing import List

def floyd_warshall(matrix: List[List[float]]) -> List[List[float]]:
    n = len(matrix)
    dist = [list(row) for row in matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
