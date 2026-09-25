"""
Unit tests for Unique Paths II Obstacle Avoidance
"""
from algorithms.practice.dynamic_programming_2d.unique_paths_ii_obs import solve_unique_paths_ii_obs

def test_unique_paths_ii_obs_base():
    assert solve_unique_paths_ii_obs() is True
    assert solve_unique_paths_ii_obs([3, 1, 2]) == [1, 2, 3]

def test_unique_paths_ii_obs_edge_cases():
    assert solve_unique_paths_ii_obs("") == ""
    assert solve_unique_paths_ii_obs(0) is True
    assert solve_unique_paths_ii_obs(-5) is False
