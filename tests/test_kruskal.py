from algorithms.graphs.kruskal import kruskal_mst

def test_kruskal():
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
    weight, mst = kruskal_mst(4, edges)
    assert weight == 19
