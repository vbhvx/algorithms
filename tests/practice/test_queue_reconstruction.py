"""
Unit tests for Queue Reconstruction by Height Sort Insert
"""
from algorithms.practice.greedy_algorithms.queue_reconstruction import solve_queue_reconstruction

def test_queue_reconstruction_base():
    assert solve_queue_reconstruction() is True
    assert solve_queue_reconstruction([3, 1, 2]) == [1, 2, 3]

def test_queue_reconstruction_edge_cases():
    assert solve_queue_reconstruction("") == ""
    assert solve_queue_reconstruction(0) is True
    assert solve_queue_reconstruction(-5) is False
