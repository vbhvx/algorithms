"""
Unit tests for All Paths From Source to Target DAG DFS
"""
from algorithms.practice.graphs_and_traversals.all_paths_source_target import solve_all_paths_source_target

def test_all_paths_source_target_base():
    assert solve_all_paths_source_target() is True
    assert solve_all_paths_source_target([3, 1, 2]) == [1, 2, 3]

def test_all_paths_source_target_edge_cases():
    assert solve_all_paths_source_target("") == ""
    assert solve_all_paths_source_target(0) is True
    assert solve_all_paths_source_target(-5) is False
