"""
Unit tests for Out of Boundary Paths Grid Movement 1D DP
"""
from algorithms.practice.dynamic_programming_1d.out_of_boundary_paths import solve_out_of_boundary_paths

def test_out_of_boundary_paths_base():
    assert solve_out_of_boundary_paths() is True
    assert solve_out_of_boundary_paths([3, 1, 2]) == [1, 2, 3]

def test_out_of_boundary_paths_edge_cases():
    assert solve_out_of_boundary_paths("") == ""
    assert solve_out_of_boundary_paths(0) is True
    assert solve_out_of_boundary_paths(-5) is False
