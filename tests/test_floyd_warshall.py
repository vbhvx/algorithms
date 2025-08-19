from algorithms.graphs.floyd_warshall import floyd_warshall

def test_floyd_warshall():
    inf = float('inf')
    mat = [[0, 5, inf, 10], [inf, 0, 3, inf], [inf, inf, 0, 1], [inf, inf, inf, 0]]
    res = floyd_warshall(mat)
    assert res[0][3] == 9
