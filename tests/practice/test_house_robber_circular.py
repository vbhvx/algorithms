"""
Unit tests for House Robber II Circular Boundary Split
"""
from algorithms.practice.dynamic_programming_1d.house_robber_circular import solve_house_robber_circular

def test_house_robber_circular_base():
    assert solve_house_robber_circular() is True
    assert solve_house_robber_circular([3, 1, 2]) == [1, 2, 3]

def test_house_robber_circular_edge_cases():
    assert solve_house_robber_circular("") == ""
    assert solve_house_robber_circular(0) is True
    assert solve_house_robber_circular(-5) is False
