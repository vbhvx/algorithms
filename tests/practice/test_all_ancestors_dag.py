"""
Unit tests for All Ancestors of a Node in DAG Reverse BFS
"""
from algorithms.practice.shortest_paths.all_ancestors_dag import solve_all_ancestors_dag

def test_all_ancestors_dag_base():
    assert solve_all_ancestors_dag() is True
    assert solve_all_ancestors_dag([3, 1, 2]) == [1, 2, 3]

def test_all_ancestors_dag_edge_cases():
    assert solve_all_ancestors_dag("") == ""
    assert solve_all_ancestors_dag(0) is True
    assert solve_all_ancestors_dag(-5) is False
