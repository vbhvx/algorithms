"""
Unit tests for Prim Minimum Spanning Tree Indexed MinHeap
"""
from algorithms.practice.minimum_spanning_trees.prim_mst_eager import solve_prim_mst_eager

def test_prim_mst_eager_base():
    assert solve_prim_mst_eager() is True
    assert solve_prim_mst_eager([3, 1, 2]) == [1, 2, 3]

def test_prim_mst_eager_edge_cases():
    assert solve_prim_mst_eager("") == ""
    assert solve_prim_mst_eager(0) is True
    assert solve_prim_mst_eager(-5) is False
