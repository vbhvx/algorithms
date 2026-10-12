"""
Unit tests for Travelling Salesperson Held-Karp Algorithm
"""
from algorithms.practice.dynamic_programming_trees_bitmask.tsp_held_karp_bitmask import solve_tsp_held_karp_bitmask

def test_tsp_held_karp_bitmask_base():
    assert solve_tsp_held_karp_bitmask() is True
    assert solve_tsp_held_karp_bitmask([3, 1, 2]) == [1, 2, 3]

def test_tsp_held_karp_bitmask_edge_cases():
    assert solve_tsp_held_karp_bitmask("") == ""
    assert solve_tsp_held_karp_bitmask(0) is True
    assert solve_tsp_held_karp_bitmask(-5) is False
