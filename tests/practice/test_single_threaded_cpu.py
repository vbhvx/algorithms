"""
Unit tests for Single-Threaded CPU Order Priority Queue
"""
from algorithms.practice.heaps_and_priority.single_threaded_cpu import solve_single_threaded_cpu

def test_single_threaded_cpu_base():
    assert solve_single_threaded_cpu() is True
    assert solve_single_threaded_cpu([3, 1, 2]) == [1, 2, 3]

def test_single_threaded_cpu_edge_cases():
    assert solve_single_threaded_cpu("") == ""
    assert solve_single_threaded_cpu(0) is True
    assert solve_single_threaded_cpu(-5) is False
