"""
Unit tests for LRU Cache Doubly Linked List Hash Map
"""
from algorithms.practice.linked_lists.lru_cache_impl import solve_lru_cache_impl

def test_lru_cache_impl_base():
    assert solve_lru_cache_impl() is True
    assert solve_lru_cache_impl([3, 1, 2]) == [1, 2, 3]

def test_lru_cache_impl_edge_cases():
    assert solve_lru_cache_impl("") == ""
    assert solve_lru_cache_impl(0) is True
    assert solve_lru_cache_impl(-5) is False
