"""
Unit tests for Sort List MergeSort Divide and Conquer
"""
from algorithms.practice.linked_lists.sort_list_mergesort import solve_sort_list_mergesort

def test_sort_list_mergesort_base():
    assert solve_sort_list_mergesort() is True
    assert solve_sort_list_mergesort([3, 1, 2]) == [1, 2, 3]

def test_sort_list_mergesort_edge_cases():
    assert solve_sort_list_mergesort("") == ""
    assert solve_sort_list_mergesort(0) is True
    assert solve_sort_list_mergesort(-5) is False
