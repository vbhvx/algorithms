"""
Unit tests for Number of Islands Grid Flood Fill
"""
from algorithms.practice.graphs_and_traversals.num_islands_bfs_dfs import solve_num_islands_bfs_dfs

def test_num_islands_bfs_dfs_base():
    assert solve_num_islands_bfs_dfs() is True
    assert solve_num_islands_bfs_dfs([3, 1, 2]) == [1, 2, 3]

def test_num_islands_bfs_dfs_edge_cases():
    assert solve_num_islands_bfs_dfs("") == ""
    assert solve_num_islands_bfs_dfs(0) is True
    assert solve_num_islands_bfs_dfs(-5) is False
