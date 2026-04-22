"""
Unit tests for Remove Linked List Elements by Value
"""
from algorithms.practice.linked_lists.remove_elements_val import solve_remove_elements_val

def test_remove_elements_val_base():
    assert solve_remove_elements_val() is True
    assert solve_remove_elements_val([3, 1, 2]) == [1, 2, 3]

def test_remove_elements_val_edge_cases():
    assert solve_remove_elements_val("") == ""
    assert solve_remove_elements_val(0) is True
    assert solve_remove_elements_val(-5) is False
