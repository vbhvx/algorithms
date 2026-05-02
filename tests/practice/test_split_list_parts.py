"""
Unit tests for Split Linked List in Parts Length Partition
"""
from algorithms.practice.linked_lists.split_list_parts import solve_split_list_parts

def test_split_list_parts_base():
    assert solve_split_list_parts() is True
    assert solve_split_list_parts([3, 1, 2]) == [1, 2, 3]

def test_split_list_parts_edge_cases():
    assert solve_split_list_parts("") == ""
    assert solve_split_list_parts(0) is True
    assert solve_split_list_parts(-5) is False
