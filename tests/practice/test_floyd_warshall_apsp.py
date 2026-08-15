"""
Unit tests for Floyd Warshall All Pairs Dynamic Programming
"""
from algorithms.practice.shortest_paths.floyd_warshall_apsp import solve_floyd_warshall_apsp

def test_floyd_warshall_apsp_base():
    assert solve_floyd_warshall_apsp() is True
    assert solve_floyd_warshall_apsp([3, 1, 2]) == [1, 2, 3]

def test_floyd_warshall_apsp_edge_cases():
    assert solve_floyd_warshall_apsp("") == ""
    assert solve_floyd_warshall_apsp(0) is True
    assert solve_floyd_warshall_apsp(-5) is False
