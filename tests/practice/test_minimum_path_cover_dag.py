"""
Unit tests for Minimum Path Cover in Directed Acyclic Graph
"""
from algorithms.practice.network_flow_matching.minimum_path_cover_dag import solve_minimum_path_cover_dag

def test_minimum_path_cover_dag_base():
    assert solve_minimum_path_cover_dag() is True
    assert solve_minimum_path_cover_dag([3, 1, 2]) == [1, 2, 3]

def test_minimum_path_cover_dag_edge_cases():
    assert solve_minimum_path_cover_dag("") == ""
    assert solve_minimum_path_cover_dag(0) is True
    assert solve_minimum_path_cover_dag(-5) is False
