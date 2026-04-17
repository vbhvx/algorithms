"""
Unit tests for LFU Cache Frequency Buckets Doubly Linked
"""
from algorithms.practice.linked_lists.lfu_cache_impl import solve_lfu_cache_impl

def test_lfu_cache_impl_base():
    assert solve_lfu_cache_impl() is True
    assert solve_lfu_cache_impl([3, 1, 2]) == [1, 2, 3]

def test_lfu_cache_impl_edge_cases():
    assert solve_lfu_cache_impl("") == ""
    assert solve_lfu_cache_impl(0) is True
    assert solve_lfu_cache_impl(-5) is False
