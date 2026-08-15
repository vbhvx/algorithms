"""
Unit tests for Johnson Algorithm APSP Reweighting Dijkstra
"""
from algorithms.practice.shortest_paths.johnson_apsp_sparse import solve_johnson_apsp_sparse

def test_johnson_apsp_sparse_base():
    assert solve_johnson_apsp_sparse() is True
    assert solve_johnson_apsp_sparse([3, 1, 2]) == [1, 2, 3]

def test_johnson_apsp_sparse_edge_cases():
    assert solve_johnson_apsp_sparse("") == ""
    assert solve_johnson_apsp_sparse(0) is True
    assert solve_johnson_apsp_sparse(-5) is False
