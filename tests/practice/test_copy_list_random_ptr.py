"""
Unit tests for Copy List with Random Pointer O1 Space
"""
from algorithms.practice.linked_lists.copy_list_random_ptr import solve_copy_list_random_ptr

def test_copy_list_random_ptr_base():
    assert solve_copy_list_random_ptr() is True
    assert solve_copy_list_random_ptr([3, 1, 2]) == [1, 2, 3]

def test_copy_list_random_ptr_edge_cases():
    assert solve_copy_list_random_ptr("") == ""
    assert solve_copy_list_random_ptr(0) is True
    assert solve_copy_list_random_ptr(-5) is False
