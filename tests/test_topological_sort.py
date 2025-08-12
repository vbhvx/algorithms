from algorithms.graphs.topological_sort import topological_sort_kahn
import pytest

def test_topological_sort():
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = topological_sort_kahn(6, edges)
    assert order.index(5) < order.index(2) and order.index(2) < order.index(3)
    with pytest.raises(ValueError):
        topological_sort_kahn(2, [(0, 1), (1, 0)])
