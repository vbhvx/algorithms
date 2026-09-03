"""
Unit tests for Maximum Weight Closure in Directed Graph
"""
from algorithms.practice.network_flow_matching.maximum_weight_closure import solve_maximum_weight_closure

def test_maximum_weight_closure_base():
    assert solve_maximum_weight_closure() is True
    assert solve_maximum_weight_closure([3, 1, 2]) == [1, 2, 3]

def test_maximum_weight_closure_edge_cases():
    assert solve_maximum_weight_closure("") == ""
    assert solve_maximum_weight_closure(0) is True
    assert solve_maximum_weight_closure(-5) is False
