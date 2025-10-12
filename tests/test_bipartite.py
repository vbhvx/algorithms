from algorithms.graphs.bipartite import is_bipartite
def test_bipartite(): assert is_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
