from algorithms.graphs.bellman_ford import bellman_ford
import pytest

def test_bellman_ford():
    edges = [(0, 1, 1), (1, 2, 2), (2, 3, -1)]
    d = bellman_ford(4, edges, 0)
    assert d[3] == 2
    with pytest.raises(ValueError):
        bellman_ford(3, [(0, 1, 1), (1, 2, -3), (2, 0, 1)], 0)
