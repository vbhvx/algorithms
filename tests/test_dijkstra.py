from algorithms.graphs.dijkstra import dijkstra

def test_dijkstra():
    edges = [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1), (2, 3, 5)]
    d = dijkstra(4, edges, 0)
    assert d[3] == 4
