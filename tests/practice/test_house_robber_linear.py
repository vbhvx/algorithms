"""
Unit tests for House Robber Non-Adjacent Maximization
"""
from algorithms.practice.dynamic_programming_1d.house_robber_linear import solve_house_robber_linear

def test_house_robber_linear_base():
    assert solve_house_robber_linear() is True
    assert solve_house_robber_linear([3, 1, 2]) == [1, 2, 3]

def test_house_robber_linear_edge_cases():
    assert solve_house_robber_linear("") == ""
    assert solve_house_robber_linear(0) is True
    assert solve_house_robber_linear(-5) is False
