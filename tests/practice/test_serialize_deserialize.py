"""
Unit tests for Serialize and Deserialize Binary Tree BFS
"""
from algorithms.practice.trees_and_bst.serialize_deserialize import solve_serialize_deserialize

def test_serialize_deserialize_base():
    assert solve_serialize_deserialize() is True
    assert solve_serialize_deserialize([3, 1, 2]) == [1, 2, 3]

def test_serialize_deserialize_edge_cases():
    assert solve_serialize_deserialize("") == ""
    assert solve_serialize_deserialize(0) is True
    assert solve_serialize_deserialize(-5) is False
