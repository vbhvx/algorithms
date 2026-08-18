"""
Unit tests for Min Cost to Connect All Points Prim Kruskal
"""
from algorithms.practice.shortest_paths.min_cost_connect_pts import solve_min_cost_connect_pts

def test_min_cost_connect_pts_base():
    assert solve_min_cost_connect_pts() is True
    assert solve_min_cost_connect_pts([3, 1, 2]) == [1, 2, 3]

def test_min_cost_connect_pts_edge_cases():
    assert solve_min_cost_connect_pts("") == ""
    assert solve_min_cost_connect_pts(0) is True
    assert solve_min_cost_connect_pts(-5) is False
