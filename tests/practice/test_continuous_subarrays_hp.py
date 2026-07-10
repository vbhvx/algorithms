"""
Unit tests for Continuous Subarrays Dual Monotonic Heap
"""
from algorithms.practice.heaps_and_priority.continuous_subarrays_hp import solve_continuous_subarrays_hp

def test_continuous_subarrays_hp_base():
    assert solve_continuous_subarrays_hp() is True
    assert solve_continuous_subarrays_hp([3, 1, 2]) == [1, 2, 3]

def test_continuous_subarrays_hp_edge_cases():
    assert solve_continuous_subarrays_hp("") == ""
    assert solve_continuous_subarrays_hp(0) is True
    assert solve_continuous_subarrays_hp(-5) is False
