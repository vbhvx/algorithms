"""
Unit tests for Insertion Sort List Pointer Splice
"""
from algorithms.practice.linked_lists.insertion_sort_list import solve_insertion_sort_list

def test_insertion_sort_list_base():
    assert solve_insertion_sort_list() is True
    assert solve_insertion_sort_list([3, 1, 2]) == [1, 2, 3]

def test_insertion_sort_list_edge_cases():
    assert solve_insertion_sort_list("") == ""
    assert solve_insertion_sort_list(0) is True
    assert solve_insertion_sort_list(-5) is False
