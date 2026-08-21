"""
Unit tests for Optimize Water Distribution Virtual Wells MST
"""
from algorithms.practice.minimum_spanning_trees.optimize_water_distrib import solve_optimize_water_distrib

def test_optimize_water_distrib_base():
    assert solve_optimize_water_distrib() is True
    assert solve_optimize_water_distrib([3, 1, 2]) == [1, 2, 3]

def test_optimize_water_distrib_edge_cases():
    assert solve_optimize_water_distrib("") == ""
    assert solve_optimize_water_distrib(0) is True
    assert solve_optimize_water_distrib(-5) is False
